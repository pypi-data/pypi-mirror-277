import pytest
import numpy as np
import anndata as ad
import pandas as pd
from scipy.sparse import csr_matrix
from tempfile import TemporaryDirectory
import testing_util
import os
import eighta_lib.file_management as fm
import random
import string

@pytest.fixture
def make_h5ad():
    test_dir = TemporaryDirectory()
    h5ad_path = os.path.join(test_dir.name, "test.h5ad")
    testing_util.make_random_h5ad((100, 200), h5ad_path)

    yield test_dir.name, h5ad_path

    test_dir.cleanup()

@pytest.fixture
def make_empty_h5ad():
    test_dir = TemporaryDirectory()
    h5ad_path = os.path.join(test_dir.name, "test.h5ad")
    file = ad.AnnData(csr_matrix(np.random.poisson(1, size=(100, 200)), dtype=np.float32))
    file.write_h5ad(h5ad_path)

    yield test_dir.name, h5ad_path

    test_dir.cleanup()

def assert_update_col(h5ad_path, test_dir, field, col_name, test_col):
    file = ad.read_h5ad(h5ad_path)
    if isinstance(test_col, list):
        getattr(file, field)[col_name] = np.array(test_col)
    else:
        getattr(file, field)[col_name] = test_col
    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, field + "/" + col_name, test_col)
    new_file = ad.read_h5ad(h5ad_path)

    return testing_util.compare_anndata(file, new_file)

def assert_update_X(h5ad_path, test_dir, test_col):
    file = ad.read_h5ad(h5ad_path)
    file.X = test_col
    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "X", test_col)
    new_file = ad.read_h5ad(h5ad_path)

    return testing_util.compare_anndata(file, new_file)

