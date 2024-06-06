import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import numpy as np
import pylab as pl
from nacl.dataset import TrainingDataset
from nacl.models.salt import SALT2Like
from nacl.models.constraints import SALT2LikeConstraints, solve_constraints
from nacl.models import constraints
from nacl.models.regularizations import NaClSplineRegularization
from nacl.models import variancemodels
from nacl import minimize
import helpers

tds, model = helpers.generate_dataset(1000, seed=42, string_ids=False,
                                      compress=False)
p_truth = model.pars.copy()


# def test_lightcurve_fit(fit=True, linesearch=False, start_from_truth=False):
#     """fit the light curves, not the model
#     """
#     # re-init model parameters
#     model.pars.full[:] = p_truth.full[:]

#     # fix everything but the SN parameters of interest
#     model.pars.fix()
#     for block_name in ['X0', 'X1', 'col', 'tmax']:
#         model.pars[block_name].release()

#     # tds_lc = TrainingDataset(tds.sn_data, tds.lc_data,
#     #                          load_filters=True)
#     # model_lc = SALT2Like(tds_lc, init_fr)

#     valid = tds.spec_data.valid.copy()
#     tds.spec_data.valid[:] = 0

#     # scramble the initial state
#     if not start_from_truth:
#         sz = len(model.pars['X0'].free)
#         model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
#         model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
#         model.pars['col'].free += np.random.normal(size=sz, scale=0.3)
#         model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

#     wres = minimize.WeightedResiduals(model)
#     chi2 = minimize.LogLikelihood(wres)
#     minz = minimize.Minimizer(chi2)
#     if fit:
#         res = minz.minimize(model.pars.free, linesearch=linesearch)
#     else:
#         res = None

#     return res, minz


def test_model_fit(start_from_truth=True, plot=True):
    """
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]
    model.init_from_training_dataset()

    if not start_from_truth:
        sz = len(model.pars['X0'].free)
        model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        model.pars['col'].free += np.random.normal(size=sz, scale=0.2)
        model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        model.pars[block_name].release()
    ll = minimize.LogLikelihood2(model, force_default_spgemm=False)
    minz = minimize.Minimizer(ll)
    res = minz.minimize_lm(model.pars.free, max_iter=1000,
                           max_attempts=40, accept=10., reject=10.,
                           lamb=1.E-6)


    res['minz'] = minz
    res['truth'] = p_truth

    if plot:
        p_rec = model.pars
        fig, axes = pl.subplots(nrows=2, ncols=2, figsize=(8,8), sharex=True)
        dp = p_rec['X0'].full - p_truth['X0'].full
        axes[0,0].plot(tds.sn_data.z, dp[tds.sn_data.sn_index],'k.')
        axes[0,0].set_title('X0')
        axes[0,0].set_ylabel('$X_0^{rec} - X_0^{true}$')

        dp = p_rec['X1'].full-p_truth['X1'].full
        axes[0,1].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[0,1].set_title('X1')
        axes[0,1].set_ylabel('$X_1^{rec} - X_1^{true}$')

        dp = p_rec['col'].full-p_truth['col'].full
        axes[1,0].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[1,0].set_title('$col$')
        axes[1,0].set_ylabel('$col^{rec} - col^{true}$')

        dp = p_rec['tmax'].full-p_truth['tmax'].full
        axes[1,1].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[1,1].set_title('$t_{max}$')
        axes[1,1].set_ylabel('$t_{max}^{rec} - t_{max}^{true}$')


    return res


def test_model_training_linear_constraints(start_from_truth=True, plot=True):
    """
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]
    model.init_from_training_dataset()

    if not start_from_truth:
        sz = len(model.pars['X0'].free)
        model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        model.pars['col'].free += np.random.normal(size=sz, scale=0.2)
        model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']:
        model.pars[block_name].release()
        
    cons = constraints.salt2like_linear_constraints(model, mu=1.E6) # was 1.E6
    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'], mu=1.) # was 1.E-6

    ll = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
                                 phot_error_pedestal=0.,
                                 force_default_spgemm=False)
    minz = minimize.Minimizer(ll)

    model.pars['X1'].full[:] -= model.pars['X1'].full.mean()
    model.pars['col'].full[:] -= model.pars['col'].full.mean()

    res = minz.minimize_lm(model.pars.free, max_iter=1000,
                           max_attempts=40, accept=10., reject=2.,
                           lamb=1.E+3, 
                           diag_charge='levenberg')

    # res = minz.minimize(model.pars.free)

    res['minz'] = minz
    res['truth'] = p_truth

    if plot:
        p_rec = model.pars
        fig, axes = pl.subplots(nrows=2, ncols=2, figsize=(8,8), sharex=True)
        dp = p_rec['X0'].full - p_truth['X0'].full
        axes[0,0].plot(tds.sn_data.z, dp[tds.sn_data.sn_index],'k.')
        axes[0,0].set_title('X0')
        axes[0,0].set_ylabel('$X_0^{rec} - X_0^{true}$')

        dp = p_rec['X1'].full-p_truth['X1'].full
        axes[0,1].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[0,1].set_title('X1')
        axes[0,1].set_ylabel('$X_1^{rec} - X_1^{true}$')

        dp = p_rec['col'].full-p_truth['col'].full
        axes[1,0].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[1,0].set_title('$col$')
        axes[1,0].set_ylabel('$col^{rec} - col^{true}$')

        dp = p_rec['tmax'].full-p_truth['tmax'].full
        axes[1,1].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[1,1].set_title('$t_{max}$')
        axes[1,1].set_ylabel('$t_{max}^{rec} - t_{max}^{true}$')


    return res


