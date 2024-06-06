import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import time 
import os
import os.path as op
import numpy as np
import scipy.sparse
import sksparse.cholmod

import croaks
import saunerie
from saunerie.fitparameters import FitParameters

from salt3.minimizers import minimize_nr_var_quad#, minimize_nr_qr
import salt3.simulations.generator
import salt3.models.models

import salt3.models.variancemodels
import salt3.models.regularizations
import salt3.models.constraints

import salt3.plotting.plots

from helpers import locate_test_datafile, check_grad, check_grad_var
##############################################
import pylab as pl
pl.ion()

bands = ['B','V', 'g', 'r']#, 'u'] # 
def fit_1dsplinemodelmultiband_same_lcs(N=100, bands  = bands,
                                        minimize=minimize_nr_var_quad, mu_regularization=10.,
                                        plot=False, seed=None):
    """
    """
    lc_data = salt3.simulations.generator.generate_lc_multiband(N, bands,
                                                    tmax_range=(0., 0.),
                                                    sig_range=(0., 0.),
                                                    norm_range=(1000., 1000.),
                                                    seed=seed) 
    
    model = salt3.models.models.MultiBandsModel(lc_data, rng_spline = [-100, 100], grid_size=250)
    f = salt3.models.models.VarModelResiduals(lc_data, model)
    cons = salt3.models.constraints.NonIntegralConstraints_4MultibandModel(f.pars, model, band_tmax='B')    
    reg = salt3.models.regularizations.SplineParamsRegularizationMultiband(f.pars, bands = model.bands_unique,
                                                           mu=mu_regularization)

    # initialization fit (spline parameters only)
    for bd in model.bands_unique:
        f.pars[f"flux_{bd.decode('UTF-8')}"].full[:] = 1000
        f.pars[f"theta_{bd.decode('UTF-8')}"].full[:] = 1.E-6
        f.pars[f"flux_{bd.decode('UTF-8')}"].fix()
    f.pars['tmax'].fix()
    f.pars['s'].fix()
    cons = salt3.models.constraints.NonIntegralConstraints_4MultibandModel(f.pars, model,
                                                               band_tmax='B')
    reg = salt3.models.regularizations.SplineParamsRegularizationMultiband(f.pars,
                                                           bands = model.bands_unique,
                                                           mu=mu_regularization)
    x = minimize(f, f.pars.free, reg=reg, cons=cons)
    f.pars.free = x[0]
    
    # real fit, with all parameters free 
    f.pars.release()
    for bd in model.bands_unique:
        f.pars[f"flux_{bd.decode('UTF-8')}"].full[:] = 1000

    #f.pars['flux'].full[:] = 10000
    x = minimize(f, f.pars.free, cons=cons, reg=reg)
    f.pars.free = x[0]

    if plot:
        import pylab as pl
        import matplotlib as mpl
        pl.figure()
        gs = mpl.gridspec.GridSpec(4,1)
        ax = pl.subplot(gs[0:3,0])
        dif = pl.subplot(gs[3,0], sharex=ax)
        ax.errorbar(lc_data.date, lc_data.flux, yerr=lc_data.flux_err, ls='', marker='.', color='b')
        xx = np.linspace(lc_data.date.min(), lc_data.date.max(), 100)
        xx.sort()
        try:
            tmax = f.pars['tmax'].full
        except:
            tmax = np.zeros(N)
        xdata = salt3.plotting.plots.get_xdata_for_model_evaluation2(N, tmax, lc_data.band_set, npoints=200)
        v = model(f.pars.free, data=xdata, jac=False)
        #4(6)
        for sn in lc_data.sn_set:
            for bd in model.bands_unique:
                idx = (xdata.sn == sn) & (xdata.band == bd)
                ax.plot(xdata.date[idx], v[idx], ls='-', color=pl.cm.jet(sn/xdata.sn.max()))

        dif.errorbar(lc_data.date, f(x,jac=False)*lc_data.flux_err, yerr=lc_data.flux_err, marker='.', ls='', color='b')
        dif.grid(1)
        dif.set_xlabel('x')
        dif.set_ylabel('res')
        pl.subplots_adjust(hspace=0.05)

        for bd in model.bands_unique:
            pl.figure()
            xx = np.linspace(-50., 50., 10000)
            jacobian = model.basis.eval(xx)
            pl.plot(xx, jacobian @ model.pars[f"theta_{bd.decode('UTF-8')}"].full, 'r-')
            pl.xlabel('x')
            pl.ylabel('LC template (spline model only)')
            pl.title(bd.decode('UTF-8'))
            pl.grid(1)

    return lc_data, f, cons, reg, x






