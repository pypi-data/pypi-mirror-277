import numpy as np
import scipy.sparse as sparse
import pandas
from matplotlib import pyplot as pl

from nacl.loglikelihood import LogLikelihood
from nacl.minimize import Minimizer
from nacl.models.toy2d import spline
from scipy.sparse import coo_matrix, dia_matrix, csc_matrix, dok_matrix
from sksparse import cholmod


def main_no_adapted_regularization_2D(n0=50, n1=50, b0_size=25, b1_size=25):
    """
    """
    gen = spline.ToyDataGenerator(n0=n0, n1=n1, b0_size=b0_size, b1_size=b1_size, error_pedestal=0., delta=5.)
    d = gen.generate()
    reg = spline.Regularization(block_name='theta', mu0=1., mu2=1.)

    model = spline.Model(gen.x0, gen.x1, gen.basis.bx.grid, gen.basis.by.grid, order=4)
    ll = LogLikelihood(model, reg=[reg], data=gen.get_data())
    #ll = LogLikelihood(model, reg=None, data=gen.get_data())
    v, grad, hess = ll(ll.pars.free, deriv=1)

    minz = Minimizer(ll)
    p_init = ll.pars.copy()
    p_init['theta'].full[:] = np.random.rand(len(p_init['theta'].full))
    minz.minimize_lm(p_init=p_init.free, lamb=1.E-6)
    spline.plot_model_and_data(minz.log_likelihood.model, minz.log_likelihood.pars, minz.log_likelihood.data)

def hand_made_fit(n0=50, n1=50, b0_size=25, b1_size=25):
    """
    Adding this to see if I can get insight on where the fitting problem is
    """
    gen = spline.ToyDataGenerator(n0=n0, n1=n1, b0_size=b0_size, b1_size=b1_size, error_pedestal=0., delta=5.)
    d = gen.generate()
    data = gen.get_data()

    def fit(x0, x1, basis, y, yerr):
        """a fit of the data -- the simplest possible
        """
        J = basis.eval(np.array(x0), np.array(x1))
        w = 1. / yerr**2
        W = dia_matrix((w, [0]), shape=(len(y), len(y)))
        H = J.T @ W @ J
        B = J.T @ W @ y
        fact = cholmod.cholesky(H, beta=1.E-6)
        theta = fact(B)

        resid = y-J @ theta
        return resid, theta
        
    r, t = fit(data.xx0, data.xx1, gen.basis, data.y, data.yerr)
    
    return r
    
    
