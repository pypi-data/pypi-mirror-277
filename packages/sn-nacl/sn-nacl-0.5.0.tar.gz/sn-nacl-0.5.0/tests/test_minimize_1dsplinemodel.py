import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)


import os
import os.path as op
import numpy as np
import scipy.sparse
import sksparse.cholmod

import croaks
import saunerie
from saunerie.fitparameters import FitParameters

from salt3.minimizers import minimize_nr_var_quad, minimize_nr
import salt3.generator
import salt3.regularizations
import salt3.constraints
import salt3.models
import salt3.plots

from helpers import locate_test_datafile
from helpers import check_grad



def fit_1dsplinemodel_same_lcs(N=200, minimize=minimize_nr_var_quad, mu_regularization=500., plot=False, seed=None):
    """
    """
    lc_data = salt3.generator.generate_lc(N, tmax_range=(0., 0.),
                                          sig_range=(0., 0.),
                                          norm_range=(1000., 1000.),
                                          seed=seed)

    model = salt3.models.SplineModel1D(lc_data, grid_size=250)
    f = salt3.models.VarModelResiduals(lc_data, model)
    reg = salt3.constraints.SplineParamsRegularization(f.pars, mu=mu_regularization)
    cons = salt3.regularizations.NonIntegralConstraints(model.pars, model.spline_basis)
    
    # initialization fit (spline parameters only)
    f.pars['flux'].full[:] = 1000
    f.pars['theta'].full[:] = 1.E-6
    f.pars['flux'].fix()
    f.pars['tmax'].fix()
    f.pars['s'].fix()
    x = minimize(f, f.pars.free, reg=reg, cons=cons)
    x = x[0]
    f.pars.free = x

    # real fit, with all parameters free
    f.pars.release()
    f.pars['flux'].full[:] = 10000
    x = minimize(f, f.pars.free, cons=cons, reg=reg)
    f.pars.free = x
    
    if plot:
        import pylab as pl
        import matplotlib as mpl
        pl.figure()
        gs = mpl.gridspec.GridSpec(4,1)
        ax = pl.subplot(gs[0:3,0])
        pl.errorbar(lc_data.date, lc_data.flux, yerr=lc_data.flux_err, ls='', marker='.', color='b')
        xx = np.linspace(lc_data.date.min(), lc_data.date.max(), 100)
        xx.sort()

        try:
            tmax = f.pars['tmax'].full
        except:
            tmax = np.zeros(N)
        xdata = salt3.plots.get_xdata_for_model_evaluation(N, tmax, lc_data.band_set, npoints=200)
        v = model(f.pars.free, dp=xdata, jac=False)
        for sn in lc_data.sn_set:
            idx = xdata.sn == sn
            pl.plot(xdata.date[idx], v[idx], ls='-', color=pl.cm.jet(sn/xdata.sn.max()))
        
        pl.subplot(gs[3,0], sharex=ax)
        pl.errorbar(lc_data.date, f(x,jac=False)*lc_data.flux_err, yerr=lc_data.flux_err, marker='.', ls='', color='b')
        pl.grid(1)
        pl.xlabel('x')
        pl.ylabel('res')
        pl.subplots_adjust(hspace=0.05)        

        pl.figure()
        xx = np.linspace(-50., 50., 10000)
        jacobian = model.spline_basis.eval(xx)
        pl.plot(xx, jacobian @ model.pars['theta'].full, 'r-')
        pl.xlabel('x')
        pl.ylabel('LC template (spline model only)')
        pl.grid(1)
        
    return lc_data, f, cons, reg, x


def test_model_derivatives(N=200, seed=0):
    """
    """
    lc_data = salt3.generator.generate_lc(N=N, tmax_range=(-70., 70.),
                                          sig_range=(-1., 1.),
                                          norm_range=(10., 1000.),
                                          seed=seed)

    model = salt3.models.SplineModel1D(lc_data, grid_size=250)
    f = salt3.models.VarModelResiduals(lc_data, model)
    
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

    # en revanche, celui la, il plante ... 
    #    model.pars.full[:] += np.random.uniform(-1., 1., len(model.pars.full))
    #    jacobian, JJ = check_grad(model, model.pars.free)
    #    D = np.abs(jacobian-JJ)
    #    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
    #    jacobian,JJ = check_grad(f, model.pars.free)
    #    D = np.abs(jacobian-JJ)
    #    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)



    
