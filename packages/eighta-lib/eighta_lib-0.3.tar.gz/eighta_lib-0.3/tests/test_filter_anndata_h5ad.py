import os
import unittest
import shutil
import numpy as np
import pandas as pd
import anndata as ad
import h5py
from tempfile import TemporaryDirectory
from eighta_lib.file_management import filter_anndata_h5ad
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
from scipy.sparse import issparse
import sys
import psutil
import subprocess
import unittest

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.h5ad_path = os.path.join(self.temp_dir.name, "slice.h5ad")
        shutil.copy("tests/slice.h5ad", self.h5ad_path)
        
        """
        The structure of tests/slice.h5ad looks as follows:
        
                / is a Group
            /X/ is a Group
                /X/data/ is a Dataset with shape (2,), dtype float64, and size 0.0000 GB
                /X/indices/ is a Dataset with shape (2,), dtype int32, and size 0.0000 GB
                /X/indptr/ is a Dataset with shape (6,), dtype int32, and size 0.0000 GB
            /layers/ is a Group
            /obs/ is a Group with index: _index
                /obs/Donor ID/ is a Group
                    /obs/Donor ID/categories/ is a Dataset with shape (3,), dtype object, and size 0.0000 GB
                    /obs/Donor ID/codes/ is a Dataset with shape (5,), dtype int8, and size 0.0000 GB
                /obs/_index/ is a Dataset with shape (5,), dtype object, and size 0.0000 GB
                /obs/col_0/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
                /obs/col_1/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
                /obs/col_2/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
                /obs/col_3/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
            /obsm/ is a Group
                /obsm/aaa/ is a Dataset with shape (5, 16), dtype float64, and size 0.0000 GB
            /obsp/ is a Group
            /uns/ is a Group
            /var/ is a Group with index: _index
                /var/_index/ is a Dataset with shape (5,), dtype object, and size 0.0000 GB
                /var/col_0/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
                /var/col_1/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
                /var/col_2/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
                /var/col_3/ is a Dataset with shape (5,), dtype float64, and size 0.0000 GB
            /varm/ is a Group
                /varm/vvv/ is a Dataset with shape (5, 16), dtype float64, and size 0.0000 GB
            /varp/ is a Group
            
                     
            X is a <class 'h5py._hl.group.Group'>
            encoding-type: csr_matrix

            layers is a <class 'h5py._hl.group.Group'>
            encoding-type: dict

            obs is a <class 'h5py._hl.group.Group'>
            encoding-type: dataframe

            obsm is a <class 'h5py._hl.group.Group'>
            encoding-type: dict

            obsm/aaa is a <class 'h5py._hl.dataset.Dataset'>
            encoding-type: array

            obsp is a <class 'h5py._hl.group.Group'>
            encoding-type: dict

            uns is a <class 'h5py._hl.group.Group'>
            encoding-type: dict

            var is a <class 'h5py._hl.group.Group'>
            encoding-type: dataframe

            varm is a <class 'h5py._hl.group.Group'>
            encoding-type: dict

            varp is a <class 'h5py._hl.group.Group'>
            encoding-type: dict

        """
        
    def tearDown(self):
        self.temp_dir.cleanup()

    def test_no_include_exclude(self):
        """Entire dataset should be loaded if no include or exclude is specified."""
        filtered_data = filter_anndata_h5ad(self.h5ad_path)
        self.assertIsInstance(filtered_data, ad.AnnData)
        
        original = ad.read_h5ad(self.h5ad_path)

        # Check if all elements of both data objects are the same
        self.assertTrue(self.ann_data_equal(filtered_data, original))

    def test_conflict_include_exclude(self):
        """Should raise ValueError if both include and exclude are provided."""
        with self.assertRaises(ValueError):
            filter_anndata_h5ad(self.h5ad_path, include=['X'], exclude=['obs']) 
            
    def test_include_key_error(self):
        """Should raise KeyError if an include key is not found."""
        with self.assertRaises(KeyError):
            filter_anndata_h5ad(self.h5ad_path, include=['nonexistent_key'])

    def test_exclude_key_error(self):
        """Should raise KeyError if an exclude key is not found."""
        with self.assertRaises(KeyError):
            filter_anndata_h5ad(self.h5ad_path, exclude=['nonexistent_key'])           

    # def test_include_everything(self):
    #     # Includes everything (from the root group)
    #     include_keys = ['/']
        
    #     filtered_data = filter_anndata_h5ad(self.h5ad_path, include=include_keys)
    #     original = ad.read_h5ad(self.h5ad_path)
        
    #     self.assertTrue(self.ann_data_equal(filtered_data, original))
    
    def test_valid_include_X_and_obs(self):
        """Test filtering with valid include keys ensures only specified keys are included."""
                
        include_keys = ['X', 'obs']
        filtered_data = filter_anndata_h5ad(self.h5ad_path, include=include_keys)
        original_data = ad.read_h5ad(self.h5ad_path)
        
        # Ensure that the 'X' matrix in the filtered data matches the original
        if issparse(original_data.X) and issparse(filtered_data.X):
            self.assertTrue((original_data.X != filtered_data.X).nnz == 0) # The original matrix is not altered
        else:
            self.assertTrue(np.array_equal(original_data.X, filtered_data.X))

        # Ensure that 'obs' DataFrame matches the original
        self.assertTrue(filtered_data.obs.equals(original_data.obs))

        self.assertFalse(original_data.var.empty) # Show that the var in the original is NOT empty
        self.assertTrue(filtered_data.var.empty) # Show that the var is now filtered
        
        self.assertFalse(len(original_data.obsm)==0) # Show that the obsm in the original is NOT empty
        self.assertTrue(len(filtered_data.obsm)==0) # Show that the obsm is now filtered
        
        self.assertFalse(len(original_data.varm)==0) # Show that the varm in the original is NOT empty
        self.assertTrue(len(filtered_data.varm)==0) # Show that the varm is now filtered
        
        # Show that the other components are still empty
        self.assertTrue(len(filtered_data.layers)==0)
        self.assertTrue(len(filtered_data.obsp)==0)
        self.assertTrue(len(filtered_data.varp)==0)
        self.assertTrue(len(filtered_data.uns)==0)
        
    def test_valid_include_no_X(self):
        """Test filtering with valid include keys ensures only specified keys are included."""
                
        include_keys = ['obs', 'var']
        filtered_data = filter_anndata_h5ad(self.h5ad_path, include=include_keys)
        original_data = ad.read_h5ad(self.h5ad_path)
        
        # Ensure that 'obs' and 'var' DataFrames match the original
        self.assertTrue(filtered_data.obs.equals(original_data.obs))
        self.assertTrue(filtered_data.var.equals(original_data.var))
        
        self.assertNotEqual(original_data.X.nnz, 0) # Show that the original X has non-zero elements
        self.assertEqual(filtered_data.X.nnz, 0) # Show that the filtered X has NO non-zero elements

        self.assertFalse(len(original_data.obsm)==0) # Show that the obsm in the original is NOT empty
        self.assertTrue(len(filtered_data.obsm)==0) # Show that the obsm is now filtered
        
        self.assertFalse(len(original_data.varm)==0) # Show that the varm in the original is NOT empty
        self.assertTrue(len(filtered_data.varm)==0) # Show that the varm is now filtered
        
        # Show that the other components are still empty
        self.assertTrue(len(filtered_data.layers)==0)
        self.assertTrue(len(filtered_data.obsp)==0)
        self.assertTrue(len(filtered_data.varp)==0)
        self.assertTrue(len(filtered_data.uns)==0)    
            
        
    def test_valid_exclude_X_and_obs(self):
        """Test filtering with valid exclude keys ensures only specified keys are excluded."""
                
        exclude_keys = ['X', 'obs']
        filtered_data = filter_anndata_h5ad(self.h5ad_path, exclude=exclude_keys)
        original_data = ad.read_h5ad(self.h5ad_path)
        
        self.assertNotEqual(original_data.X.nnz, 0) # Show that the original X has non-zero elements
        self.assertEqual(filtered_data.X.nnz, 0) # Show that the filtered X has NO non-zero elements
        
        self.assertFalse(original_data.obs.empty) # Show that the obs in the original is NOT empty
        self.assertTrue(filtered_data.obs.empty) # Show that the obs is now filtered
        
        # Ensure that the 'var' matches the original
        self.assertTrue(filtered_data.var.equals(original_data.var))

        # Ensure that the 'obsm' matches the original        
        self.assertTrue(self.are_components_dicts_equal(filtered_data.obsm, original_data.obsm))
        
        # Ensure that the 'varm' matches the original        
        self.assertTrue(self.are_components_dicts_equal(filtered_data.varm, original_data.varm))

        # Show that the other components are empty in both the original and filtered result
        self.assertTrue(len(original_data.layers)==0)
        self.assertTrue(len(filtered_data.layers)==0)
        
        self.assertTrue(len(original_data.obsp)==0)
        self.assertTrue(len(filtered_data.obsp)==0)
        
        self.assertTrue(len(original_data.varp)==0)
        self.assertTrue(len(filtered_data.varp)==0)
        
        self.assertTrue(len(original_data.uns)==0)
        self.assertTrue(len(filtered_data.uns)==0)
        
    
    # def test_valid_exclude_all(self):
    #     """Test filtering with valid exclude keys ensures only specified keys are excluded."""
                
    #     exclude_keys = ['/']
    #     filtered_data = filter_anndata_h5ad(self.h5ad_path, exclude=exclude_keys)
    #     original_data = ad.read_h5ad(self.h5ad_path)
        
    #     self.assertNotEqual(original_data.X.nnz, 0) # Show that the original X has non-zero elements
    #     self.assertEqual(filtered_data.X.nnz, 0) # Show that the filtered X has NO non-zero elements

    #     self.assertFalse(len(original_data.obsm)==0) # Show that the obsm in the original is NOT empty
    #     self.assertTrue(len(filtered_data.obsm)==0) # Show that the obsm is now filtered
        
    #     self.assertFalse(len(original_data.varm)==0) # Show that the varm in the original is NOT empty
    #     self.assertTrue(len(filtered_data.varm)==0) # Show that the varm is now filtered
        
    #     # Show that the other components are still empty
    #     self.assertTrue(len(filtered_data.layers)==0)
    #     self.assertTrue(len(filtered_data.obsp)==0)
    #     self.assertTrue(len(filtered_data.varp)==0)
    #     self.assertTrue(len(filtered_data.uns)==0)  
    
    
    def test_valid_include_deeper_than_1_group(self): 
        include_keys = ['X', '/obs/col_0']
        filtered_data = filter_anndata_h5ad(self.h5ad_path, include=include_keys)
        original_data = ad.read_h5ad(self.h5ad_path)
        
        # Ensure that the 'X' matrix in the filtered data matches the original
        if issparse(original_data.X) and issparse(filtered_data.X):
            self.assertTrue((original_data.X != filtered_data.X).nnz == 0) # The original matrix is not altered
        else:
            self.assertTrue(np.array_equal(original_data.X, filtered_data.X))
    
        # Assert shapes of 'obs' DataFrame
        expected_filtered_shape = (5, 1)  # Expected shape after filtering to include only 'col_0'
        expected_original_shape = (5, 5)  # Expected original shape with all columns
        
        # Check filtered data shape
        self.assertEqual(filtered_data.obs.shape, expected_filtered_shape)

        # Check original data shape
        self.assertEqual(original_data.obs.shape, expected_original_shape)
        
        # Check that 'col_0' in the filtered result is the same as 'col_0' in the original
        self.assertTrue(np.array_equal(filtered_data.obs['col_0'], original_data.obs['col_0']))
        
        # Check if the index of obs is not filtered out
        self.assertTrue(filtered_data.obs.index.equals(original_data.obs.index))


        self.assertFalse(original_data.var.empty) # Show that the var in the original is NOT empty
        self.assertTrue(filtered_data.var.empty) # Show that the var is now filtered
        
        self.assertFalse(len(original_data.obsm)==0) # Show that the obsm in the original is NOT empty
        self.assertTrue(len(filtered_data.obsm)==0) # Show that the obsm is now filtered
        
        self.assertFalse(len(original_data.varm)==0) # Show that the varm in the original is NOT empty
        self.assertTrue(len(filtered_data.varm)==0) # Show that the varm is now filtered
        
        # Show that the other components are still empty
        self.assertTrue(len(filtered_data.layers)==0)
        self.assertTrue(len(filtered_data.obsp)==0)
        self.assertTrue(len(filtered_data.varp)==0)
        self.assertTrue(len(filtered_data.uns)==0)     
    
    
    def ann_data_equal(self, adata1, adata2):
        """Check if two AnnData objects are equal."""
        if issparse(adata1.X) and issparse(adata2.X):
            if not (adata1.X != adata2.X).nnz == 0:
                return False
        elif not np.array_equal(adata1.X, adata2.X):
            return False

        if not adata1.obs.equals(adata2.obs):
            return False
        if not adata1.var.equals(adata2.var):
            return False

        if not self.compare_annot(adata1.obsm, adata2.obsm):
            return False
        if not self.compare_annot(adata1.varm, adata2.varm):
            return False
        if not self.compare_annot(adata1.obsp, adata2.obsp):
            return False
        if not self.compare_annot(adata1.varp, adata2.varp):
            return False

        if not self.compare_annot(adata1.uns, adata2.uns):
            return False

        return True

    def compare_annot(self, dict1, dict2):
        """Helper function to compare dictionaries in AnnData objects."""
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1.keys():
            if isinstance(dict1[key], np.ndarray) and isinstance(dict2[key], np.ndarray):
                if not np.array_equal(dict1[key], dict2[key]):
                    return False
            elif isinstance(dict1[key], csr_matrix) or isinstance(dict2[key], csr_matrix):
                if not (dict1[key] != dict2[key]).nnz == 0:
                    return False
            else:
                if dict1[key] != dict2[key]:
                    return False
        return True 
    
    @staticmethod
    def are_components_dicts_equal(comp1, comp2):
        """
        Assert that two component dictionaries are equal.

        Args:
        - comp1 (dict): First component dictionary.
        - comp2 (dict): Second component dictionary.
        """
        # Check that both dictionaries have the same keys
        if set(comp1.keys()) != set(comp2.keys()):
            return False

        # Iterate over each key and compare the arrays
        for key in comp1:
            array1 = comp1[key]
            array2 = comp2[key]

            if issparse(array1) and issparse(array2):
                # Check if the nonzero elements are the same
                if (array1 != array2).nnz != 0:
                    return False
            else:
                # Use np.array_equal for dense arrays
                if not np.array_equal(array1, array2):
                    return False

        return True

if __name__ == '__main__':
    unittest.main()