def test_model_derivatives(N=200, bands = bands, seed=0):
    """                                                                                                 
    """
    lc_data = salt3.simulations.generator.generate_lc_multiband(N=N, bands=bands,
                                                    tmax_range=(-70, 70.),
                                                    sig_range=(-1, 1.),
                                                    norm_range=(1000., 1000.),
                                                    seed=seed) 
    
    model = salt3.models.models.MultiBandsModel(lc_data, rng_spline = [-100, 100], grid_size=250)
    f = salt3.models.models.VarModelResiduals(lc_data, model)

    jacobian, JJ = check_grad(model, model.pars.free)
    D = np.abs(jacobian-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-8)

    jacobian, JJ = check_grad(f, model.pars.free)
    D = np.abs(jacobian-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)

    model.pars.free[:] += np.random.uniform(-1., 1., len(model.pars.free))
    jacobian, JJ = check_grad(model, model.pars.free)
    D = np.abs(jacobian-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)

    jacobian,JJ = check_grad(f, model.pars.free)
    D = np.abs(jacobian-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
    ###  passe pas
    # model.pars.full[:] += np.random.uniform(-1., 1., len(model.pars.full))                          
    # jacobian, JJ = check_grad(model, model.pars.free)
    # D = np.abs(jacobian-JJ)
    # np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)                                     

    # jacobian,JJ = check_grad(f, model.pars.free)
    # D = np.abs(jacobian-JJ)
    # np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6) 

    # Variance model derivative test :

    variance_model = salt3.models.variancemodels.VarianceMultibandModel(model, var_init = 0.01)
    f = salt3.models.models.VarModelResiduals(lc_data, model, variance_model = variance_model)

    D0, D1 = check_grad_var(f, model.pars.free, variance_model.pars.free)
    D = np.abs(D0-D1)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)

    model = salt3.models.models.SiftoModel(lc_data, grid_size = 250, rng_spline = [-100, 100])
    variance_model = salt3.models.variancemodels.VarianceMultibandModel(model, var_init = 0.01)
    f = salt3.models.models.VarModelResiduals(lc_data, model, variance_model = variance_model)

    D0, D1 = check_grad_var(f, model.pars.free, variance_model.pars.free)
    D = np.abs(D0-D1)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
def test_1D_multibandmodelfullfit_nr():
    x_target = np.load(locate_test_datafile('test_1D_multibandmodel_solution.npy'))
    lc, f, cons, reg, x = fit_1dsplinemodelmultiband_same_lcs(N = 100, mu_regularization=10, seed = 0)
    np.testing.assert_allclose(x_target, x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)



def fit_1dmultibandmodel(N=100, bands = bands,
                         minimize=minimize_nr_var_quad, mu_regularization=20.,
                         plot=False, seed=None):
    """
    given                                                                                               
    """
    logging.info('generating data...')
    lc_data = salt3.simulations.generator.generate_lc_multiband(N=N, bands=bands,
                                                    tmax_range=(-50., 50.),
                                                    sig_range=(-0.5, 0.5),
                                                    norm_range=(100., 10000.),
                                                    seed=seed)

    model = salt3.models.models.MultiBandsModel(lc_data, grid_size=100)
    # fit initialization
    logging.info('initialization...')
    model.pars.full[:] = salt3.models.models.init_splinemodel1dmultiband(model).full[:]
    p_init = model.pars.copy()

    # minimization
    logging.info('minimization...')
    f = salt3.models.models.VarModelResiduals(lc_data, model)
    cons = salt3.models.constraints.NonIntegralConstraints_4MultibandModel(f.pars, model,
                                                               band_tmax='B')
    reg = salt3.models.regularizations.SplineParamsRegularizationMultiband(f.pars,
                                                           bands = model.bands_unique,
                                                           mu=mu_regularization)
    x = minimize(f, f.pars.free, cons=cons, reg=reg)

    if plot:
        import pylab as pl
        import matplotlib as mpl
        salt3.plotting.plots.plot_all_lcs_stacked_multiband_stretch(lc_data, model, sifto_like = False)
        
        # plot the template itself
        for bd in model.bands_unique:
            pl.figure()
            xx = np.linspace(-50., 50., 10000)
            jacobian = model.basis.eval(xx)
            pl.plot(xx, jacobian @ model.pars[f"theta_{bd.decode('UTF-8')}"].full, 'r-')
            pl.xlabel('x')
            pl.ylabel('LC template (spline model only)')
            pl.grid(1)
            pl.title('spline model band : ' + bd.decode('UTF-8'))

        # and the residuals
        pl.figure()
        pl.hist(f(f.pars.free, jac=False), bins=100)
        pl.xlabel('residuals')

    return lc_data, f, model, cons, reg, p_init, x