def test_obs_var(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    for f in ["obs", "var"]:
        # Add col
        test_col = np.arange(len(getattr(file, f)))
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_0", test_col)

        test_col = list(np.full(len(getattr(file, f)), "test"))
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_1", test_col)

        test_col = np.full(len(getattr(file, f)), True)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_2", test_col)

        # Update col
        test_col = np.arange(100, len(getattr(file, f))+100)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_1", test_col)

        test_col = np.full(len(getattr(file, f)), "hello")
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_2", test_col)

        test_col = np.full(len(getattr(file, f)), False)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_0", test_col)

        # Add col in groups
        test_col = np.arange(len(getattr(file, f)))
        assert assert_update_col(h5ad_path, test_dir, f, "group/new_col_0", test_col)

        test_col = np.full(len(getattr(file, f)), "test")
        assert assert_update_col(h5ad_path, test_dir, f, "group/group/new_col_1", test_col)

        test_col = np.full(len(getattr(file, f)), True)
        assert assert_update_col(h5ad_path, test_dir, f, "group/group/group/new_col_2", test_col)

        # Update col in groups
        test_col = np.arange(100, len(getattr(file, f))+100)
        assert assert_update_col(h5ad_path, test_dir, f, "group/group/new_col_1", test_col)

        test_col = np.full(len(getattr(file, f)), "hello")
        assert assert_update_col(h5ad_path, test_dir, f, "group/group/group/new_col_2", test_col)

        test_col = np.full(len(getattr(file, f)), False)
        assert assert_update_col(h5ad_path, test_dir, f, "group/new_col_0", test_col)

def test_obsm_varm(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    for f, size in zip(["obsm", "varm"], [file.n_obs, file.n_vars]):
        # Add col
        test_col = np.full((size, 1), 11.32)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_0", test_col)

        test_col = np.full((size, 2), "test")
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_1", test_col)

        test_col = np.full((size, 10), 1)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_2", test_col)

        # Update col
        test_col = np.full((size, 1), -11.32)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_1", test_col)

        test_col = np.full((size, 4), "hello")
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_2", test_col)

        test_col = np.full((size, 3), 0)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_0", test_col)


def test_obsp_varp(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    for f, size in zip(["obsp", "varp"], [file.n_obs, file.n_vars]):
        # Add col
        test_col = np.full((size, size), 11.32)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_0", test_col)

        test_col = np.full((size, size), "test")
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_1", test_col)

        test_col = np.full((size, size), True)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_2", test_col)

        # Update col
        test_col = np.full((size, size), -22.33)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_1", test_col)

        test_col = np.full((size, size), "hello")
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_2", test_col)

        test_col = np.full((size, size), False)
        assert assert_update_col(h5ad_path, test_dir, f, "new_col_0", test_col)

        # Add col in groups
        with pytest.raises(Exception):
            test_col = np.full((size, size), 11.32)
            fm.update_h5ad(h5ad_path, f, test_col)

def test_layer(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    # Add col
    test_col = np.full((100, 200), 11.32)
    assert assert_update_col(h5ad_path, test_dir, "layers", "new_col_0", test_col)

    test_col = np.full((100, 200), "test")
    assert assert_update_col(h5ad_path, test_dir, "layers", "new_col_1", test_col)

    test_col = csr_matrix(np.random.poisson(1, size=(100, 200)), dtype=np.float32)
    assert assert_update_col(h5ad_path, test_dir, "layers", "new_col_2", test_col)

    # Update col
    test_col = np.full((100, 200), -11.32)
    assert assert_update_col(h5ad_path, test_dir, "layers", "new_col_1", test_col)

    test_col = np.full((100, 200), "hello")
    assert assert_update_col(h5ad_path, test_dir, "layers", "new_col_2", test_col)

    test_col = csr_matrix(np.random.poisson(1, size=(100, 200)), dtype=np.float32)
    assert assert_update_col(h5ad_path, test_dir, "layers", "new_col_0", test_col)

def test_X(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    test_col = np.full((file.n_obs, file.n_vars), "test")
    assert assert_update_X(h5ad_path, test_dir, test_col)

    test_col = np.full((file.n_obs, file.n_vars), 11.22)
    assert assert_update_X(h5ad_path, test_dir, test_col)

    with pytest.raises(Exception):
        test_col = np.full((file.n_vars, file.n_obs), 11.22)
        assert_update_X(h5ad_path, test_dir, test_col)
    
    test_col = csr_matrix(np.random.poisson(1, size=(file.n_obs, file.n_vars)), dtype=np.float32)
    assert assert_update_X(h5ad_path, test_dir, test_col)

def test_raw_with_ad(make_empty_h5ad):
    test_dir, h5ad_path = make_empty_h5ad
    file = ad.read_h5ad(h5ad_path)

    ad_raw = ad.AnnData(csr_matrix(np.random.poisson(1, size=(10, 20)), dtype=np.float32))
    ad_raw.var_names = [f"Gene_{i:d}" for i in range(ad_raw.n_vars)]
    ad_raw.var["col0"] = np.random.rand(20)
    ad_raw.var["col1"] = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(20)]
    ad_raw.var["col2"] = [random.choice([True, False]) for x in range(20)]
    ad_raw.varm["a"] = np.array([[''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(11)] for y in range(20)])
    file.raw = ad_raw

    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "raw", ad_raw)
    new_file = ad.read_h5ad(h5ad_path)
    
    assert testing_util.compare_raw(file.raw, new_file.raw)

    # test_col = np.full(20, 1)
    test_col_varm = np.full((20, 3), "test")
    # file.raw.var["new_col"] = test_col
    file.raw.varm["b"] = test_col_varm
    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))

    # fm.update_h5ad(h5ad_path, "raw/var/new_col", test_col.tolist())
    fm.update_h5ad(h5ad_path, "raw/varm/b", test_col_varm)

    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_raw(file.raw, new_file.raw)

    ad_raw.obs["col"] = np.random.rand(10)
    file.raw = ad_raw
    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "raw", ad_raw)
    new_file = ad.read_h5ad(h5ad_path)
    
    assert testing_util.compare_raw(file.raw, new_file.raw)

