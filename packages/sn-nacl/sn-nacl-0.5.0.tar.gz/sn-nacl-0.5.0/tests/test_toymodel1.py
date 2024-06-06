import numpy as np
import scipy.sparse as sparse
import pandas
from matplotlib import pyplot as pl

from nacl.loglikelihood import LogLikelihood
from nacl.minimize import Minimizer
from nacl.models.toy1d import spline


def main_no_adapted_regularization(n=100, bsize=25):
    """
    """
    gen = spline.ToyDataGenerator(n=n, bsize=bsize, error_pedestal=0., delta=5.)
    d = gen.generate()
    reg = spline.Regularization(block_name='theta', mu0=1., mu2=1.)

    model = spline.Model(gen.x, gen.basis.grid)
    ll = LogLikelihood(model, reg=[reg], data=gen.get_data())
    v, grad, hess = ll(ll.pars.free, deriv=1)

    minz = Minimizer(ll)
    p_init = ll.pars.copy()
    p_init['theta'].full[:] = np.random.rand(len(p_init['theta'].full))
    minz.minimize_lm(p_init=p_init.free, lamb=1.E-6)
    spline.plot_model_and_data(minz.log_likelihood.model, minz.log_likelihood.pars, minz.log_likelihood.data)


def main_adapted_regularization(n=100, bsize=30, mu=1000., mu_model=1.E-6):
    """
    """
    gen = spline.ToyDataGenerator(n=n, bsize=bsize, error_pedestal=0., delta=5.)
    d = gen.generate()
    reg = spline.Regularization(block_name='theta', mu0=1., mu2=1.)

    model = spline.Model(gen.x, gen.basis.grid)
    ll = LogLikelihood(model, reg=[reg], data=gen.get_data())
    v, grad, hess = ll(ll.pars.free, deriv=1)

    minz = Minimizer(ll)
    p_init = ll.pars.copy()
    p_init['theta'].full[:] = np.random.rand(len(p_init['theta'].full))
    minz.minimize_lm(p_init=p_init.free, lamb=1.E-6)
    spline.plot_model_and_data(minz.log_likelihood.model, minz.log_likelihood.pars, minz.log_likelihood.data)

    _,J = model(ll.pars, jac=1)
    reg.adapt_regularization_strength(J, mu=mu, mu_model=mu_model)
    minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)
    spline.plot_model_and_data(minz.log_likelihood.model, minz.log_likelihood.pars, minz.log_likelihood.data)


def main_adapted_regularization_error_model(n=100, bsize=20,
                                            mu=1000, mu_model=1.E-6,
                                            error_pedestal=0.0075):
    """
    """
    gen = spline.ToyDataGenerator(n=n, bsize=bsize, error_pedestal=error_pedestal, delta=5.)
    d = gen.generate()
    reg = spline.Regularization(block_name='theta', mu0=2., mu2=1.)

    model = spline.Model(gen.x, gen.basis.grid)
    error_snake = spline.SimplePedestalErrorModel(model)
    ll = LogLikelihood(model, variance_model=error_snake, reg=[reg], data=gen.get_data())
    v, grad, hess = ll(ll.pars.free, deriv=1)

    minz = Minimizer(ll)
    p_init = ll.pars.copy()
    p_init['theta'].full[:] = np.random.rand(len(p_init['theta'].full))
    p_init['gamma'].full[:] = 1.
    r = minz.minimize_lm(p_init=p_init.free, lamb=1.E-6)
    print(r)
    spline.plot_model_and_data(minz.log_likelihood.model, minz.log_likelihood.pars, minz.log_likelihood.data)
    minz.plot()

    _,J = model(ll.pars, jac=1)
    reg.adapt_regularization_strength(J, mu=mu, mu_model=mu_model)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)
    spline.plot_model_and_data(minz.log_likelihood.model, minz.log_likelihood.pars, minz.log_likelihood.data, reg_lambda=reg.reg_lambda)
    print(r)
