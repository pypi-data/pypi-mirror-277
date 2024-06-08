import unittest
import os
import shutil
import numpy as np
import pandas as pd
from tempfile import TemporaryDirectory
import anndata as ad
import h5py
from scipy.sparse import issparse
from eighta_lib import read_slice_h5ad

class TestSliceReadWrite(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory for the tests
        self.test_dir = TemporaryDirectory()
        self.h5ad_path = os.path.join(self.test_dir.name, "slice_v2.h5ad")
        # Copy the test h5ad file into the temporary directory
        shutil.copy("tests/slice_v2.h5ad", self.h5ad_path)

    def tearDown(self):
        # Clean up the temporary directory after the tests
        self.test_dir.cleanup()

    def assert_AnnData_equal(self, result, expected):
        self.assertIsInstance(result, ad.AnnData)
        self.assertEqual(result.X.shape, expected.X.shape)

        # Convert sparse matrices to dense arrays if necessary
        def to_dense(matrix):
            return matrix.toarray() if issparse(matrix) else matrix

        np.testing.assert_allclose(to_dense(result.X), to_dense(expected.X))

        # Convert views to full objects
        if result.is_view:
            result = result.copy()
        if expected.is_view:
            expected = expected.copy()

        # Align indices to ensure consistent comparison
        result.obs.index = expected.obs.index
        result.var.index = expected.var.index

        # Ensure the same column order
        result.obs = result.obs[expected.obs.columns]
        result.var = result.var[expected.var.columns]

        # Ensure the same index type
        result.obs.index = result.obs.index.astype(str)
        expected.obs.index = expected.obs.index.astype(str)

        # Align categories in Categorical columns
        for col in result.obs.select_dtypes(['category']).columns:
            result.obs[col] = result.obs[col].cat.set_categories(expected.obs[col].cat.categories)

        for col in result.var.select_dtypes(['category']).columns:
            result.var[col] = result.var[col].cat.set_categories(expected.var[col].cat.categories)

        # Remove extra keys from result.uns that are not present in expected.uns
        for key in list(result.uns.keys()):
            if key not in expected.uns:
                del result.uns[key]

        # Detailed comparison
        pd.testing.assert_frame_equal(result.obs, expected.obs)
        pd.testing.assert_frame_equal(result.var, expected.var)

        np.testing.assert_equal(result.obsm.keys(), expected.obsm.keys())
        np.testing.assert_equal(result.varm.keys(), expected.varm.keys())
        np.testing.assert_equal(result.layers.keys(), expected.layers.keys())
        np.testing.assert_equal(result.obsp.keys(), expected.obsp.keys())
        np.testing.assert_equal(result.varp.keys(), expected.varp.keys())
        np.testing.assert_equal(result.uns.keys(), expected.uns.keys())

        # Helper function to compare dense or sparse matrices
        def compare_dense_or_sparse(a, b):
            if issparse(a) and issparse(b):
                np.testing.assert_allclose(a.toarray(), b.toarray())
            else:
                np.testing.assert_allclose(a, b)

        # Compare obsm
        for key in result.obsm.keys():
            compare_dense_or_sparse(result.obsm[key], expected.obsm[key])

        # Compare varm
        for key in result.varm.keys():
            compare_dense_or_sparse(result.varm[key], expected.varm[key])

        # Compare layers
        for key in result.layers.keys():
            compare_dense_or_sparse(result.layers[key], expected.layers[key])

        # Compare obsp
        for key in result.obsp.keys():
            compare_dense_or_sparse(result.obsp[key], expected.obsp[key])

        # Compare varp
        for key in result.varp.keys():
            compare_dense_or_sparse(result.varp[key], expected.varp[key])

    def test_basic_slicing(self):
        rows = slice(0, 2)
        cols = slice(2, 5)

        result = read_slice_h5ad(self.h5ad_path, rows, cols)
        print(result)
        print(type(result))

        # Load the full data and slice for comparison
        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]
        print(expected)
        print(type(expected))

        self.assert_AnnData_equal(result, expected)

    def test_full_slice(self):
        with h5py.File(self.h5ad_path, 'r') as f:
            num_rows = f["X/indptr"].shape[0] - 1
            num_cols = f["var/_index"].shape[0]

        rows = slice(0, num_rows)
        cols = slice(0, num_cols)

        result = read_slice_h5ad(self.h5ad_path, rows, cols)

        expected = ad.read_h5ad(self.h5ad_path)

        self.assert_AnnData_equal(result, expected)

    def test_partial_slice(self):
        rows = slice(1, 4)
        cols = slice(1, 3)

        result = read_slice_h5ad(self.h5ad_path, rows, cols)

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_missing_optional_groups(self):
        # Manually remove optional groups from the test file
        with h5py.File(self.h5ad_path, 'a') as f:
            del f["layers"]
            del f["obsp"]
            del f["varp"]
            del f["uns"]

        rows = slice(0, 2)
        cols = slice(0, 2)

        result = read_slice_h5ad(self.h5ad_path, rows, cols)

        # Load the full data, remove the same optional groups, and slice for comparison
        expected = ad.read_h5ad(self.h5ad_path)
        expected.layers = {}
        expected.obsp = {}
        expected.varp = {}
        expected.uns = {}
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_non_contiguous_slicing(self):
        rows = slice(0, 5, 2)
        cols = slice(1, 4, 2)

        result = read_slice_h5ad(self.h5ad_path, rows, cols)

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_specific_columns(self):
        rows = slice(0, 5)
        cols = [0, 2, 4]

        result = read_slice_h5ad(self.h5ad_path, rows, slice(min(cols), max(cols) + 1))
        result = result[:, cols]

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_specific_rows(self):
        rows = [0, 2, 4]
        cols = slice(0, 5)

        result = read_slice_h5ad(self.h5ad_path, slice(min(rows), max(rows) + 1), cols)
        result = result[rows, :]

        expected = ad.read_h5ad(self.h5ad_path)
        expected = expected[rows, cols]

        self.assert_AnnData_equal(result, expected)

    def test_get_slice_size(self):
        with h5py.File(self.h5ad_path, 'r') as f:
            num_rows = f["X/indptr"].shape[0] - 1
            num_cols = f["var/_index"].shape[0]

        rows = slice(0, num_rows)
        cols = slice(0, num_cols)

        result = read_slice_h5ad(self.h5ad_path, rows, cols, True)

        expected = ad.read_h5ad(self.h5ad_path)

        self.assert_AnnData_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
