import numpy as np


def reindex(id_array, input=False):
    """
    reindex an indices array to a continuous one

    Parameters
    ----------
    id_array : numpy.array
        Non-continuous index array
    input : bool 
        Wheter the input array is wanted [optional]
    Returns
    -------
    id_array_ri : numpy.array
        Continuous index array
    id_array : numpy.array
        Imput array [if input is True]
    """
    idx = np.arange(len(np.unique(id_array)))
    id_array_unique = np.unique(id_array)
    id_array_ri = np.array([idx[np.where(id_array_unique == i)[0][0]] for i in id_array])
    if input:
        return id_array_ri, id_array
    return id_array_ri
