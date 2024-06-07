#!/usr/bin/env python3

#!/usr/bin/env python3

import logging
import time

import numpy as np
import matplotlib.pyplot as plt

from numba import jit, njit

from lemaitre import bandpasses
from nacl.models import helpers
from nacl.models import salt2
from nacl.models.salt2 import lightcurves
from nacl.models.salt2 import spectra
from nacl import TrainingDataset


def load(filename='compressed_lm2', keep=None):
    """
    """
    fl = bandpasses.get_filterlib()

    if 'hd5' in filename:
        tds = TrainingDataset.read_hdf(filename)
    else:
        tds = TrainingDataset.read_parquet(filename, filterlib=fl)

    if keep is not None:
        sne = tds.sn_data.sn_set.tolist()
        for k in keep:
            sne.remove(k)
        tds.kill_sne(sne)
        tds.compress()

    return tds


def eval_deriv(X0, cl, K, zz, calib_corr, cs_corr):
    v_ = X0 * cl * calib_corr * cs_corr * zz
    r = v_[K.row] * K.data
    return r

@njit(parallel=True)
def eval_deriv_jit(X0, cl, k_row, k_data, zz, calib_corr, cs_corr):
    v_ = X0 * cl * calib_corr * cs_corr * zz
    return v_[k_row] * k_data



if __name__ == '__main__':
    tds = load()
    model = salt2.SALT2Like(tds)
    pars = model.init_pars()

    v, J = model(pars, jac=1)

    X0 = model.queue[0].X0
    cl = model.queue[0].cl
    K = model.queue[0].K
    zz = model.queue[0].zz
    calib_corr = model.queue[0].calib_corr
    cs_corr = model.queue[0].cs_corr