def test_raw_with_file(make_empty_h5ad):
    test_dir, h5ad_path = make_empty_h5ad
    file = ad.read_h5ad(h5ad_path)

    ad_raw = ad.AnnData(csr_matrix(np.random.poisson(1, size=(10, 20)), dtype=np.float32))
    ad_raw.var_names = [f"Gene_{i:d}" for i in range(ad_raw.n_vars)]
    ad_raw.var["col0"] = np.random.rand(20)
    ad_raw.var["col1"] = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(20)]
    ad_raw.var["col2"] = [random.choice([True, False]) for x in range(20)]
    ad_raw.varm["a"] = np.array([[''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(11)] for y in range(20)])
    ad_raw.write_h5ad(os.path.join(test_dir, "raw.h5ad"))
    file.raw = ad_raw

    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "raw", os.path.join(test_dir, "raw.h5ad"))
    new_file = ad.read_h5ad(h5ad_path)
    
    assert testing_util.compare_raw(file.raw, new_file.raw)

def test_bad_weather(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    # Shape not match
    with pytest.raises(Exception):
        test_col = np.full(200, "hello")
        assert_update_col(h5ad_path, test_dir, "obs", "group/group/group/new_col_2", test_col)
    with pytest.raises(Exception):
        test_col = np.full(200, "hello").tolist()
        assert_update_col(h5ad_path, test_dir, "obs", "group/group/group/new_col_2", test_col)
    with pytest.raises(Exception):
        test_col = np.full((200, 100), "hello")
        assert_update_col(h5ad_path, test_dir, "obsp", "new_col_2", test_col)

    # Key not found
    with pytest.raises(Exception):
        test_col = np.full(200, "hello")
        assert_update_col(h5ad_path, test_dir, "abc", "group/group/group/new_col_2", test_col)

    # Key not found
    with pytest.raises(Exception):
        test_col = pd.DataFrame()
        test_col.index = [f"Cell_{i:d}" for i in range(len(file.obs))]
        test_col["col0"] = np.arange(len(file.obs))
        test_col["col1"] = np.full(len(file.obs), "test")
        test_col["col2"] = np.full(len(file.obs), True)
        fm.update_h5ad(h5ad_path, "abc", test_col)
    
    # DF shape not match obs
    with pytest.raises(Exception):
        test_col = pd.DataFrame()
        test_col.index = [f"Cell_{i:d}" for i in range(200)]
        test_col["col0"] = np.arange(200)
        test_col["col1"] = np.full(200, "test")
        test_col["col2"] = np.full(200, True)
        fm.update_h5ad(h5ad_path, "obs", test_col)

    # DF shape not match var
    with pytest.raises(Exception):
        test_col = pd.DataFrame()
        test_col.index = [f"Cell_{i:d}" for i in range(100)]
        test_col["col0"] = np.arange(100)
        test_col["col1"] = np.full(100, "test")
        test_col["col2"] = np.full(100, True)
        fm.update_h5ad(h5ad_path, "var", test_col)

    # Type not match obs
    with pytest.raises(Exception):
        fm.update_h5ad(h5ad_path, "obs", np.arange(100))
    with pytest.raises(Exception):
        fm.update_h5ad(h5ad_path, "obs", "test")
    with pytest.raises(Exception):
        fm.update_h5ad(h5ad_path, "obs", np.array)

    # Create group in obsp
    with pytest.raises(Exception):
        fm.update_h5ad(h5ad_path, "obsp/group/a", np.full((100, 100), 11.32))

def test_df(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    
    file = ad.read_h5ad(h5ad_path)
    test_col = pd.DataFrame()
    test_col.index = [f"Cell_{i:d}" for i in range(len(file.obs))]
    test_col["col0"] = np.arange(len(file.obs))
    test_col["col1"] = np.full(len(file.obs), "test")
    test_col["col2"] = np.full(len(file.obs), True)

    file.obs["col0"] = np.arange(len(file.obs))
    file.obs["col1"] = np.full(len(file.obs), "test")
    file.obs["col2"] = np.full(len(file.obs), True)

    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "obs", test_col)
    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_anndata(file, new_file)

def test_dict(make_h5ad):
    test_dir, h5ad_path = make_h5ad
    file = ad.read_h5ad(h5ad_path)

    # Check obsp
    test_col = {"a": np.full((file.n_obs, file.n_obs), 11.2), 
                "b": np.full((file.n_obs, file.n_obs), "test"), 
                "c": np.full((file.n_obs, file.n_obs), True)}

    file.obsp["a"] = np.full((file.n_obs, file.n_obs), 11.2)
    file.obsp["b"] = np.full((file.n_obs, file.n_obs), "test")
    file.obsp["c"] = np.full((file.n_obs, file.n_obs), True)

    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "obsp", test_col)
    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_anndata(file, new_file)

    # Check obsm
    test_col = {"a": np.full((file.n_obs, 1), 11.2), 
                "b": np.full((file.n_obs, file.n_obs), "test"), 
                "c": np.full((file.n_obs, 10), True)}

    file.obsm["a"] = np.full((file.n_obs, 1), 11.2)
    file.obsm["b"] = np.full((file.n_obs, file.n_obs), "test")
    file.obsm["c"] = np.full((file.n_obs, 10), True)

    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "obsm", test_col)
    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_anndata(file, new_file)

    # Check uns
    test_col = {"a": np.full((file.n_obs, 1), 11.2), 
                "b": np.full((file.n_obs, file.n_obs), "test"), 
                "c": np.full((file.n_obs, 10), True),
                "d": 2,
                "e": "test"}

    file.uns["a"] = np.full((file.n_obs, 1), 11.2)
    file.uns["b"] = np.full((file.n_obs, file.n_obs), "test")
    file.uns["c"] = np.full((file.n_obs, 10), True)
    file.uns["d"] = 2
    file.uns["e"] = "test"

    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "uns", test_col)
    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_anndata(file, new_file)

