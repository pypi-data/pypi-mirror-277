import numpy as np
import pylab as pl
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)
from nacl.dataset import TrainingDataset
from nacl import minimize
from nacl.fit import TrainSALT2Like
from nacl.models import salt2
try:
    from nacl.models.salt2 import wl_extend
except:
    logging.info(f'wl_extend not imported')
import pandas as pd
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
pl.ion()

sne_full = pd.read_hdf('../sandbox/snf_tds_not_clean.hd5', key='sn_data')
spec_full = pd.read_hdf('../sandbox/snf_tds_not_clean.hd5', key='spectrophotometric_data')
#sne_full = pd.read_hdf('../sandbox/snf_tds_spline.hd5', key='sn_data')
#spec_full = pd.read_hdf('../sandbox/snf_tds_spline.hd5', key='spectrophotometric_data')
spec_full = spec_full.assign(i_basis = [0 for x in range(len(spec_full))])
tds_full = TrainingDataset(sne_full, spectrophotometric_data=spec_full)

def filter_tds(tds, min_wavelength=3600.):
    idx = tds.spectrophotometric_data.wavelength <= min_wavelength
    logging.info(f'invalidating {idx.sum()} measurements outside wl range')
    tds.spectrophotometric_data.valid[idx] = 0
    tds.kill_sne(['PTF12iiq', 'LSQ13aiz', 'PTF11qzq', 'SN2006X'])
    # tds.kill_sne(['PTF12ikt', 'PTF10zdk', 'PTF11bgv'])
    # tds.kill_sne(['SN2004gc', 'PTF11kly', 'SN2005cg'])
    tds.kill_photometric_spectra([1121, 3116, 3307, 1803, 690,
                                   788, 1670, 1056, 1057, 732, 1614,
                                   817, 1224, 1225, 1226, 1227, 1228,
                                  1229, 1230, 1231, 1232, 1233, 1234,
                                  1235, 1236, 1237, 1238, 1239, 1240,
                                  1241, 1242, 1243, 1244, 1245, 1246,
                                  1580, 1854])

    flux = tds.spectrophotometric_data.flux
    fluxerr = tds.spectrophotometric_data.fluxerr
    ey = np.sqrt(fluxerr**2 + 0.05**2 * flux**2)
    tds.spectrophotometric_data.nt['fluxerr'] = ey

    tds.compress()

    return tds

def plot_chi2_spec(tds, v):
    """
    """
    # residuals
    pl.figure()
    x = np.arange(len(v))
    idx = tds.spectrophotometric_data.valid > 0
    res = tds.get_all_fluxes() - v
    yerr=tds.get_all_fluxerr()
    wres = res / yerr
    pl.figure()
    spec_chi2 = np.bincount(np.int64(tds.spectrophotometric_data.spec[idx]),
                            wres[idx]**2)
    spec_nmeas = np.bincount(np.int64(tds.spectrophotometric_data.spec[idx]))
    rchi2_spec = spec_chi2 / spec_nmeas
    pl.plot(rchi2_spec, 'ro')
    pl.title('spectrum $\chi^2$')
    pl.xlabel('spec_index')
    pl.ylabel('$\chi^2$')
    
    pl.figure()
    pl.hist(rchi2_spec, bins=80)
    pl.title('spec $\chi^2$/n_meas')
    pl.ylabel('Counts')
    pl.xlabel('spec $\chi^2$/n_meas')
    
def remove_chi2_spec(tds, model, pars, thresh=1e+4):
    """
    """
    v = model(pars, jac=False)
    idx = tds.spectrophotometric_data.valid > 0
    res = tds.get_all_fluxes() - v
    yerr=tds.get_all_fluxerr()
    wres = res / yerr
    pl.figure()
    spec_chi2 = np.bincount(np.int64(tds.spectrophotometric_data.spec[idx]),
                            wres[idx]**2)
    spec_nmeas = np.bincount(np.int64(tds.spectrophotometric_data.spec[idx]))
    rchi2_spec = spec_chi2 / spec_nmeas
    
    spec_to_kill = np.where(rchi2_spec > thresh)[0]
    tds.kill_photometric_spectra(spec_to_kill)
    tds.compress()
    tds.spectrophotometric_data.valid = np.int64(tds.spectrophotometric_data.valid)
    

