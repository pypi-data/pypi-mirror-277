"""
"""
import logging

import os.path as op
import ctypes
import numpy as np
import scipy.sparse
import numba

class Triplet(ctypes.Structure):
    _fields_ = [("row", ctypes.c_int),
                ("col", ctypes.c_int),
                ("value", ctypes.c_double)]


lib = np.ctypeslib.load_library("_libnacl", op.dirname(op.abspath(__file__)))
lib.kron_product_by_line.restype = ctypes.c_int
lib.kron_product_by_line.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags="aligned, contiguous"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="aligned, contiguous"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, flags="aligned, contiguous"),

    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='aligned, contiguous, writeable'),
    # ctypes.POINTER(Triplet)
]


lib.kron_product_by_line_2.restype = ctypes.c_int
lib.kron_product_by_line_2.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags="aligned, contiguous"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="aligned, contiguous"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, flags="aligned, contiguous"),

    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='aligned, contiguous, writeable'),
]


lib.append.restype = ctypes.c_int
lib.append.argtypes = [
    ctypes.c_int, ctypes.c_int,
    np.ctypeslib.ndpointer(dtype=np.int64, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(dtype=np.int64, ndim=1, flags="aligned, contiguous"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="aligned, contiguous"),

    np.ctypeslib.ndpointer(dtype=np.int64, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(dtype=np.int64, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='aligned, contiguous, writeable'),

    ctypes.c_int
]



def kron_product_by_line(A, B):
    """
    """
    A = A.tocsr()
    A_indices = A.indices
    A_indptr = A.indptr
    A_data = A.data
    # B_data = np.array(B.flatten()).squeeze()

    # estimate the number of non-zero triplets
    # could be passed as an argument
    non_zero_count_A = A_indptr[1:] - A_indptr[:-1]
    #    i, _ = B.nonzero()
    #    non_zero_count_B = np.bincount(i, minlength=B.shape[0])
    estimated_result_size = (non_zero_count_A * B.shape[1]).sum()

    rows = np.zeros(estimated_result_size).astype(np.int32)
    cols = np.zeros(estimated_result_size).astype(np.int32)
    vals = np.zeros(estimated_result_size).astype(np.float64)

    n = lib.kron_product_by_line_2(A.shape[0], A.shape[1], B.shape[1],
                                   A_indices, A_indptr, A_data,
                                   B,
                                   rows, cols, vals)
    # print(n, estimated_result_size, n/estimated_result_size)

    return scipy.sparse.coo_matrix((vals[:n], (rows[:n], cols[:n])),
                                   shape=(A.shape[0], A.shape[1] * B.shape[1]))



class CooMatrixBuff:

    def __init__(self, shape, estimated_nnz, increment=1.3):
        self.shape = shape
        self.size = estimated_nnz
        self.increment = increment
        self.i = np.zeros(self.size).astype(np.int64)
        self.j = np.zeros(self.size).astype(np.int64)
        self.val = np.zeros(self.size)
        self.ptr = 0

    def _resize(self):
        logging.warning('need to resize CooMatrixBuff: revise your estimates of non-zero terms !')
        new_size = self.size * self.increment
        self.i = np.resize(self.i, new_size)
        self.j = np.resize(self.j, new_size)
        self.val = np.resize(self.val, new_size)
        self.i[self.ptr:] = 0
        self.j[self.ptr:] = 0
        self.val[self.ptr:] = 0.
        self.size = new_size

    def append(self, i, j, val, free_pars_only=False):
        """
        """
        logging.info(f'appending {len(i)} to buffer at location {self.ptr}')
        sz = len(i)
        assert (len(j) == sz) and (len(val) == sz)

        if (self.ptr + sz) > self.size:
            self._resize()

        # if free_pars_only:
        #     sz = lib.append(len(i), self.ptr,
        #                     i.astype(np.int64), j.astype(np.int64), val,
        #                     self.i, self.j, self.val,
        #                     1)
        #     self.ptr += sz
        # else:
        #     sz = lib.append(len(i), self.ptr,
        #                     i.astype(np.int64), j.astype(np.int64), val,
        #                     self.i, self.j, self.val,
        #                     0)
        #     self.ptr += sz

        if free_pars_only:
            idx = j >= 0
            sz = idx.sum()
            self.i[self.ptr:self.ptr+sz] = i[idx]
            self.j[self.ptr:self.ptr+sz] = j[idx]
            self.val[self.ptr:self.ptr+sz] = val[idx]
            self.ptr += sz
        else:
            self.i[self.ptr:self.ptr+sz] = i
            self.j[self.ptr:self.ptr+sz] = j
            self.val[self.ptr:self.ptr+sz] = val
            self.ptr += sz
        logging.info('done')

    def tocoo(self):
        r = scipy.sparse.coo_matrix((self.val[:self.ptr],
                                     (self.i[:self.ptr], self.j[:self.ptr])),
                                    self.shape)
        return r


class CooMatrixBuff2:

    def __init__(self, shape, increment=1.3):
        self.shape = shape
        self.increment = increment
        self._row = []
        self._col = []
        self._data = []
        self._idx = []

    def append(self, i, j, val):
        """
        """
        self._row.append(i)
        self._col.append(j)
        self._data.append(val)
        self._idx.append(j>=0)

    def tocoo(self):
        idx = np.hstack(self._idx)
        r = scipy.sparse.coo_matrix((np.hstack(self._data)[idx],
                                     (np.hstack(self._row)[idx],
                                      np.hstack(self._col)[idx])),
                                    self.shape)
        return r

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def data(self):
        return self._data
