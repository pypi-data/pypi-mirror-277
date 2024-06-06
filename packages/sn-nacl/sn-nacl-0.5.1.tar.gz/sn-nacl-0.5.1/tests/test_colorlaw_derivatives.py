#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from lemaitre import bandpasses
from nacl.models import helpers
from nacl.models import salt2
from nacl.models.salt2 import lightcurves
from nacl.models.salt2 import spectra
from nacl import TrainingDataset


def load(filename='snf_projected.hd5', keep=['SNF20051003-004', 'PTF10qyz', 'PTF11kly', 'SNF20080803-000']):
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


def check_color_law_grad(color_law, wl, pars):
    """
    """
    pp = pars['CL'].full

    v, jacobian = color_law(wl, pp, jac=True)
    dx = 1.E-7
    ppp = pp.copy()
    df = []
    for i in range(len(pp)):
        ppp[i] += dx
        vp, _ = color_law(wl, ppp, jac=False)
        df.append((vp-v)/dx)
        ppp[i] -= dx
    return jacobian, np.vstack(df).T


if __name__ == '__main__':
    tds = load()
    model = salt2.SALT2Like(tds, wl_grid=np.linspace(2000., 11000., 202))
    pars = model.init_pars()
    wl = np.linspace(2200., 9200., 250)
    J, Jn = check_color_law_grad(model.color_law, wl, pars)

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16,5))
    axes[0].imshow(J, aspect='auto')
    axes[0].set_title('color law derivatives - analytical')
    axes[1].imshow(Jn, aspect='auto')
    axes[1].set_title('color law derivatives - numerical')
    c = axes[2].imshow(J-Jn, aspect='auto')
    axes[2].set_title('analytical - numerical')
    plt.colorbar(c)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))
    J = J.flatten()
    Jn = Jn.flatten()
    axes[0,0].plot(J, Jn, 'k.')
    axes[0,1].plot((J-Jn)/J, 'k.')
    axes[1,0].plot(J, J-Jn, 'k.')