def plot_spectrum(tds, v, spec, var):
    """
    Plotting fitted spectra
    """
    pl.figure()
    idx = tds.spectrophotometric_data.spec == spec
    pl.plot(tds.spectrophotometric_data.wavelength[idx],
            tds.spectrophotometric_data.flux[idx], 'r+')
    pl.errorbar(tds.spectrophotometric_data.wavelength[idx],
                tds.spectrophotometric_data.flux[idx],
                yerr=tds.spectrophotometric_data.fluxerr[idx],
                ls='', marker='.', label='data')
    pl.plot(tds.spectrophotometric_data.wavelength[idx], v[idx],
            color='r', lw=2, ls='-', zorder=10,
            label='trained model')
    pl.fill_between(tds.spectrophotometric_data.wavelength[idx], 
                    v[idx]-np.sqrt(var[idx]), v[idx]+np.sqrt(var[idx]), alpha = 0.5)
    pl.title(f'spectrum #{spec}', fontsize=16)
    pl.xlabel('observer frame $\lambda\ [\AA]$', fontsize=16)
    pl.ylabel('coefficient', fontsize=16)
    pl.legend(loc='best')
    
def plot_spectrum_test(tds, v, spec=0, var=None):
    """
    Plotting fitted spectra
    """
    basis = tds.basis
    ii = tds_full.spectrophotometric_data.spec == spec
    wl = tds_full.spectrophotometric_data.wavelength[ii] / (1.+tds_full.spectrophotometric_data.z[ii])
    flux_true = tds_full.spectrophotometric_data.flux[ii]
    fluxerr_true = tds_full.spectrophotometric_data.fluxerr[ii]
    #w = 1/fluxerr_true
    #W = sparse.dia_matrix((w**2, 0), shape=(len(wl),len(wl)))
    
    J = basis.eval(np.array(wl))
    J = J.tocsr()
    idx = tds.spectrophotometric_data.spec == spec
    i_basis = tds.spectrophotometric_data.i_basis[idx]
    flux = tds.spectrophotometric_data.flux[idx]
    
    JJ = J[:,i_basis]
    
    y = JJ @ flux
    y_fit = JJ @ v[idx]
    y_err_model = JJ @ var[idx]    
    #pl.plot(wl, y)
    #pl.plot(wl, flux_true)
    
    
    pl.figure()
    pl.plot(wl,
            flux_true, 'r+')
    pl.errorbar(wl,
                flux_true,
                yerr=fluxerr_true,
                ls='', marker='.', label='data')
    pl.plot(wl, y_fit,
            color='r', lw=2, ls='-', zorder=10,
            label='trained model')
    pl.fill_between(wl, 
                    y_fit-np.sqrt(y_err_model), y_fit+np.sqrt(y_err_model), alpha = 0.5)
    pl.title(f'spectrum #{spec}', fontsize=16)
    pl.xlabel('restframe frame $\lambda\ [\AA]$', fontsize=16)
    pl.ylabel('flux', fontsize=16)
    pl.legend(loc='best')

