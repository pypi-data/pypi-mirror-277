import unittest
import numpy as np
import pandas as pd
import anndata as ad
from tempfile import TemporaryDirectory
from eighta_lib.file_management import get_group_and_children
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
from scipy.sparse import issparse
import unittest

class TestGetGroupAndChildren(unittest.TestCase):
    def test_group_with_children(self):
        group = "group1"
        group_list = ["/", "/group1", "/group1/subgroup1", "/group1/subgroup2", "/group2", "/group2/subgroup1"]
        expected = ["/group1", "/group1/subgroup1", "/group1/subgroup2"]
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

    def test_group_without_children(self):
        group = "group3"
        group_list = ["/", "/group1", "/group1/subgroup1", "/group1/subgroup2", "/group2", "/group2/subgroup1", "/group3"]
        expected = ["/group3"]
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

    def test_non_existent_group(self):
        group = "group4"
        group_list = ["/", "/group1", "/group1/subgroup1", "/group1/subgroup2", "/group2", "/group2/subgroup1", "/group3"]
        expected = []
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

    def test_empty_group_list(self):
        group = "group1"
        group_list = []
        expected = []
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

    def test_group_with_similar_names(self):
        group = "group1"
        group_list = ["/", "/group1", "/group1a", "/group1/subgroup1", "/group10/subgroup1"]
        expected = ["/group1", "/group1/subgroup1"]
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)
        
    def test_group_with_slash(self):
        group = "/group1"
        group_list = ["/", "/group1", "/group1/subgroup1", "/group1/subgroup2", "/group1/subgroup3"]
        expected = ["/group1", "/group1/subgroup1", "/group1/subgroup2", "/group1/subgroup3"]
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

    def test_group_with_case_sensitivity(self):
        group = "Group1"
        group_list = ["/", "group1", "Group1/subgroup1", "group1/Subgroup2", "group2", "group2/subgroup1"]
        expected = []
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

    def test_group_with_partial_name_match(self):
        group = "group"
        group_list = ["/", "/group", "/group/subgroup", "/group1", "/group2"]
        expected = ["/group", "/group/subgroup"]
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)
        
    def test_group_empty_name(self):
        group = ""
        group_list = ["/group", "/group/subgroup", "/group1", "/group2"]
        expected = []
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)    
    
    def test_strip_rootname_followed_by_slash(self):
        """Test stripping of the rootname followed by a slash."""
        group = "/group1"
        group_list = ["/group1", "/group1/subgroup1"]
        expected = ["/group1", "/group1/subgroup1"]
        result = get_group_and_children(group, group_list)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