def test_1dsplinemodelfullfit_nr():
    x_target = np.load(locate_test_datafile('test_1dsplinemodel_solution.npy'))
    lc, f, cons, reg, x = fit_1dsplinemodel_same_lcs(N=1000, minimize=minimize_nr, mu_regularization=500., plot=0, seed=0)
    np.testing.assert_allclose(x_target, x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)    
    


def fit_1dsplinemodel(N=200, minimize=minimize_nr, mu_regularization=500., plot=False, seed=None):
    """
    given
    """
    logging.info('generating data...')
    lc = salt3.generator.generate_lc(N=N, tmax_range=(-50., 50.),
                                     sig_range=(-0.5, 0.5),
                                     norm_range=(100., 10000.),
                                     seed=seed)
    model = salt3.models.SplineModel1D(lc, grid_size=250)

    # fit initialization
    logging.info('initialization...')    
    model.pars.full[:] = salt3.models.init_splinemodel1d(model).full[:]
    p_init = model.pars.copy()

    # minimization
    logging.info('minimization...')    
    reg = salt3.models.SplineParamsRegularization(model.pars, mu=mu_regularization)
    cons = salt3.models.NonIntegralConstraints(model.pars, model.spline_basis)
    f = salt3.models.VarModelResiduals(lc, model)
    x = minimize_nr(f, f.pars.free, cons=cons, reg=reg)

    if plot:
        import pylab as pl
        import matplotlib as mpl
        salt3.plots.plot_all_lcs_nrl(lc, model)
        salt3.plots.plot_all_lcs(lc, model)

        # plot the template itself 
        pl.figure()
        xx = np.linspace(-50., 50., 10000)
        jacobian = model.spline_basis.eval(xx)
        pl.plot(xx, jacobian @ model.pars['theta'].full, 'r-')
        pl.xlabel('x')
        pl.ylabel('LC template (spline model only)')
        pl.grid(1)
        pl.title('spline model')

        # and the residuals 
        pl.figure()
        pl.hist(f(f.pars.free, jac=False), bins=100)
        pl.xlabel('residuals')
    
    return lc, f, model, cons, reg, p_init, x
    

def test_1dsplinemodelfullfit_with_init_200():
    ff = np.load(locate_test_datafile('test_1dsplinemodel_fullfit_with_init_solution.npz'))
    x_target = ff['x_200']
    lc, f, model, cons, reg, p_init, x = fit_1dsplinemodel(N=200, minimize=minimize_nr, mu_regularization=200., plot=False, seed=0)
    np.testing.assert_allclose(x_target, x, atol=1.E-8)
    c = cons(x, jac=False)
    np.testing.assert_allclose(np.zeros_like(c), c, atol=1.E-8)

def test_1dsplinemodelfullfit_with_init_500():
    ff = np.load(locate_test_datafile('test_1dsplinemodel_fullfit_with_init_solution.npz'))
    x_target = ff['x_500']
    lc, f, model, cons, reg, p_init, x = fit_1dsplinemodel(N=500, minimize=minimize_nr, mu_regularization=500., plot=False, seed=0)
    np.testing.assert_allclose(x_target, x, atol=1.E-8)
    c = cons(x, jac=False)
    np.testing.assert_allclose(np.zeros_like(c), c, atol=1.E-8)
    
def test_1dsplinemodelfullfit_with_init_1000():
    ff = np.load(locate_test_datafile('test_1dsplinemodel_fullfit_with_init_solution.npz'))
    x_target = ff['x_1000']
    lc, f, model, cons, reg, p_init, x = fit_1dsplinemodel(N=1000, minimize=minimize_nr, mu_regularization=1000., plot=False, seed=0) 
    np.testing.assert_allclose(x_target, x, atol=1.E-8)
    c = cons(x, jac=False)
    np.testing.assert_allclose(np.zeros_like(c), c, atol=1.E-8)
    

    
if __name__ == "__main__":
    lc, f, cons, reg, x = fit_1dsplinemodel_same_lcs(N=1000, minimize=minimize_nr, mu_regularization=500., plot=True)
    lc, f, model, cons, reg, p_init, x = fit_1dsplinemodel(N=500, minimize=minimize_nr, mu_regularization=500., plot=True, seed=0)
    lc, f, model, cons, reg, p_init, x = fit_1dsplinemodel(N=2500, minimize=minimize_nr, mu_regularization=2500., plot=True, seed=0)    
