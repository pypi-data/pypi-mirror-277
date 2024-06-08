import os
import unittest
import shutil
import numpy as np
import pandas as pd
import anndata as ad
import h5py
from tempfile import TemporaryDirectory
from eighta_lib.slicing import write_slice_h5ad
from scipy.sparse import csr_matrix, issparse


class TestSliceToNewFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.h5ad_path = os.path.join(self.test_dir.name, "slice_v2.h5ad")
        self.dest_file_path = os.path.join(self.test_dir.name, "sliced.h5ad")
        self.compressed_h5ad_path = os.path.join(self.test_dir.name, "slice_v2_compressed.h5ad")
        shutil.copy("tests/slice_v2.h5ad", self.h5ad_path)
        shutil.copy("tests/slice_v2_compressed.h5ad", self.compressed_h5ad_path)

    def tearDown(self):
        self.test_dir.cleanup()

    def assert_AnnData_equal(self, result, expected):
        self.assertIsInstance(result, ad.AnnData)
        self.assertEqual(result.X.shape, expected.X.shape)
        if issparse(result.X) and issparse(expected.X):
            np.testing.assert_allclose(result.X.toarray(), expected.X.toarray())
        else:
            np.testing.assert_allclose(result.X, expected.X)

        if result.is_view:
            result = result.copy()
        if expected.is_view:
            expected = expected.copy()

        result.obs.index = expected.obs.index
        result.var.index = expected.var.index

        result.obs = result.obs[expected.obs.columns]
        result.var = result.var[expected.var.columns]

        print("Result obs types:", result.obs.dtypes)
        print("Expected obs types:", expected.obs.dtypes)
        print("Result obs columns:", result.obs.columns)
        print("Expected obs columns:", expected.obs.columns)
        print("Result obs:\n", result.obs)
        print("Expected obs:\n", expected.obs)

        result.obs.index = result.obs.index.astype(str)
        expected.obs.index = expected.obs.index.astype(str)

        for col in result.obs.select_dtypes(['category']).columns:
            result.obs[col] = result.obs[col].cat.set_categories(expected.obs[col].cat.categories)

        for col in result.var.select_dtypes(['category']).columns:
            result.var[col] = result.var[col].cat.set_categories(expected.var[col].cat.categories)

        for key in list(result.uns.keys()):
            if key not in expected.uns:
                del result.uns[key]

        try:
            pd.testing.assert_frame_equal(result.obs, expected.obs)
        except AssertionError as e:
            print("Obs DataFrame mismatch:", e)
            raise

        try:
            pd.testing.assert_frame_equal(result.var, expected.var)
        except AssertionError as e:
            print("Var DataFrame mismatch:", e)
            raise

        np.testing.assert_equal(result.obsm.keys(), expected.obsm.keys())
        np.testing.assert_equal(result.varm.keys(), expected.varm.keys())
        np.testing.assert_equal(result.layers.keys(), expected.layers.keys())
        np.testing.assert_equal(result.obsp.keys(), expected.obsp.keys())
        np.testing.assert_equal(result.varp.keys(), expected.varp.keys())
        np.testing.assert_equal(result.uns.keys(), expected.uns.keys())

        for key in result.obsm.keys():
            if issparse(result.obsm[key]) and issparse(expected.obsm[key]):
                np.testing.assert_allclose(result.obsm[key].toarray(), expected.obsm[key].toarray())
            else:
                np.testing.assert_allclose(result.obsm[key], expected.obsm[key])

        for key in result.varm.keys():
            if issparse(result.varm[key]) and issparse(expected.varm[key]):
                np.testing.assert_allclose(result.varm[key].toarray(), expected.varm[key].toarray())
            else:
                np.testing.assert_allclose(result.varm[key], expected.varm[key])

        for key in result.layers.keys():
            if issparse(result.layers[key]) and issparse(expected.layers[key]):
                np.testing.assert_allclose(result.layers[key].toarray(), expected.layers[key].toarray())
            else:
                np.testing.assert_allclose(result.layers[key], expected.layers[key])

        for key in result.obsp.keys():
            if issparse(result.obsp[key]) and issparse(expected.obsp[key]):
                np.testing.assert_allclose(result.obsp[key].toarray(), expected.obsp[key].toarray())
            else:
                np.testing.assert_allclose(result.obsp[key], expected.obsp[key])

        for key in result.varp.keys():
            if issparse(result.varp[key]) and issparse(expected.varp[key]):
                np.testing.assert_allclose(result.varp[key].toarray(), expected.varp[key].toarray())
            else:
                np.testing.assert_allclose(result.varp[key], expected.varp[key])

    def test_basic_slicing(self):
        rows = slice(0, 2)
        cols = slice(2, 5)

        write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)
        result = ad.read_h5ad(self.dest_file_path)

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_full_slice(self):
        with h5py.File(self.h5ad_path, 'r') as f:
            num_rows = f["X/indptr"].shape[0] - 1
            num_cols = f["var/_index"].shape[0]

        rows = slice(0, num_rows)
        cols = slice(0, num_cols)

        write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)
        result = ad.read_h5ad(self.dest_file_path)

        expected = ad.read_h5ad(self.h5ad_path)

        self.assert_AnnData_equal(result, expected)

    def test_partial_slice(self):
        rows = slice(1, 4)
        cols = slice(1, 3)

        write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)
        result = ad.read_h5ad(self.dest_file_path)

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_empty_slice(self):
        rows = slice(0, 0)
        cols = slice(0, 0)

        with self.assertRaises(ValueError):
            write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)

    def test_non_contiguous_slicing(self):
        rows = slice(0, 5, 2)
        cols = slice(1, 4, 2)

        write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)
        result = ad.read_h5ad(self.dest_file_path)

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_different_data_types(self):
        adata = ad.AnnData(
            X=csr_matrix(np.random.rand(10, 10)),
            obs=pd.DataFrame({
                'obs1': np.random.rand(10),
                'obs2': np.random.randint(0, 100, 10).astype('int8')
            }),
            var=pd.DataFrame({
                'var1': np.random.rand(10),
                'var2': np.random.choice(['A', 'B', 'C'], 10).astype('object')
            })
        )
        adata.write(self.h5ad_path)

        rows = slice(2, 5)
        cols = slice(2, 5)

        write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)
        result = ad.read_h5ad(self.dest_file_path)

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_invalid_slices(self):
        rows = slice(10, 20)  # Out of bounds
        cols = slice(10, 20)  # Out of bounds

        with self.assertRaises(ValueError):
            write_slice_h5ad(self.h5ad_path, self.dest_file_path, rows, cols)

    def test_compression_retention(self):
        rows = slice(0, 3)
        cols = slice(0, 3)

        # Perform the slicing operation
        write_slice_h5ad(self.compressed_h5ad_path, self.dest_file_path, rows, cols)
        result = h5py.File(self.dest_file_path, 'r')
        original = h5py.File(self.compressed_h5ad_path, 'r')

        def check_compression(original_group, result_group):
            for name, item in original_group.items():
                if isinstance(item, h5py.Dataset):
                    result_item = result_group[name]
                    self.assertEqual(item.compression, result_item.compression,
                                     f"Compression mismatch for dataset {name}")
                elif isinstance(item, h5py.Group):
                    check_compression(item, result_group[name])

        check_compression(original, result)

        original.close()
        result.close()

if __name__ == '__main__':
    unittest.main()
