from .slicing import read_slice_h5ad, write_slice_h5ad
from .file_management import update_h5ad, pop_h5ad, filter_anndata_h5ad

__version__ = "0.4"

__all__ = [
    "read_slice_h5ad",
    "write_slice_h5ad",
    "update_h5ad",
    "pop_h5ad",
    "filter_anndata_h5ad"
]