def test_model_training_linear_constraints_error_snake(tds, start_from_truth=False,
                                                       plot=True):
    """
    """
    model = SALT2Like(tds,
                      init_from_salt2_file='salt2.npz',
                      normalization_band_name='SWOPE::B',
                      error_snake_model_type=variancemodels.SimpleErrorSnake)
    model.init_from_training_dataset()
    # model.init_pars()
    # model.pars.release()
    # model.pars.full[:] = p_truth.full[:]
    # model.pars['sigma_snake'].full[:] = 0.05

    if not start_from_truth:
        sz = len(model.pars['X0'].free)
        model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        model.pars['col'].free += np.random.normal(size=sz, scale=0.2)
        model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    model.pars['X1'].full[:] -= model.pars['X1'].full.mean()
    model.pars['col'].full[:] -= model.pars['col'].full.mean()

    # first, fit the model
    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax',
                       'M0', 'M1', 'CL']:
        model.pars[block_name].release()

    cons = constraints.salt2like_linear_constraints(model, mu=1.E6)
    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'], mu=1.) # was 1.E-6

    ll = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
                                 variance_model=None, # model.error_snake_model,
                                 force_default_spgemm=False)
    minz = minimize.Minimizer(ll)

    model.pars['X1'].full[:] -= model.pars['X1'].full.mean()
    model.pars['col'].full[:] -= model.pars['col'].full.mean()
    model.pars['sigma_snake'].full[:] = 0.05
    res = minz.minimize_lm(model.pars.free, max_iter=100,
                           max_attempts=40, accept=10., reject=2.,
                           lamb=1.E+3, dchi2_stop=0.01,
                           model='supernodal',
                           diag_charge='levenberg')

    # then, fit the error model only
    model.pars.fix()
    for block_name in ['sigma_snake']:
        model.pars[block_name].release()
    model.pars['sigma_snake'].full[:] = 0.05
    ll = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
                                 variance_model=model.error_snake_model,
                                 force_default_spgemm=False)
    minz = minimize.Minimizer(ll)

    res = minz.minimize_lm(model.pars.free, max_iter=100,
                           max_attempts=40., accept=10., reject=2.,
                           lamb=1.E+3, dchi2_stop=0.01,
                           mode='supernodal',
                           diag_charge='levenberg')
    
    # finally, release all the parameters
    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax',
                       'M0', 'M1', 'CL', 
                       'sigma_snake']:
        model.pars[block_name].release()
    ll = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
                                 variance_model=model.error_snake_model,
                                 force_default_spgemm=False)
    minz = minimize.Minimizer(ll)
    res = minz.minimize_lm(model.pars.free, max_iter=100,
                           max_attempts=40., accept=10., reject=2.,
                           lamb=1.E+3, dchi2_stop=0.01,
                           mode='supernodal',
                           diag_charge='levenberg')
    res['minz'] = minz
    res['truth'] = p_truth

    if plot:
        p_rec = model.pars
        fig, axes = pl.subplots(nrows=2, ncols=2, figsize=(8,8), sharex=True)
        dp = p_rec['X0'].full - p_truth['X0'].full
        axes[0,0].plot(tds.sn_data.z, dp[tds.sn_data.sn_index],'k.')
        axes[0,0].set_title('X0')
        axes[0,0].set_ylabel('$X_0^{rec} - X_0^{true}$')

        dp = p_rec['X1'].full-p_truth['X1'].full
        axes[0,1].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[0,1].set_title('X1')
        axes[0,1].set_ylabel('$X_1^{rec} - X_1^{true}$')

        dp = p_rec['col'].full-p_truth['col'].full
        axes[1,0].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[1,0].set_title('$col$')
        axes[1,0].set_ylabel('$col^{rec} - col^{true}$')

        dp = p_rec['tmax'].full-p_truth['tmax'].full
        axes[1,1].plot(tds.sn_data.z, dp[tds.sn_data.sn_index], 'k.')
        axes[1,1].set_title('$t_{max}$')
        axes[1,1].set_ylabel('$t_{max}^{rec} - t_{max}^{true}$')


    return res






