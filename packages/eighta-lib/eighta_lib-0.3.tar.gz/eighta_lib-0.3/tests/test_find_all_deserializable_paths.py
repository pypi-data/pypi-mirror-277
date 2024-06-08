import unittest
import h5py
import numpy as np
from io import BytesIO
from eighta_lib.file_management import find_all_deserializable_paths
from unittest.mock import MagicMock
import h5py
import unittest
import h5py
from io import BytesIO
import unittest
from io import BytesIO
import h5py

class TestFindAllDeserializablePaths(unittest.TestCase):
    def create_h5_file_1(self):
        # This method creates a lightweight in-memory HDF5 file and returns it.
        h5file = BytesIO()
        with h5py.File(h5file, 'w') as f:
            # Create groups and minimal datasets similar to the provided structure
            grp_x = f.create_group("X")
            grp_x.create_dataset("data", (1,), dtype='float64')
            grp_x.create_dataset("indices", (1,), dtype='int32')
            grp_x.create_dataset("indptr", (1,), dtype='int32')
            grp_x.attrs['encoding-type'] = 'csr_matrix'
            
            grp_layers = f.create_group("layers")
            grp_layers.create_dataset("data", (1,), dtype='float64')
            grp_layers.create_dataset("indices", (1,), dtype='int32')
            grp_layers.create_dataset("indptr", (1,), dtype='int32')
            grp_layers.attrs['encoding-type'] = 'csc_matrix'

            grp_obs = f.create_group("obs")
            grp_obs.attrs['encoding-type'] = 'dict'
            grp_obs.attrs["_index"] = "_index"
            
            grp_donor_id = grp_obs.create_group("Donor ID")
            grp_donor_id.attrs['encoding-type'] = 'categorial'  
            
            # The children of a categorical group should not be included the set returned by 'find_all_deserializable_paths'
            grp_donor_id.create_dataset("categories", (1,), dtype=h5py.special_dtype(vlen=bytes)).attrs['encoding-type'] = 'dataframe'
            grp_donor_id.create_dataset("codes", (1,), dtype='int8').attrs['encoding-type'] = 'dataframe'

            grp_obs.create_dataset("_index", (1,), dtype=h5py.special_dtype(vlen=bytes)).attrs['encoding-type'] = 'dataframe'
            for i in range(4):
                grp_obs.create_dataset(f"col_{i}", (1,), dtype='float64').attrs['encoding-type'] = 'dataframe'
                
            # Subgroup 'AnndataGroup' with an 'anndata' encoding type
            grp_anndata = grp_obs.create_group("anndataGroup")
            grp_anndata.attrs['encoding-type'] = 'anndata'
            grp_anndata.create_dataset("anndata_example_data", (10,), dtype='float32')
            
            # Subgroup 'RawDataGroup' with a 'raw' encoding type
            grp_rawdata = grp_obs.create_group("rawDataGroup")
            grp_rawdata.attrs['encoding-type'] = 'raw'
            grp_rawdata.create_dataset("raw_example_data", (10,), dtype='int16')    

            grp_obsm = f.create_group("obsm")
            grp_obsm.attrs['encoding-type'] = 'dict'
            grp_obsm.create_dataset("aaa", (1, 1), dtype='float64').attrs['encoding-type'] = 'dataframe'

            # Group 'var' setup with additional attributes and datasets
            grp_var = f.create_group("var")
            grp_var.attrs['encoding-type'] = 'dataframe' 
            grp_var.attrs["_index"] = "_index"  # Index attribute
            
            # Create a dataset '_index' with specific encoding type
            grp_var.create_dataset("_index", (1,), dtype=h5py.special_dtype(vlen=bytes)).attrs['encoding-type'] = 'arr'

            # Create datasets for columns and record their names for column order
            column_names = []
            column_names.append("_index")
            for i in range(4):
                dataset_name = f"col_{i}"
                grp_var.create_dataset(dataset_name, (1,), dtype='float64').attrs['encoding-type'] = 'arr'
                column_names.append(dataset_name)
            
            # Creating a subgroup within 'var' and adding a dataset inside this subgroup
            subgroup = grp_var.create_group("subgroup")
            # Adding a dataset inside this subgroup
            dataset_name = "subgroup/subdata"  
            subgroup.create_dataset("subdata", (10,), dtype='int32')  
            column_names.append(dataset_name)  # Append the path to the dataset in the subgroup to the column order list
            
            # Set the 'column-order' attribute to the list of column names
            grp_var.attrs['column-order'] = column_names
            
            grp_varm = f.create_group("varm")
            grp_varm.attrs['encoding-type'] = 'dict'
            grp_varm.create_dataset("vvv", (1, 1), dtype='float64').attrs['encoding-type'] = 'dataframe'
            
            grp_obsp = f.create_group("obsp") # No encoding-type specified
            # Path to this dataset will not be included 
            grp_obsp.create_dataset("obsp_data", (1, 1), dtype='float64').attrs['encoding-type'] = 'string-arr' 
            
            grp_varp = f.create_group("varp") # No encoding-type specified
            # Path to this dataset will not be included 
            grp_varp.create_dataset("varp_data", (1, 1), dtype='float64').attrs['encoding-type'] = 'string-arr'

        
        h5file.seek(0)  # Rewind the file for reading in subsequent operations
        return h5file
    
    def setUp(self):
        self.h5file_1 = self.create_h5_file_1()
                
    def test_find_all_subkey_paths(self):
        self.maxDiff = None
        with h5py.File(self.h5file_1, 'r') as f:
            expected_paths = [
                '/X', 
                '/layers', 
                '/obs/Donor ID', 
                '/obs/_index', 
                '/obs/anndataGroup/anndata_example_data', 
                '/obs/col_0', 
                '/obs/col_1', 
                '/obs/col_2', 
                '/obs/col_3', 
                '/obs/rawDataGroup/raw_example_data', 
                '/obsm/aaa', 
                '/obsp/obsp_data', 
                '/var/_index', 
                '/var/col_0', 
                '/var/col_1', 
                '/var/col_2', 
                '/var/col_3', 
                '/var/subgroup/subdata', 
                '/varm/vvv', 
                '/varp/varp_data'
            ]
            result = find_all_deserializable_paths(f)
            
            print("Expected Paths:", expected_paths)
            print("Actual Result:", result)
        
            self.assertCountEqual(result, expected_paths)

if __name__ == '__main__':
    unittest.main()
