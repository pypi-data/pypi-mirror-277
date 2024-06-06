import numpy as np
import pylab as pl
from nacl import dataset
from nacl.dataset import TrainingDataset
from nacl.models.salt import SALT2Like
from nacl.models.constraints import SALT2LikeConstraints
from nacl.models.regularizations import NaClSplineRegularization
from nacl import minimize
import helpers

jla_tds = None

def load():
    global jla_tds
    if jla_tds is None:
        jla_tds = dataset.read_hdf('jla.hd5')
    return jla_tds

def fit(tds):
    model = SALT2Like(tds, init_from_salt2_file='salt2.npz')
    model.init_from_training_dataset()

    #  light curve fit only. Invalidate the spectral data
    valid = tds.spec_data.valid.copy()
    tds.spec_data.valid[:] = 0

    # eliminate all measurements before -20 and after +50
    idx = (tds.lc_data.mjd - model.pars['tmax'].full[tds.lc_data.sn_index])>50
    tds.lc_data.valid[idx] = 0
    idx = (tds.lc_data.mjd - model.pars['tmax'].full[tds.lc_data.sn_index])<-25
    tds.lc_data.valid[idx] = 0

    # remove u-band data
    tr = tds.get_all_transmissions()
    for k in tr:
        wl = tr[k].mean()
        if wl < 3900:
            idx = tds.lc_data.band == k
            print(f'killed {idx.sum()} measurements in {k}')
            tds.lc_data.nt.valid[idx] = 0

    # keep only the supernovae with points at least 5 days before max.
    # we need to be conservative, because tmax may vary during the fit
    idx = (tds.lc_data.mjd - model.pars['tmax'].full[tds.lc_data.sn_index])<-5
    sne = [tds.sn_data.sn_map[sni] for sni in \
           np.where((np.bincount(tds.lc_data.sn_index, idx) == 0))[0]]
    tds.kill_sne(sne)

    # remove the supernovae with strange colors
    idx = np.abs(tds.sn_data.col) > 1.
    sne = tds.sn_data.sn[idx]
    tds.kill_sne(sne)
    tds.compress()

    # re-instantiate the model
    model = SALT2Like(tds, init_from_salt2_file='salt2.npz')
    model.init_from_training_dataset()

    model.pars.fix()
    model.pars['X0'].release()
    model.pars['X1'].release()
    model.pars['col'].release()
    model.pars['tmax'].release()

    wres = minimize.WeightedResiduals(model)
    chi2 = minimize.LogLikelihood(wres)
    minz = minimize.Minimizer(chi2)

    return minz