#     # nphot = len(tds.lc_data.flux)
#     # noise = np.random.normal(scale=np.abs(0.05 * tds.lc_data.flux), size=nphot)
#     # tds.lc_data.flux += noise

#     # we start with a simple light curve fit
#     # to do this, we extract just the light curves
#     # from the training dataset
#     lc_tds = TrainingDataset(sne=tds.sn_data.nt, lc_data=tds.lc_data.nt)
#     lc_model = SALT2Like(lc_tds, init_from_salt2_file='salt2.npz')
#     lc_model.init_from_training_dataset()

#     # scramble the initial parameters
#     if not start_from_truth:
#         sz = len(lc_model.pars['X0'].free)
#         lc_model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
#         lc_model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
#         lc_model.pars['col'].free += np.random.normal(size=sz, scale=0.3)
#         lc_model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

#     lc_model.pars.fix()
#     lc_model.pars['sigma_snake'].full[:] = 0.1
#     for block_name in ['X0', 'X1', 'col', 'tmax']:  # 'sigma_snake']:
#         lc_model.pars[block_name].release()
#     chi2 = minimize.LogLikelihood2(lc_model,
#                                    # variance_model=lc_model.error_snake,
#                                    force_default_spgemm=False)
#     minz = minimize.Minimizer(chi2)
#     res = minz.minimize(lc_model.pars.free)  # , mode='simplicial', beta=1.E-6)

#     # and initialize the full model with the results of the light curve fit
#     for block_name in ['X0', 'X1', 'col', 'tmax']:
#         model.pars[block_name].full[:] = lc_model.pars[block_name].full[:]
#     # then, release the other parameters and start the real fit
#     model.pars['sigma_snake'] = 0.05
#     model.pars.fix()
#     model.pars['sigma_snake'].full[:] = 0.05
#     for block_name in ['X0', 'X1', 'col', 'tmax',
#                        'M0', 'M1', 'CL',
#                        'sigma_snake'
#                        # 'SpectrumRecalibration'
#                        ]:
#         model.pars[block_name].release()
#         # nrecal = len(model.pars['SpectrumRecalibration'].full)
#         # model.pars['SpectrumRecalibration'].full[:] += np.random.uniform(-1.E-6, 1.E-6, size=nrecal)

