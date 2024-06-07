###########    READ   ###########

##   Use snf_fit to fit the data
##   Use snf_plot to shpw the relevant plots after the fit
##   The .lib files need to be uncommented in the model if they are and also present( not .delete)
##   The hd5 file needs to be in the same directory as this file





import numpy as np
import pylab as pl
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)
from nacl import dataset
from nacl.dataset import TrainingDataset
#from nacl.models.salt import SALT2Like, SALT2Eval
#from nacl.models.constraints import SALT2LikeConstraints
#from nacl.models.regularizations import NaClSplineRegularization
from nacl import minimize
from nacl.fit import fit
#import helpers



from nacl.fit import TrainSALT2Like

#from nacl.models.salt2.salt import SALT2Like
#from nacl.models.salt2.constraints import SALT2LikeConstraints
#from nacl.models.salt2.regularizations import NaClSplineRegularization

from nacl.models import salt2
import pandas as pd
from nacl.loglikelihood import LogLikelihood
from nacl.minimize import Minimizer

snf_tds = None

def load():
    global snf_tds
    if snf_tds is None:
        snf_tds = dataset.read_hdf('snf_tds_spline.hd5')
    return snf_tds

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

#SNF Fitter

def snf_fit(mu_reg=1., block_names = ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL'], error=True):
    """
    Fitting the SNFactory data with SALT2 model with the addition of a simple error snake
    (optional) : var = (gamma * v) ** 2
    
    Parameters:
    ----------
    mu_reg : float 
            regularization intensity, default = 1.
    block_names : list
            Parameters to be fitted in the model, default = X0, X1, col, tmax, M0, M1, CL
    error = bool
            Whether or not to include the error snake, default = True
    
    Returns:
    --------
    res : dict
            Dictionnary containing all of the information regarding the minimisation process
            such as the final parameters, the loglikelihood (in minz), etc...
    """
    tds = load()
    tds = filter_tds(tds)
    tm = TrainSALT2Like(tds, mu_reg=mu_reg)
    res = tm.fit(block_names=block_names, fit_error_model=error)
    return res


def snf_mini_fit(tds, mu_reg=1., block_names = ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']):
    """
    Testing elements of the fit, do not use for an actual fit for snf
    """
    model = salt2.get_model(tds)
    model.init_from_training_dataset()
    model.init_from_salt2(None, stick_to_original_model=False)
    reg = salt2.get_regularization_prior(model, mu=mu_reg, order=1, check=True)
    cons = salt2.get_constraint_prior(model, linear=True,
                                      mu=1.E6, Mb=-19.5,
                                      check=True)
    # dp = data
    d = {'y':tds.get_all_fluxes(), 'yerr':tds.get_all_fluxerr(), 'bads':tds.get_valid()==0}
    dp = pd.DataFrame(d)
    ll = LogLikelihood(model, reg=[reg], cons=[cons], data=dp)
    ll.pars.release()
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6, dchi2=10., max_iter=10)
    minz.plot()

    
def train(tds):
    model = SALT2Like(tds,
                      init_from_salt2_file='salt2.npz',
                      init_from_training_dataset=True)
    # we start with a simple light curve fit
    lcfit = fit(model, block_names=['X0', 'X1', 'col', 'tmax'],
                n_iter=10)

    # then, we fit the model itself
    model = SALT2Like(tds, phase_range=(-20, 50.),
                      wl_range=(3000., 10000.),
                      basis_knots=(600, 60),
                      init_from_salt2_file='salt2.npz')
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        model.pars[block_name].full[:] = lcfit['pars'][block_name].full[:]

    # fit the model
    modfit = fit(model, block_names=['M0', 'M1', 'CL'],
                 init_pars=lcfit['pars'])
    p = modfit['pars']

    # then, we release everything
    allfit = fit(model, block_names=['M0', 'M1', 'CL',
                                     'X0', 'X1', 'col', 'tmax'],
                 init_pars=p,
                 n_iter=10)

    return allfit

def plot_results(res):
    model = res['model']
    tds = model.training_dataset
    v = model(model.pars.free, jac=False)


    # residuals
    pl.figure()
    x = np.arange(len(v))
    idx = tds.spectrophotometric_data.valid > 0
    res = tds.get_all_fluxes() - v
    yerr=tds.get_all_fluxerr()
    print(x, idx, res)
    pl.plot(x, res, ls='', color='r', marker='.')
    pl.errorbar(x[idx], res[idx], yerr=tds.get_all_fluxerr()[idx],
                ls='', color='k', marker='.')

    # SN_chi2
    pl.figure()
    wres = res / yerr
    sn_chi2 = np.bincount(tds.spectrophotometric_data.sn_index[idx],
                          wres[idx]**2)
    sn_nmeas = np.bincount(tds.spectrophotometric_data.sn_index[idx])
    rchi2_sn = sn_chi2 / sn_nmeas
    pl.plot(rchi2_sn, 'ro')
    pl.title('SN $\chi^2$')
    pl.xlabel('sn_index$')
    pl.ylabel('SN $\chi^2$')
    
    pl.figure()
    pl.hist(rchi2_sn, bins=40)
    pl.title('SN $\chi^2$/n_meas')
    pl.ylabel('Counts')
    pl.xlabel('SN $\chi^2$/n_meas')
    print('SNe with chi2 > 20')
    isn = np.where(rchi2_sn > 20)[0]
    print(isn)
    print(tds.sn_data.sn_set[isn])
    print('Chi2 = ')
    print(rchi2_sn[isn])

    # spectrum chi2
    pl.figure()
    spec_chi2 = np.bincount(tds.spectrophotometric_data.spec_index[idx],
                            wres[idx]**2)
    spec_nmeas = np.bincount(tds.spectrophotometric_data.spec_index[idx])
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
    
    print('spectra with chi2 > 20')
    ispec = np.where(rchi2_spec > 20)[0]
    print(ispec)
    print(tds.spectrophotometric_data.spec_set[ispec])
    #print(tds.spectrophotometric_data.spec_set[ispec])

def plot_spectrum(tds, v, spec):
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
    pl.title(f'spectrum #{spec}', fontsize=16)
    pl.xlabel('observer frame $\lambda\ [\AA]$', fontsize=16)
    pl.ylabel('flux', fontsize=16)
    pl.legend(loc='best')
    
def plot_spectrum_snake(tds, v, spec, var):
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
    pl.ylabel('flux', fontsize=16)
    pl.legend(loc='best')

def plot_stacked_residuals(tds, model, pars, v=None):
    """
    """
    if v is None:
        v = model(pars, jac=False)

    wl = tds.spectrophotometric_data.wavelength / (1. + tds.spectrophotometric_data.z)
    ph = (tds.spectrophotometric_data.mjd - pars['tmax'].full[tds.spectrophotometric_data.sn_index]) / (1 + tds.spectrophotometric_data.z)

    pl.figure(figsize=(14, 10))
    idx = tds.get_valid() > 0
    res = tds.get_all_fluxes() - v
    wres = res / tds.get_all_fluxerr()
    pl.hexbin(wl[idx], ph[idx], wres[idx], vmin=-2.5, vmax=2.5)
    pl.title('weighted residuals', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()
    
def plot_stacked_residuals_snake(tds, model, pars, var, v=None):
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
    pl.hexbin(wl[idx], ph[idx], wres[idx], vmin=-2.5, vmax=2.5)
    pl.title('pulls with simple snake', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()

def plot_chi2(tds, model, v=None):
    if v is None:
        v = model(model.pars, jac=False)
    wl = tds.spectrophotometric_data.wavelength / (1. + tds.spectrophotometric_data.z)
    ph = (tds.spectrophotometric_data.mjd - model.pars['tmax'].full[tds.spectrophotometric_data.sn_index]) / (1 + tds.spectrophotometric_data.z)

    pl.figure(figsize=(14, 10))
    idx = tds.get_valid() > 0
    res = tds.get_all_fluxes() - v
    wres = res / tds.get_all_fluxerr()
    chi2, _, _ = np.histogram2d(wl, ph, bins=(400,50), weights=wres**2)
    cc, _, _ = np.histogram2d(wl, ph, bins=(400,50))
    rchi2 = chi2 / cc
    pl.imshow(rchi2.T[::-1,:], vmin=0, vmax=10,
              aspect='auto',
              interpolation='none',
              extent=[wl.min(), wl.max(), ph.min(), ph.max()])
    pl.title('local $\chi^2$', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()

def plot_chi2_snake(tds, model, var, v=None):
    """
    Chi2 with snake error
    """
    if v is None:
        v = model(model.pars, jac=False)
    wl = tds.spectrophotometric_data.wavelength / (1. + tds.spectrophotometric_data.z)
    ph = (tds.spectrophotometric_data.mjd - model.pars['tmax'].full[tds.spectrophotometric_data.sn_index]) / (1 + tds.spectrophotometric_data.z)

    pl.figure(figsize=(14, 10))
    idx = tds.get_valid() > 0
    res = tds.get_all_fluxes() - v
    wres = res / (tds.get_all_fluxerr() + np.sqrt(var))
    chi2, _, _ = np.histogram2d(wl, ph, bins=(400,50), weights=wres**2)
    cc, _, _ = np.histogram2d(wl, ph, bins=(400,50))
    rchi2 = chi2 / cc
    pl.imshow(rchi2.T[::-1,:], vmin=0, vmax=10,
              aspect='auto',
              interpolation='none',
              extent=[wl.min(), wl.max(), ph.min(), ph.max()])
    pl.title('local $\chi^2$', fontsize=16)
    pl.xlabel('restframe $\lambda [\AA]$', fontsize=16)
    pl.ylabel('restframe phase [days]', fontsize=16)
    pl.colorbar()

def snf_plotter(res):
    """
    Plots the relevant plots after a fit and some spectra.
    
    Parameters:
    ----------
    res : dict
    
    """
    minz = res['minz']
    ll = minz.log_likelihood
    model = ll.model
    variance_model = ll.variance_model
    tds = model.training_dataset
    
    v = model(model.pars, jac=False)
    var = variance_model(ll.pars, jac=False)
    spec0 = 0
    spec1 = 2642
    spec2 = 518
    
    plot_stacked_residuals_snake(tds, model, var, v)
    plot_chi2_snake(tds, model, var, v=None)
    plot_spectrum_snake(tds, v, spec0, var)
    plot_spectrum_snake(tds, v, spec1, var)
    plot_spectrum_snake(tds, v, spec2, var)
    

def train_orig(tds):
    """Fit a NaCl model on the TrainingDataset
    """
    # we start with a light curve fit
    model = SALT2Like(tds, init_from_salt2_file='salt2.npz')
    model.init_from_training_dataset()

    model.pars.fix()
    model.pars['X0'].release()
    model.pars['X1'].release()
    model.pars['col'].release()
    model.pars['tmax'].release()

    # reg = NaClSplineRegularization(model, to_regularize=['M0'],
    #                                order=0, mu=1.)
    wres = minimize.WeightedResiduals(model)
    chi2 = minimize.LogLikelihood(wres)
    minz = minimize.Minimizer(chi2)
    ret = minz.minimize(model.pars.free, dchi2_stop=0.1)

    # now, we fix everything but M0 (and M1)
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        model.pars[block_name].full[:] = ret['pars'][block_name].full[:]
    model.pars.fix()
    for block_name in ['M0', 'M1', 'CL']:
        model.pars[block_name].release()

    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
                                    order=0, mu=1.)
    wres = minimize.WeightedResiduals(model)
    chi2 = minimize.LogLikelihood(wres, reg=[reg])
    minz = minimize.Minimizer(chi2)
    ret = minz.minimize(model.pars.free)

    return ret, minz

def compare_pars(tds, model):
    """
    compares the parameters found in the IDR and after the NaCl fit
    
    model : SALT2Like result after fit(tds)
    """
    
    x0_tds = tds.sn_data.x0
    x1_tds = tds.sn_data.x1
    c_tds = tds.sn_data.col
    tmax_tds = tds.sn_data.tmax
    z = tds.sn_data.z
    
    x0_mod = model.pars['X0'].full[tds.sn_data.sn_index]
    x1_mod = model.pars['X1'].full[tds.sn_data.sn_index]
    c_mod = model.pars['col'].full[tds.sn_data.sn_index]
    tmax_mod = model.pars['tmax'].full[tds.sn_data.sn_index]
    
    pl.figure()
    pl.scatter(x0_tds, x0_mod)
    pl.title('X0 NaCl vs X0 IDR')
    pl.xlabel('X0 IDR')
    pl.ylabel('X0 NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(x1_tds, x1_mod)
    pl.title('X1 NaCl vs X1 IDR')
    pl.xlabel('X1 IDR')
    pl.ylabel('X1 NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(c_tds, c_mod)
    pl.title('col NaCl vs col IDR')
    pl.xlabel('col IDR')
    pl.ylabel('col NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(tmax_tds, tmax_mod)
    pl.title('tmax NaCl vs tmax IDR')
    pl.xlabel('tmax IDR')
    pl.ylabel('tmax NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(z, x0_mod/x0_tds, color='red')
    pl.title('X0 NaCl/X0 IDR vs z')
    pl.xlabel('z')
    pl.ylabel('X0 NaCl/X0 IDR')
    pl.show()

    pl.figure()
    pl.scatter(z, x1_mod/x1_tds, color='red')
    pl.title('X1 NaCl/X1 IDR vs z')
    pl.xlabel('z')
    pl.ylabel('X1 NaCl/X1 IDR')
    pl.show()
    
    pl.figure()
    pl.scatter(z, c_mod/c_tds, color='red')
    pl.title('col NaCl/col IDR vs z')
    pl.xlabel('z')
    pl.ylabel('col NaCl/col IDR')
    pl.show()
    
    pl.figure()
    pl.scatter(z, tmax_mod/tmax_tds, color='red')
    pl.title('tmax NaCl/tmax IDR vs z')
    pl.xlabel('z')
    pl.ylabel('tmax NaCl/tmax IDR')
    pl.show()

    pl.figure()
    pl.scatter(z, x1_mod-x1_tds, color='red')
    pl.title('X1 NaCl-X1 IDR vs z')
    pl.xlabel('z')
    pl.ylabel('X1 NaCl-X1 IDR')
    pl.show()
    
    pl.figure()
    pl.scatter(z, c_mod-c_tds, color='red')
    pl.title('col NaCl-col IDR vs z')
    pl.xlabel('z')
    pl.ylabel('col NaCl-col IDR')
    pl.show()
    
        
    pl.figure()
    pl.scatter(z, np.sqrt( 1/x0_mod ), label='NaCl' )
    pl.scatter(z, np.sqrt( 1/x0_tds ), label='IDR' )
    pl.xlabel('z')
    pl.ylabel(r'$\sqrt{1/X0}$')
    pl.legend()
    pl.show()
    
    pl.figure()
    pl.scatter(z, 1/x0_mod, label='NaCl')
    pl.scatter(z, 1/x0_tds, label='IDR')
    pl.xlabel('z')
    pl.ylabel('1/X0')
    pl.yscale('log')
    pl.legend()
    pl.show()
