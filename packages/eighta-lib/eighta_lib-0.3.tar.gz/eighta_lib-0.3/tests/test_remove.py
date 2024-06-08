from tempfile import TemporaryDirectory
import shutil
import os
from util import TestingUtil
import anndata as ad
import h5py
import pandas as pd
import pytest
import eighta_lib


@pytest.fixture(name="clone_h5ad")
def fixture_clone_h5ad():
    # Set up a temporary directory for the tests
    test_dir = TemporaryDirectory()
    original_dir = "tests/slice.h5ad"

    # Create a path for the copied object
    copy_path = os.path.join(test_dir.name, "copy.h5ad")
    # Copy the h5ad to the copied object path
    shutil.copy(original_dir, copy_path)

    yield original_dir, copy_path

    test_dir.cleanup()


@pytest.fixture(name="create_h5ad")
def fixture_create_h5ad():
    # Set up a temporary directory for the tests
    test_dir = TemporaryDirectory()
    original_dir = os.path.join(test_dir.name, "source.h5ad")
    util = TestingUtil(123456789)
    util.create_h5ad(size=(10, 100), path=original_dir)

    # Create a path for the copied object
    copy_path = os.path.join(test_dir.name, "copy.h5ad")
    # Copy the h5ad to the copied object path
    shutil.copy(original_dir, copy_path)

    yield original_dir, copy_path

    test_dir.cleanup()


targets = [
    ("obsm"),
    ("obsp"),
    ("varm"),
    ("varp"),
    ("uns"),
    ("layers"),
    ("obsm/col1"),
    ("obsp/m_1"),
    ("varm/row0"),
    ("varp/m_0"),
    ("uns/dict"),
    ("uns/dict/a"),
    ("layers/layer1"),
]


@pytest.mark.parametrize("target", targets)
def test_integration_remove(create_h5ad, target):
    targets = list(filter(None, target.split("/")))
    print("Targets:", targets)

    original_dir, copy_path = create_h5ad

    ad_obj = ad.read_h5ad(original_dir)
    removed_data = eighta_lib.pop_h5ad(copy_path, target)

    curr_data = getattr(ad_obj, targets[0])
    for target in targets[1:]:
        curr_data = curr_data[target]

    TestingUtil.compare(curr_data, removed_data)

    # Assert that the edited h5ad is readable and the changes have been made
    ad_obj = ad.read_h5ad(copy_path)

    curr_data = getattr(ad_obj, targets[0])
    for target in targets[1:-1]:
        curr_data = curr_data[target]

    assert targets[-1] not in curr_data.keys()


def test_remove_raises(create_h5ad):
    original_dir, copy_path = create_h5ad
    with pytest.raises(KeyError):
        eighta_lib.pop_h5ad(copy_path, "nonexistent")

    with pytest.raises(KeyError):
        eighta_lib.pop_h5ad(copy_path, "raw/var")

    with pytest.raises(KeyError):
        eighta_lib.pop_h5ad(copy_path, "raw/X")


def test_remove_categorical(create_h5ad):
    cell_types = pd.Categorical(["Type1"] * 50 + ["Type2"] * 50)
    gene_types = pd.Categorical(["Type2"] * 50 + ["Type3"] * 50)
    dict = {"cell_types": cell_types, "gene_types": gene_types}

    # Set up a temporary directory for the tests
    test_dir = TemporaryDirectory()
    original_dir = os.path.join(test_dir.name, "source.h5ad")
    util = TestingUtil(123456789)
    util.create_h5ad(size=(100, 10), path=original_dir, obs=dict)

    # Create a path for the copied object
    copy_path = os.path.join(test_dir.name, "copy.h5ad")
    # Copy the h5ad to the copied object path
    shutil.copy(original_dir, copy_path)

    # eighta_lib.explore_hdf5_file(original_dir)
    adata = ad.read_h5ad(original_dir)

    with pytest.raises(KeyError):
        eighta_lib.pop_h5ad(copy_path, "obs/cell_types/categories")

    removed_data = eighta_lib.pop_h5ad(copy_path, "obs/cell_types")
    curr_data = adata.obs["cell_types"]
    TestingUtil.compare(removed_data, curr_data)


def test_remove_higher_level(create_h5ad):
    _, copy_path = create_h5ad

    adata = ad.read_h5ad(copy_path)
    data = pd.Series(range(10))
    adata.obs["mygroup/remove_me"] = data
    adata.write_h5ad(copy_path)

    eighta_lib.pop_h5ad(copy_path, "obs/mygroup/remove_me")

    with pytest.raises(KeyError):
        eighta_lib.pop_h5ad(copy_path, "obs/mygroup")


def test_remove_invisible_col(create_h5ad):
    _, copy_path = create_h5ad

    adata = ad.read_h5ad(copy_path)
    data = pd.Series(range(10))
    adata.obs["invisible"] = data
    adata.write_h5ad(copy_path)

    with h5py.File(copy_path, "a") as f:
        f["obs"].attrs["column-order"] = list(
            filter(lambda x: x == "invisible", f["obs"].attrs.keys())
        )

    with pytest.raises(KeyError):
        eighta_lib.pop_h5ad(copy_path, "obs/invisible")