#     # at first order, make sure that the constraints are respected
#     # model.pars['X1'].full -= model.pars['X1'].full.mean()
#     # model.pars['X1'].full /= model.pars['X1'].full.std()
#     # model.pars['col'].full -= model.pars['col'].full.mean()
#     cons = SALT2LikeConstraints(model,
#                                 active={'M0': 10**(-0.4 * (30-19.5)),
#                                         'dM0': 0.,
#                                         'M1': 0.,
#                                         'dM1': 0.,
#                                         'col': 0.,
#                                         'X1': 0.,
#                                         'X1_var': 1.}, mu=1.E6)
#     reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
#                                    order=0, mu=1.)
#     chi2 = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
#                                    force_default_spgemm=False,
#                                    variance_model=model.error_snake
#                                    )
#     minz = minimize.Minimizer(chi2)
#     # dx = solve_constraints(cons, model.pars)
#     # model.pars.free += dx
#     # model.pars['X1'].full /= model.pars['X1'].full.std()
#     # print('cons=', cons(model.pars.free))
#     res = minz.minimize(model.pars.free)

#     res['lc_model'] = lc_model
#     res['model'] = model
#     res['cons'] = cons
#     res['reg'] = reg
#     res['chi2'] = chi2

#     return res





def test_model_fit_no_constraints():
    """Simple model fit, some regularization, no constraints,
    just fixing a couple of SNe to break the degeneracies.
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]

    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']:
        model.pars[block_name].release()
    for sn in [0,1,2,3]:
        model.pars['X0'].fix(sn)
        model.pars['X1'].fix(sn)
        model.pars['col'].fix(sn)
        model.pars['tmax'].fix(sn)

    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
                                   order=1, mu=1.E-0)
    wres = minimize.WeightedResiduals(model)
    chi2 = minimize.LogLikelihood(wres, reg=[reg])
    minz = minimize.Minimizer(chi2)
    res = minz(model.pars.free, linesearch=False)

    # res['cons'] = cons
    res['reg'] = reg
    res['chi2'] = chi2

    return res


def test_training_before_after(start_from_truth=False):
    """
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]

    flux = tds.spec_data.flux
    fluxerr = tds.spec_data.fluxerr
    tds.spec_data.fluxerr[:] = np.sqrt(fluxerr**2 + 0.1**2 * flux**2)

    # we may want to scramble the initial parameters
    if not start_from_truth:
        sz = len(model.pars['X0'].free)
        model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        model.pars['col'].free += np.random.normal(size=sz, scale=0.3)
        model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    # first, we fit the X0,X1,c,tmax only
    # (on the full dataset)
    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        model.pars[block_name].release()
    chi2 = minimize.LogLikelihood2(model, force_default_spgemm=False)
    minz = minimize.Minimizer(chi2)
    p = minz.minimize(model.pars.free)
    p_fit1 = p.copy()
    print('chi2 after fit1: ', chi2(p_fit1['pars'].free))

    # then, we fit the full model
    for block_name in ['X0', 'X1', 'col', 'tmax', 'M0', 'CL']:
        model.pars[block_name].release()
    cons = SALT2LikeConstraints(model,
                                active={'M0': 10**(-0.4 * (30-19.5)),
                                        'dM0': 0.,
                                        'M1': 0.,
                                        'dM1': 0.,
                                        'col': 0.,
                                        'X1': 0.,
                                        'X1_var': 1.}, mu=1.)
    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
                                   order=0, mu=1.E-6)
    chi2 = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
                                   force_default_spgemm=False,
                                   )
    print('chi2 before fit2: ', chi2(model.pars.free))

    minz = minimize.Minimizer(chi2)
    p = minz.minimize(model.pars.free)
    p_fit2 = p.copy()
    print('chi2 after fit2: ', chi2(p_fit2['pars'].free))

    ret = {}
    ret['model'] = model
    ret['p_fit1'] = p_fit1
    ret['p_fit2'] = p_fit2

    return ret


