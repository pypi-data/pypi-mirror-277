import unittest
import os
import shutil
import anndata as ad
import eighta_lib
from tempfile import TemporaryDirectory
import numpy as np

class TestExample(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory for the tests
        self.test_dir = TemporaryDirectory()
        self.h5ad_path = os.path.join(self.test_dir.name, "slice.h5ad")
        # Copy the test h5ad file into the temporary directory
        shutil.copy("tests/slice.h5ad", self.h5ad_path)
        
    def tearDown(self):
        # Clean up the temporary directory after the tests
        self.test_dir.cleanup()
    
    def test_pop_h5ad_throws_error_on_invalid_key(self):
        # test if this raises an error
        with self.assertRaises(KeyError):
            eighta_lib.pop_h5ad(self.h5ad_path, "X/col_2")
         
       
    def test_update_h5ad_throws_error_on_invalid_key(self):
        # test if this raises an error
        with self.assertRaises(KeyError):
            eighta_lib.update_h5ad(self.h5ad_path, "X/col_2", np.array([1, 2, 3]))
            
    def test_update_h5ad_throws_error_on_invalid_shape(self):
        # test if this raises an error
        with self.assertRaises(ValueError):
            eighta_lib.update_h5ad(self.h5ad_path, "obs/col_0", np.array([1, 2, 3]))

    def test_filter_anndata_h5ad_keeps_correct_fields(self):
        adata = ad.read_h5ad(self.h5ad_path)
        filtered_adata = eighta_lib.filter_anndata_h5ad(self.h5ad_path, include=["obs", "var/col_0"])
        self.assertEqual(adata.shape, filtered_adata.shape)
        # Check if obs keys match the expected keys
        self.assertCountEqual(adata.obs.keys(), filtered_adata.obs.keys())
        
        # Ensure only "var/col_0" is included in the filtered data
        self.assertNotEqual(len(adata.var.keys()), 1)
        self.assertCountEqual(filtered_adata.var.keys(), ['col_0'])
        self.assertCountEqual(adata.var.index, filtered_adata.var.index)
        
if __name__ == '__main__':
    unittest.main()
