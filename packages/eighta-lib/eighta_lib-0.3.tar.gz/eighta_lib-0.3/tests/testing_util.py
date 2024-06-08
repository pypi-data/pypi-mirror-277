import random
import string
import numpy as np
import anndata as ad
from scipy.sparse import csr_matrix
import pandas as pd

def make_random_h5ad(size, path):
    X = csr_matrix(np.random.poisson(1, size=size), dtype=np.float32)
    adata = ad.AnnData(X)
    adata.obs_names = [f"Cell_{i:d}" for i in range(adata.n_obs)]
    adata.var_names = [f"Gene_{i:d}" for i in range(adata.n_vars)]

    adata.obs["col0"] = np.random.rand(size[0])
    adata.obs["col1"] = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(size[0])]
    adata.obs["col2"] = [random.choice([True, False]) for x in range(size[0])]

    adata.var["col0"] = np.random.rand(size[1])
    adata.var["col1"] = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(size[1])]
    adata.var["col2"] = [random.choice([True, False]) for x in range(size[1])]

    adata.layers["a"] = np.random.random((size[0],size[1]))
    adata.layers["b"] = np.array([[''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for x in range(size[1])] for y in range(size[0])])
    adata.layers["c"] = np.array([[random.choice([True, False]) for x in range(size[1])] for y in range(size[0])])

    for x in ["a", "b", "c"]:
        adata.obsp[x] = np.random.random((size[0],size[0]))
        adata.varp[x] = np.random.random((size[1],size[1]))
        adata.obsm[x] = np.random.random((size[0], np.random.randint(5, 20)))
        adata.varm[x] = np.random.random((size[1], np.random.randint(5, 20)))

    adata.uns["a"] = {"a": 1, "b": "Hello", "c": [1, 2, 3], "d": {"a": 1, "b": "Hello", "c": [1, 2, 3]}}
    adata.uns["b"] = [random.choice(string.ascii_uppercase + string.digits) for _ in range(np.random.randint(5, 20))]
    adata.uns["c"] = random.choice([True, False])
    adata.uns["d"] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    adata.uns["e"] = np.random.randint(-1000, 1000)

    adata.write_h5ad(path)

    pass

def compare_anndata(ad1: ad.AnnData, ad2: ad.AnnData):
    # Compare X matrix
    if type(ad1.X) != type(ad2.X):
        return False
    
    if type(ad1.X) == csr_matrix:
        if not np.array_equal(ad1.X.indices, ad2.X.indices) or not np.array_equal(ad1.X.indptr, ad2.X.indptr) or not np.array_equal(ad1.X.data, ad2.X.data):
            print("X not equals")
            return False
    elif type(ad1.X) == np.ndarray:
        if not np.array_equal(ad1.X, ad2.X):
            return False
    else:
        return False
    
    # Compare layer keys
    if ad1.layers.keys() != ad2.layers.keys():
        print("layer keys not equals")
        return False
    
    # Compare layers
    for key in ad1.layers.keys():
        if type(ad1.X) != type(ad2.X):
            return False
        if type(ad1.X) == csr_matrix:
            if not np.array_equal(ad1.X.indices, ad2.X.indices) or not np.array_equal(ad1.X.indptr, ad2.X.indptr) or not np.array_equal(ad1.X.data, ad2.X.data):
                print("layer not equals:", key)
                return False
        elif not np.array_equal(ad1.layers[key], ad2.layers[key]):
            print("layer not equals:", key)
            return False
    
    # Compare obsp and varp
    for c in ["obsp", "varp"]:
        if getattr(ad1, c).keys() != getattr(ad2, c).keys():
            print("field keys not equals:", c)
            return False
        for field in getattr(ad1, c).keys():
            if type(getattr(ad2, c)[field]) != type(getattr(ad1, c)[field]):
                print("type not match", c + "/" + field)
                return False
            elif isinstance(getattr(ad1, c)[field], pd.Series):
                if not getattr(ad1, c)[field].equals(getattr(ad2, c)[field]):
                    print("pd field keys not equals:", c + "/" + field)
                    return False
            elif isinstance(getattr(ad1, c)[field], np.ndarray):
                if not np.array_equal(getattr(ad1, c)[field], getattr(ad2, c)[field]):
                    print("np field keys not equals:", c + "/" + field)
                    return False
            else:
                if getattr(ad1, c)[field] != getattr(ad2, c)[field]:
                    print("field keys not equals:", c + "/" + field)
                    return False

    # Compare obs, obsm, var, varm and uns
    for c in ["obs", "obsm", "var", "varm", "uns"]:
        if set(getattr(ad1, c + "_keys")()) != set(getattr(ad2, c + "_keys")()):
            print("field keys not equals:", c)
            print(getattr(ad1, c + "_keys")())
            print(getattr(ad2, c + "_keys")())
            return False
        for field in getattr(ad1, c + "_keys")():
            if type(getattr(ad2, c)[field]) != type(getattr(ad1, c)[field]):
                print("type not match", c + "/" + field)
                return False
            elif isinstance(getattr(ad1, c)[field], pd.Series):
                if getattr(ad1, c)[field].dtype.name == 'category':
                    if not getattr(ad1, c)[field].str.strip().equals(getattr(ad2, c)[field].str.strip()):
                        print("pd category field keys not equals:", c + "/" + field)
                        return False
                elif not getattr(ad1, c)[field].equals(getattr(ad2, c)[field]):
                    print("pd field keys not equals:", c + "/" + field)
                    return False
            elif isinstance(getattr(ad1, c)[field], np.ndarray):
                if not np.array_equal(getattr(ad1, c)[field], getattr(ad2, c)[field]):
                    print("np field keys not equals:", c + "/" + field)
                    return False
            elif isinstance(getattr(ad1, c)[field], dict):
                try:
                    np.testing.assert_equal(getattr(ad1, c)[field], getattr(ad2, c)[field])
                except:
                    print("dict field keys not equals:", c + "/" + field)
                    print(getattr(ad1, c)[field])
                    print(getattr(ad2, c)[field])
                    return False
            else:
                if getattr(ad1, c)[field] != getattr(ad2, c)[field]:
                    print("field keys not equals:", c + "/" + field)
                    return False

    return True