def test_training_fit_new_likelihood(start_from_truth=True):
    """
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]
    model.init_from_training_dataset()

    # nphot = len(tds.lc_data.flux)
    # noise = np.random.normal(scale=np.abs(0.05 * tds.lc_data.flux), size=nphot)
    # tds.lc_data.flux += noise

    # we start with a simple light curve fit
    # to do this, we extract just the light curves
    # from the training dataset
    lc_tds = TrainingDataset(sne=tds.sn_data.nt, lc_data=tds.lc_data.nt)
    lc_model = SALT2Like(lc_tds, init_from_salt2_file='salt2.npz')
    lc_model.init_from_training_dataset()

    # scramble the initial parameters
    if not start_from_truth:
        sz = len(lc_model.pars['X0'].free)
        lc_model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        lc_model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        lc_model.pars['col'].free += np.random.normal(size=sz, scale=0.3)
        lc_model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    lc_model.pars.fix()
    lc_model.pars['sigma_snake'].full[:] = 0.1
    for block_name in ['X0', 'X1', 'col', 'tmax']:  # 'sigma_snake']:
        lc_model.pars[block_name].release()
    chi2 = minimize.LogLikelihood2(lc_model,
                                   # variance_model=lc_model.error_snake,
                                   force_default_spgemm=False)
    minz = minimize.Minimizer(chi2)
    res = minz.minimize(lc_model.pars.free)  # , mode='simplicial', beta=1.E-6)

    # and initialize the full model with the results of the light curve fit
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        model.pars[block_name].full[:] = lc_model.pars[block_name].full[:]
    # then, release the other parameters and start the real fit
    model.pars['sigma_snake'] = 0.05
    model.pars.fix()
    model.pars['sigma_snake'].full[:] = 0.05
    for block_name in ['X0', 'X1', 'col', 'tmax',
                       'M0', 'M1', 'CL',
                       'sigma_snake'
                       # 'SpectrumRecalibration'
                       ]:
        model.pars[block_name].release()
        # nrecal = len(model.pars['SpectrumRecalibration'].full)
        # model.pars['SpectrumRecalibration'].full[:] += np.random.uniform(-1.E-6, 1.E-6, size=nrecal)

    # at first order, make sure that the constraints are respected
    # model.pars['X1'].full -= model.pars['X1'].full.mean()
    # model.pars['X1'].full /= model.pars['X1'].full.std()
    # model.pars['col'].full -= model.pars['col'].full.mean()
    cons = SALT2LikeConstraints(model,
                                active={'M0': 10**(-0.4 * (30-19.5)),
                                        'dM0': 0.,
                                        'M1': 0.,
                                        'dM1': 0.,
                                        'col': 0.,
                                        'X1': 0.,
                                        'X1_var': 1.}, mu=1.E6)
    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
                                   order=0, mu=1.)
    chi2 = minimize.LogLikelihood2(model, reg=[reg], cons=[cons],
                                   force_default_spgemm=False,
                                   variance_model=model.error_snake
                                   )
    minz = minimize.Minimizer(chi2)
    # dx = solve_constraints(cons, model.pars)
    # model.pars.free += dx
    # model.pars['X1'].full /= model.pars['X1'].full.std()
    # print('cons=', cons(model.pars.free))
    res = minz.minimize(model.pars.free)

    res['lc_model'] = lc_model
    res['model'] = model
    res['cons'] = cons
    res['reg'] = reg
    res['chi2'] = chi2

    return res




def test_training_fit(start_from_truth=True):
    """fit the light curves and a block of the model
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]

    # we start with a simple light curve fit
    # to do this, we extract just the light curves
    # from the training dataset
    lc_tds = TrainingDataset(sne=tds.sn_data.nt, lc_data=tds.lc_data.nt)
    lc_model = SALT2Like(lc_tds, init_from_salt2_file='salt2.npz')
    lc_model.init_from_training_dataset()

    # scramble the initial parameters
    if not start_from_truth:
        sz = len(lc_model.pars['X0'].free)
        lc_model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        lc_model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        lc_model.pars['col'].free += np.random.normal(size=sz, scale=0.3)
        lc_model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    lc_model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        lc_model.pars[block_name].release()
    wres = minimize.WeightedResiduals(lc_model)
    chi2 = minimize.LogLikelihood(wres)
    minz = minimize.Minimizer(chi2)
    res = minz.minimize(lc_model.pars.free)

    # and initialize the full model with the results of the light curve fit
    for block_name in ['X0', 'X1', 'col', 'tmax']:
        model.pars[block_name].full[:] = lc_model.pars[block_name].full[:]
    # then, release the other parameters and start the real fit
    model.pars.fix()
    for block_name in ['X0', 'X1', 'col', 'tmax',
                       'M0', 'M1', 'CL']:  # 'SpectrumRecalibration']:
        model.pars[block_name].release()

    # at first order, make sure that the constraints are respected
    model.pars['X1'].full -= model.pars['X1'].full.mean()
    model.pars['X1'].full /= model.pars['X1'].full.std()
    model.pars['col'].full -= model.pars['col'].full.mean()
    cons = SALT2LikeConstraints(model,
                                active={'M0': 10**(-0.4 * (30-19.5)),
                                        'dM0': 0.,
                                        'M1': 0.,
                                        'dM1': 0.,
                                        'col': 0.,
                                        'X1': 0.,
                                        'X1_var': 1.}, mu=1.E6)
    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
                                   order=0, mu=1.)
    wres = minimize.WeightedResiduals(model)
    chi2 = minimize.LogLikelihood(wres, reg=[reg], cons=[cons])
    minz = minimize.Minimizer(chi2)
    res = minz.minimize(model.pars.free)

    res['cons'] = cons
    res['reg'] = reg
    res['chi2'] = chi2

    return res