def test_repeat(make_h5ad):
    test_dir, h5ad_path = make_h5ad

    file = ad.read_h5ad(h5ad_path)
    file.obs["new_col"] = np.full(file.n_obs, "test")
    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    fm.update_h5ad(h5ad_path, "obs/new_col", "test")
    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_anndata(file, new_file)


def test_uns(make_empty_h5ad):
    test_dir, h5ad_path = make_empty_h5ad
    file = ad.read_h5ad(h5ad_path)

    test_col = True
    assert assert_update_col(h5ad_path, test_dir, "uns", "a", test_col)

    test_col = {"a": 1, 
                "b": "test", 
                "c": np.array([1,2,3]), 
                "d": {"a": 1, "b": "test", "c": np.array([1,2,3])}, 
                "e": [1,2,3],
                # "f": pd.DataFrame([1,2,3]),
                "g": ["test1", "test2", "test3"]}
                # "h": pd.Categorical(["test", "test1", "test", "test2", "test1"])}

    assert assert_update_col(h5ad_path, test_dir, "uns", "b", test_col)

    # test_col = np.full(13, "test")
    # file = ad.read_h5ad(h5ad_path)
    # file.uns["c"] = test_col
    # file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    # file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    # fm.update_h5ad(h5ad_path, "uns/c", pd.DataFrame(test_col))
    # new_file = ad.read_h5ad(h5ad_path)

    # assert testing_util.compare_anndata(file, new_file)

    test_col = ["test1", "test2", "test3"]
    assert assert_update_col(h5ad_path, test_dir, "uns", "d", test_col)

    test_col = [1, 2, 3]
    assert assert_update_col(h5ad_path, test_dir, "uns", "e", test_col)

    ad_col_path = os.path.join(test_dir, "ad_col.h5ad")
    testing_util.make_random_h5ad((100, 200), ad_col_path)
    ad_col = ad.AnnData(csr_matrix(np.random.poisson(1, size=(100, 200)), dtype=np.float32))
    ad_col.write_h5ad(ad_col_path)
    ad_col = ad.read_h5ad(ad_col_path)
    fm.update_h5ad(h5ad_path, "uns/e", ad_col)
    file.uns["e"] = ad_col
    file.write_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    file = ad.read_h5ad(os.path.join(test_dir, "adtest.h5ad"))
    new_file = ad.read_h5ad(h5ad_path)

    assert testing_util.compare_anndata(file.uns["e"], new_file.uns["e"])