def test_1dmultibandmodelfullfit_with_init_200():
    ff = np.load(locate_test_datafile('test_1D_multibandmodel_fullfit_with_init_solution.npz'))
    x_target = ff['x_200']
    lc, f, model, cons, reg, p_init, x = fit_1dmultibandmodel(N=200, minimize=minimize_nr_var_quad, mu_regularization=100., plot=False, seed=0)
    x = x[0]
    np.testing.assert_allclose(x_target, x, atol=1.E-8)
    c = cons(x, jac=False)
    np.testing.assert_allclose(np.zeros_like(c), c, atol=1.E-8)

def test_1dmultibandmodelfullfit_with_init_500():
    ff = np.load(locate_test_datafile('test_1D_multibandmodel_fullfit_with_init_solution.npz'))
    x_target = ff['x_500']
    lc, f, model, cons, reg, p_init, x = fit_1dmultibandmodel(N=500, minimize=minimize_nr_var_quad, mu_regularization=200., plot=False, seed=0)
    x = x[0]
    np.testing.assert_allclose(x_target, x, atol=1.E-8)
    c = cons(x, jac=False)
    np.testing.assert_allclose(np.zeros_like(c), c, atol=1.E-8)

def test_1dmultibandmodelfullfit_with_init_1000():
    ff = np.load(locate_test_datafile('test_1D_multibandmodel_fullfit_with_init_solution.npz'))
    x_target = ff['x_1000']
    lc, f, model, cons, reg, p_init, x = fit_1dmultibandmodel(N=1000, minimize=minimize_nr_var_quad, mu_regularization=400., plot=False, seed=0)
    x = x[0]
    np.testing.assert_allclose(x_target, x, atol=1.E-8)
    c = cons(x, jac=False)
    np.testing.assert_allclose(np.zeros_like(c), c, atol=1.E-8)


#@profile
def fit_multibandsmodel_var(N=200, minimize=minimize_nr_var_quad,
                            mu_regularization=10., plot=False, seed=None, sifto_like = True, order = 4, timing = False):
    """
    """
    lc_data = salt3.simulations.generator.generate_lc_multiband(N=N, bands=bands,
                                                    tmax_range=(-50., 50.),
                                                    sig_range=(-0.5, 0.5),
                                                    norm_range=(100., 10000.),
                                                    seed=seed)
    if sifto_like:
        model = salt3.models.models.SiftoModel(lc_data, grid_size = 250, 
                                        rng_spline = [-100, 100])
    else :
        model = salt3.models.models.MultiBandsModel(lc_data, grid_size=250,
                                             rng_spline = [-100, 100])
        
    variance_model = salt3.models.variancemodels.VarianceMultibandModel(model, var_init = 0.01)
    f = salt3.models.models.VarModelResiduals(lc_data, model, variance_model = variance_model)
    cons = salt3.models.constraints.NonIntegralConstraints_4MultibandModel(f.model.pars, model,
                                                               band_tmax='B',
                                                               sifto_like = sifto_like)
    reg = salt3.models.regularizations.SplineParamsRegularizationMultiband(f.model.pars,
                                                           bands = model.bands_unique,
                                                           mu=mu_regularization,
                                                           deriv = False)
    # initialization fit (spline parameters only)
    model.pars.full[:] = salt3.models.models.init_splinemodel1dmultiband(model, mu_regularization =.01,
                                                                  deriv = False,
                                                                  sifto_like = sifto_like).full[:]
    if plot :
        salt3.plots.plot_all_lcs_stacked_multiband_stretch(lc_data, model, sifto_like = sifto_like)
    if timing : 
        t0 = time.time()
    x, log0  = minimize(f, f.model.pars.free, g0 = None, reg=reg, cons=cons, log = [])
    
    if plot:
        salt3.plots.plot_all_lcs_stacked_multiband_stretch(lc_data, model,
                                                           sifto_like = sifto_like,
                                                           varmodel = variance_model)
    if timing : 
        t1 = time.time()

    x, g, log = minimize(f, f.model.pars.free, g0 = f.VarianceModel.pars.free,
                         reg=reg, cons=cons, log = [])
    if timing : 
        t2 = time.time()

    if plot :
        salt3.plotting.plots.plot_all_lcs_stacked_multiband_stretch(lc_data, model,
                                                           sifto_like = sifto_like,
                                                           varmodel = variance_model)
        
        pl.figure()
        pl.hist(np.abs(g), bins = 'auto')
        pl.vlines(0.01, 0, 10, color = 'b',label = 'initializarion')
        pl.vlines(0.02, 0, 10, color = 'r', label = 'implementation')
        pl.text(np.abs(g).mean(), 10, f'm : {np.abs(g).mean() : .3f}, \n s : {np.abs(g).std() : .3f}')
        pl.grid(1)
        pl.legend()
            
    if timing : 
        return lc_data, f, cons, reg, x, g, log0, log, t0, t1, t2
    return lc_data, f, cons, reg, x, g



