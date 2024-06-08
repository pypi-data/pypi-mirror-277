import sys
import os
import numpy as np

# Add the directory containing the .so file to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'c_extensions'))

# Now import the module
import slicers

# Create a NumPy array and use the function
array = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
slicers.print_numpy_array(array)