def plot_stacked_residuals_test(tds, model, pars, var, v=None):
    """
    Pulls with snake error
    """
    if v is None:
        v = model(pars, jac=False)
    basis = tds.basis
    y_fit = []
    y_err = []
    y_true = []
    yerr_true = []
    wave = []
    phase = []
    for spec in range(int(np.max(tds_full.spectrophotometric_data.spec_index))):
        ii = tds_full.spectrophotometric_data.spec_index == spec
        wl = tds_full.spectrophotometric_data.wavelength[ii] / (1.+tds_full.spectrophotometric_data.z[ii])
        ph = (tds_full.spectrophotometric_data.mjd[ii] - pars['tmax'].full[tds_full.spectrophotometric_data.sn_index][ii]) / (1 + tds_full.spectrophotometric_data.z[ii])
        wave.append(wl)
        phase.append(ph)
        flux_true = tds_full.spectrophotometric_data.flux[ii]
        y_true.append(flux_true)
        fluxerr_true = tds_full.spectrophotometric_data.fluxerr[ii]
        yerr_true.append(fluxerr_true)
        
        J = basis.eval(np.array(wl))
        J = J.tocsr()
        idx = tds.spectrophotometric_data.spec_index == spec
        i_basis = tds.spectrophotometric_data.i_basis[idx]
        JJ = J[:,i_basis]
        if len(JJ @ v[idx]) == 0:
            print('no data : spec ', spec)
        y_fit.append(JJ @ v[idx])
        y_err.append(JJ @ var[idx])
    y_fit = np.hstack(y_fit)
    y_err = np.hstack(y_err)
    y_true = np.hstack(y_true)
    yerr_true = np.hstack(yerr_true)
    print(len(y_fit))
    wl = np.hstack(wave)
    ph = np.hstack(phase)

    pl.figure(figsize=(14, 10))
    
    res = y_true - y_fit
    wres = res / (yerr_true + np.sqrt(y_err) )
    
    ii = ph < 50.
    if len(ph[ii]) != len(ph):
        logging.warning(f'Phase > 50 exists fit not very good')
    
    pl.hexbin(wl[ii], ph[ii], wres[ii], vmin=-2.5, vmax=2.5)
    pl.title('pulls with simple snake', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()
  
def plot_stacked_residuals(tds, model, pars, var, v=None):
    """
    Pulls with snake error
    """
    if v is None:
        v = model(pars, jac=False)

    wl = tds.spectrophotometric_data.wavelength / (1. + tds.spectrophotometric_data.z)
    ph = (tds.spectrophotometric_data.mjd - pars['tmax'].full[tds.spectrophotometric_data.sn_index]) / (1 + tds.spectrophotometric_data.z)

    pl.figure(figsize=(14, 10))
    idx = tds.get_valid() > 0
    res = tds.get_all_fluxes() - v
    wres = res / (tds.get_all_fluxerr() + np.sqrt(var))
    
    ii = ph[idx] < 50.
    if len(ph[idx][ii]) != len(ph[idx]):
        logging.warning(f'Phase > 50 exists fit not very good')
    
    pl.hexbin(wl[idx][ii], ph[idx][ii], wres[idx][ii], vmin=-2.5, vmax=2.5)
    pl.title('pulls with simple snake', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()

def plot_chi2(tds, model, pars, var, v=None):
    """
    Chi2 with snake error
    """
    if v is None:
        v = model(pars, jac=False)
    wl = tds.spectrophotometric_data.wavelength / (1. + tds.spectrophotometric_data.z)
    ph = (tds.spectrophotometric_data.mjd - pars['tmax'].full[tds.spectrophotometric_data.sn_index]) / (1 + tds.spectrophotometric_data.z)
    ii = ph < 50
    pl.figure(figsize=(14, 10))
    idx = tds.get_valid() > 0
    res = tds.get_all_fluxes() - v
    wres = res / (tds.get_all_fluxerr() + np.sqrt(var))
    chi2, _, _ = np.histogram2d(wl[ii], ph[ii], bins=(400,50), weights=wres[ii]**2)
    cc, _, _ = np.histogram2d(wl[ii], ph[ii], bins=(400,50))
    rchi2 = chi2 / cc
    pl.imshow(rchi2.T[::-1,:], vmin=0, vmax=10,
              aspect='auto',
              interpolation='none',
              extent=[wl[ii].min(), wl[ii].max(), ph[ii].min(), ph[ii].max()])
    pl.title('local $\chi^2$', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()

if __name__ == '__main__':
    tds = TrainingDataset.read_hdf('../sandbox/snf_projected_200.hd5')
    #tds = TrainingDataset.read_hdf('../sandbox/snf_projected_450.hd5')
    #tds = TrainingDataset.read_hdf('../sandbox/snf_projected_test.hd5')
    
    tds = filter_tds(tds, min_wavelength=3600.)
    
    tds.spectrophotometric_data.valid = np.int64(tds.spectrophotometric_data.valid)  #should be looked at
    
    try:
        grid = wl_extend()
    except:
        gird = np.linspace(2000., 11000., 200)
    
    #model = salt2.SALT2Like(tds, wl_grid = grid)
    #pars = model.init_pars()
    #remove_chi2_spec(tds, model, pars, thresh=1e+2)
    
    model = salt2.SALT2Like(tds, wl_grid = grid)
    pars = model.init_pars()
    v_init = model(pars)
    tm = TrainSALT2Like(tds, mu_reg=1, mu_cons=1e-10)
    #res = tm.fit(block_names=['X0', 'X1', 'col', 'tmax'], pars=pars, fit_error_model=True)
    #res = tm.fit(block_names=['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL'], pars=pars, fit_error_model=False)
    res = tm.fit_by_blocks(block_names=['X0', 'X1', 'col', 'tmax'], pars=pars, fit_error_model=True)
    minz = res['minz']
    m = minz.log_likelihood.model
    v = m(res['pars'])
    try:
        v_err = minz.log_likelihood.variance_model(res['pars'])
    except:
        v_err = np.zeros(len(v))
    
    plot_spectrum_test(tds, v, 14, v_err)
    #plot_spectrum_test(tds, v_init, 0, v_err)
    plot_spectrum(tds, v, 14, v_err)
    #plot_spectrum(tds, v_init, 0, v_err)
    plot_spectrum_test(tds, v, 24, v_err)
    plot_spectrum(tds, v, 24, v_err)
    plot_stacked_residuals(tds, m, res['pars'], v_err, v=v)
    #plot_stacked_residuals_test(tds, m, res['pars'], v_err, v=v)
    #plot_stacked_residuals(tds, model, pars, v_err, v=v_init)
    #import test_snf
    #test_snf.compare_pars(tds, res['pars'])    
    #plot_chi2(tds, m, res['pars'], v_err, v=v)