def timing(N = [10, 50, 100, 500, 1000, 5000, 10000], stock = True):

    if stock :
        T = np.array([0.024266421794891357, 0.0399980147679646, 0.0516820028424263, 0.24664335963369785, 0.4919382160545414, 2.039620816707611, 4.158022114208767  ])
        T_err = np.array([0.04793691635131836, 0.05689263343811035, 0.10866343975067139, 0.45550668239593506, 0.9045883019765218, 5.144795179367065, 11.023170948028564 ])
        ite = np.array([4, 6, 32, 87, 234, 16, 14])
        ite_err = np.array([2, 2, 2, 2, 3, 2, 2])
    else : 
        T = []
        T_err = []
        ite = []
        ite_err = []
        
        for n in N:
            lc_data, f, cons, reg, x, g, log0, log, t0, t1, t2 = fit_multibandsmodel_var(N=n, mu_regularization = n/100, timing = True)
        
            T.append((t1 - t0)/(log0[-1][0]+1))
            T_err.append((t2 - t1)/(log[-1][0]+1))
            ite.append(log0[-1][0]+1)
            ite_err.append(log[-1][0]+1)
            print('\n', n, np.array(T)[-1], np.array(T_err)[-1])
        
        T = np.array(T)
        T_err = np.array(T_err)
    x = np.array(N)
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(x, T, color = 'r', ls = '',
            marker = '.', label ='Fit flux model', markersize=20)
    ax.plot(x, T_err, color = 'b', ls = '',
            marker = '^', label ='With error model', markersize=20) 
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(which='both')
    parameters = {'axes.labelsize': 20,
                  #'axes.titlesize': 300,
                  'xtick.labelsize': 25,
                  'ytick.labelsize': 25}
    pl.rcParams.update(parameters)
    ax.grid(which='minor', alpha=0.5, linestyle='-')
    ax.set_ylabel('time per iteration (in sec)')
    ax.set_xlabel('Number of SNe (5 bands)')
    pl.legend(fontsize=20)



    
def test_1dmultiband_sifto_model():
    ff = np.load(locate_test_datafile('test_1D_multiband&Sifto_model_var_with_init_solution.npz'))
    x_sifto_target = ff['x_sifto']
    x_multi_target = ff['x_multi']
    g_sifto_target = ff['g_sifto']
    g_multi_target = ff['g_multi']  
    lc_data, f, cons_m, reg, x_multi, g_multi = fit_multibandsmodel_var(mu_regularization=50.,
                                                                        plot = False,
                                                                        sifto_like = False,
                                                                        seed = 0)

    lc_data, f, cons_s, reg, x_sifto, g_sifto = fit_multibandsmodel_var(mu_regularization=50.,
                                                                        plot = False,
                                                                        sifto_like = True,
                                                                        seed = 0)
    np.testing.assert_allclose(x_sifto_target, x_sifto, atol=1.E-8)
    np.testing.assert_allclose(x_multi_target, x_multi, atol=1.E-8)
    np.testing.assert_allclose(g_sifto_target, g_sifto, atol=1.E-8)
    np.testing.assert_allclose(g_multi_target, g_multi, atol=1.E-8)

    cs = cons_s(x_sifto, jac=False)
    cm = cons_m(x_multi, jac=False)
    np.testing.assert_allclose(np.zeros_like(cm), cm, atol=1.E-8)
    np.testing.assert_allclose(np.zeros_like(cs), cs, atol=1.E-8)

# if __name__ == "__main__":
#      test_model_derivatives(N=200)
#      test_1dmultibandmodelfullfit_with_init_200()
#      test_1dmultibandmodelfullfit_with_init_500()
#      test_1dmultibandmodelfullfit_with_init_1000()
#      test_1dmultiband_sifto_model()
