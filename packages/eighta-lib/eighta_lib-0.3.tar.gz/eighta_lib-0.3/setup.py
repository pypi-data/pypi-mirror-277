from setuptools import setup, find_packages, Extension
import os
import numpy

HDF5_INCLUDE_DIR = os.getenv('HDF5_INCLUDE_DIR', '/opt/homebrew/opt/hdf5/include')
HDF5_LIB_DIR = os.getenv('HDF5_LIB_DIR', '/opt/homebrew/opt/hdf5/lib')

slicers_extension = Extension(
    'slicers',
    sources=['src/eighta_lib/c_extensions/csr_csc_slicers.c'],
    include_dirs=[numpy.get_include(), HDF5_INCLUDE_DIR],
    library_dirs=[HDF5_LIB_DIR],
    libraries=['hdf5']
)

setup(
    name='eighta_lib',
    version='0.3',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'h5py',
        'numpy',
        'pandas',
        'scipy',
        'psutil',
        'anndata'
    ],
    extras_require={
        'test': ['pytest', 'pytest-cov']
    },
    ext_modules=[slicers_extension],
    include_package_data=True,
)