def compare_raw(raw1: ad.Raw, raw2: ad.Raw):

    if type(raw1.X) != type(raw2.X):
        return False
    
    if type(raw1.X) == csr_matrix:
        if not np.array_equal(raw1.X.indices, raw2.X.indices) or not np.array_equal(raw1.X.indptr, raw2.X.indptr) or not np.array_equal(raw1.X.data, raw2.X.data):
            print("X not equals")
            return False
    elif type(raw1.X) == np.ndarray:
        if not np.array_equal(raw1.X, raw2.X):
            return False
    else:
        return False
    
    if any(raw1.var_names != raw2.var_names):
        return False
    
    for c in ["var", "varm"]:
        if set(getattr(getattr(raw1, c), "keys")()) != set(getattr(getattr(raw1, c), "keys")()):
            print("field keys not equals:", c)
            print(getattr(raw1, c + "_keys")())
            print(getattr(raw1, c + "_keys")())
            return False
        for field in getattr(getattr(raw1, c), "keys")():
            if type(getattr(raw2, c)[field]) != type(getattr(raw1, c)[field]):
                print("type not match", c + "/" + field)
                return False
            elif isinstance(getattr(raw1, c)[field], pd.Series):
                if getattr(raw1, c)[field].dtype.name == 'category':
                    if not getattr(raw1, c)[field].str.strip().equals(getattr(raw2, c)[field].str.strip()):
                        print("pd category field keys not equals:", c + "/" + field)
                        return False
                elif not getattr(raw1, c)[field].equals(getattr(raw2, c)[field]):
                    print("pd field keys not equals:", c + "/" + field)
                    return False
            elif isinstance(getattr(raw1, c)[field], np.ndarray):
                if not np.array_equal(getattr(raw1, c)[field], getattr(raw2, c)[field]):
                    print("np field keys not equals:", c + "/" + field)
                    return False
            elif isinstance(getattr(raw1, c)[field], dict):
                try:
                    np.testing.assert_equal(getattr(raw1, c)[field], getattr(raw2, c)[field])
                except:
                    print("dict field keys not equals:", c + "/" + field)
                    return False
            else:
                if getattr(raw1, c)[field] != getattr(raw2, c)[field]:
                    print("field keys not equals:", c + "/" + field)
                    return False
    return True