def test_cons_dM0():
    cons = SALT2LikeConstraints(model,
                                active={'dM0': 0.},
                                mu=1.)
    pp = model.pars.copy()

    l = []
    for dx in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]:
        M0 = pp['M0'].full.copy()
        M0 = np.roll(M0.reshape(-1, 129), dx, axis=0)
        model.pars['M0'].full[:] = M0.ravel()
        l.append((dx, float(cons.Jac @ model.pars.full)))
    l = np.rec.fromrecords(l, names=['dx', 'cons'])
    return l

def test_likelihood_derivatives(start_from_truth=False):
    """
    """
    model.pars.release()
    model.pars.full[:] = p_truth.full[:]

    if not start_from_truth:
        sz = len(model.pars['X0'].free)
        model.pars['X0'].free *= np.random.normal(size=sz, loc=1., scale=0.1)
        model.pars['X1'].free += np.random.normal(size=sz, scale=1.)
        model.pars['col'].free += np.random.normal(size=sz, scale=0.3)
        model.pars['tmax'].free += np.random.normal(size=sz, scale=1.)

    # fix everything but the SN parameters of interest
    # plus one block
    model.pars.fix()
    for block_name in ['X0', 'M0', 'X1', 'col', 'tmax']:
        model.pars[block_name].release()

    model.pars['X1'].full -= model.pars['X1'].full.mean()
    model.pars['X1'].full /= model.pars['X1'].full.std()
    model.pars['col'].full -= model.pars['col'].full.mean()

    cons = SALT2LikeConstraints(model,
                                active={'M0': 10**(-0.4 * (30-19.5)),
                                        'dM0': 0.,
                                        'M1': 0.,
                                        'dM1': 0.,
                                        'col': 0.,
                                        'X1': 0.,
                                        'X1_var': 1.
                                               },
                                mu=1.E6)
    # return cons
    reg = NaClSplineRegularization(model, to_regularize=['M0', 'M1'],
                                   order=0, mu=1.e-6)
    wres = minimize.WeightedResiduals(model)
    chi2 = minimize.LogLikelihood(wres)  # , reg=[reg], cons=[cons])

    Ja, Jn = helpers.check_deriv(chi2, p=model.pars.free)

    return Ja, Jn


