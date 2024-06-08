# Eighta_lib

## Description
The eighta_lib enables the processing of large .h5ad datasets without the need of load them entirely into the memory.

## Getting Started

### Dependencies
- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [Pandas](https://pandas.pydata.org/)
- [AnnData](https://anndata.readthedocs.io/en/latest/)
- [Matplotlib](https://matplotlib.org/)
- [HDF5-tools](https://github.com/HDFGroup/hdf5/blob/develop/release_docs/INSTALL)

### Installation

1. From the root of the repository, perform the command:
```
pip install .
```
This will build and install the package to your current installation of pip. It is recommended to be using a Python virtual environment for this so that you can    nuke your virtual environment and start over from scratch in case you want to test whether all dependencies are downloaded when pip installs the package.

2. Afterwards, you can simply import the package as you would any other:
```
import eighta_lib
```
## Documentation
Please check [api-documentations](api-documentations.md).

## Roadmap
- [x] Access metadata columns as pandas dataframes to find rows we want to slice.
- [x] Slice subsets to a new .h5ad file with minimal memory overhead.
- [x] Ensure that new files generated using the library are compatible with the AnnData library and, subsequently, ScanPy operations.
- [ ] Implement the Append operation to update datasets: Append adds to the end of the fields.
- [ ] Implement the Remove operation to update datasets: Remove removes elements from the fields.
- [ ] Implement the Filter operation when loading datasets: Filter provides the option to include or exclude from certain fields as long as alignment is not broken, while not modifying the dataset.
- [ ] Implement the ability to determine the file size of slices before performing a slicing operation.
- [ ] Implement the ability to slice subsets and load the subset to memory 
