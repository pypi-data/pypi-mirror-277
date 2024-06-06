"""
"""

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import numpy as np
import scipy.sparse as sparse
from scipy.sparse import coo_matrix, dia_matrix, csc_matrix, dok_matrix
import scipy.sparse as sparse
import pandas

import pylab as pl
from matplotlib.gridspec import GridSpec

from nacl.minimize import Minimizer, LogLikelihood2

from sksparse import cholmod

from nacl.lib import bspline
from nacl.lib.fitparameters import FitParameters
from nacl.loglikelihood import LogLikelihood

from matplotlib import cm

def gaussian(x, a, sigma):
    """
    Gaussian function *2
    """
    norm = a / (np.sqrt(2. * np.pi) * sigma)
    xx = x / sigma
    return norm * np.exp(-0.5 * xx**2)

def gaussian_2d(x, y, a, sigma):
    """
    Gaussian function *2
    """
    norm = a / (np.sqrt(2. * np.pi) * sigma)
    xx = x / sigma
    yy = y / sigma
    return norm * np.exp(-0.5 * (xx**2 + yy**2))

def gen_data(xmin=-10., xmax=10., n=100, ):
    """
    Generates random data that follows a gaussian with noise
    """
    x = np.random.uniform(xmin, xmax, size=n)  #coordonnées
    err = np.linspace(0.1, 0.1, 20)
    noise = np.random.uniform(low=0.5, high=0.5, size=20)
    return x, err, gaussian(x) + noise


class ToyDataGenGenerator:

    def __init__(self, xmin=-10., xmax=10., yerr=0.01, a=1., sigma=3.,
                 n=100, delta=2., bsize=10, order=4):
        self.xmin, self.xmax = xmin, xmax
        self.yerr = yerr
        self.a, self.sigma = a, sigma
        self.n = n
        self.delta = delta
        self.basis = bspline.BSpline(np.linspace(xmin-delta, xmax+delta, bsize), order=order)

    def generate(self):
        """
        generate a realization of a dataset
        """
        x = np.random.uniform(self.xmin, self.xmax, size=self.n)
        y = gaussian(x, self.a, self.sigma)
        yerr = np.full(self.n, self.yerr)
        noise = np.random.normal(loc=0., scale=yerr)
        self.x, self.y_true, self.yerr, self.noise = x, y, yerr, noise
        self.y = self.y_true + self.noise
        return self.x, self.y + self.noise, self.yerr

    def get_data(self):
        if not hasattr(self, 'x'):
            self.generate()
        dd = pandas.DataFrame({'xx': self.x,
                               'y': self.y,
                               'yerr': self.yerr,
                               'bads': np.zeros(len(self.yerr)).astype(bool),
                               })
        return dd

    def fit(self, beta=1.E-6):
        """a fit of the data -- the simplest possible
        """
        J = self.basis.eval(self.x)
        w = 1. / self.yerr**2
        W = dia_matrix((w, [0]), shape=(self.n, self.n))
        H = J.T @ W @ J
        B = J.T @ W @ self.y
        fact = cholmod.cholesky(H, beta=beta)
        self.theta = fact(B)
    
    def plot(self, color='b', marker='.'):
        """plot the data and the model
        """
        fig = pl.figure()
        gs = GridSpec(2, 1, height_ratios=[4,2])

        ax1 = fig.add_subplot(gs[0])
        ax1.errorbar(self.x, self.y, yerr=self.yerr, ls='', color=color, marker=marker, label='data', zorder=0.5)
        ax1.set_ylabel('model \& data')
        ax2 = fig.add_subplot(gs[1], sharex=ax1)
        ax2.set_xlabel('x')
        ax2.set_ylabel('residuals')

        # pl.grid(ls=':')
        # pl.plot(self.basis.grid, np.zeros(len(self.basis.grid)), 'k|')
        if hasattr(self, 'theta'):
            xx = self.basis._grid.copy()
            JJ = self.basis.eval(xx)
            ax1.plot(xx, JJ@self.theta, ls='', color='red', marker='.', alpha=1., label='nodes', zorder=10., linewidth=2)

            xx = np.linspace(self.xmin-self.delta, self.xmax+self.delta, 200)
            JJ = self.basis.eval(xx)
            ax1.plot(xx, JJ@self.theta, 'r-', label='model', zorder=2.)

            JJ = self.basis.eval(self.x)
            ax2.errorbar(self.x, self.y-JJ @ self.theta, yerr=self.yerr, ls='', marker='.', color='k')

        pl.legend(loc='best')

class ToyDataGenGenerator2D:

    def __init__(self, x0_min=-10., x0_max=10., x1_min=-10., x1_max=10., yerr=0.01, a=1., sigma=3., n0=30, n1=30, delta=2., b0_size=10, b1_size=10, mu_0=0., mu_1=0., mu_max=0.):
        self.x0_min, self.x0_max = x0_min, x0_max
        self.x1_min, self.x1_max = x1_min, x1_max
        self.yerr = yerr
        self.a, self.sigma = a, sigma
        self.n0 = n0
        self.n1 = n1
        self.delta = delta
        self.basis = bspline.BSpline2D(np.linspace(x0_min-delta, x0_max+delta, b0_size), np.linspace(x1_min-delta, x1_max+delta, b1_size), x_order=4, y_order=4)
        self.mu = mu_max
        self.mu_0 = mu_0
        self.mu_1 = mu_1
        self.b0 = b0_size
        self.b1 = b1_size

    def generate(self):
        """
        generate a realization of a dataset
        """
        x0 = np.random.uniform(self.x0_min, self.x0_max, size=self.n0)
        x1 = np.random.uniform(self.x1_min, self.x1_max, size=self.n1)
        X0, X1 = np.meshgrid(x0, x1)
        X0 = X0.ravel()
        X1 = X1.ravel()
        n = len(X0)
        self.n = n
        yerr = np.full(self.n, self.yerr)
        y = gaussian_2d(X0, X1, self.a, self.sigma)
        noise = np.random.uniform(low = -self.yerr, high = self.yerr, size = n)
        self.x0, self.x1, self.y_true, self.noise, self.yerr = x0, x1, y, noise, yerr
        self.y = self.y_true + self.noise
        return self.x0, self.x1, self.y + self.noise, self.yerr
        
    def get_data(self):
        if not hasattr(self, 'x'):
            self.generate()
        X0, X1 = np.meshgrid(self.x0, self.x1)
        dd = pandas.DataFrame({'xx0': X0.ravel(),
                               'xx1': X1.ravel(),
                               'y': self.y,
                               'yerr': self.yerr,
                               'bads': np.zeros(len(self.yerr)).astype(bool),
                               })
        return dd
    
    def adapt_reg_matrix(self):
        """
        adding adapted regularization to test different methods
        """
        X0, X1 = np.meshgrid(self.x0, self.x1)
        J = self.basis.eval(X0.ravel(), X1.ravel())
        J = J.toarray()
        D = self.basis.hessian(x=X0.ravel(), y=X1.ravel())
        D = D[0] + D[1] + D[2]
        D.toarray()
        
        s_j =  np.sum(J, axis=0)
        s_j_tilde = np.sum(D, axis=0)
        s_j_tilde = np.array(s_j_tilde)[0]
        
        mu = np.ones(len(J[0])) * self.mu
        idx = s_j_tilde!=0
        #idx = np.array(idx)[0]
        int_mj = (mu - s_j)
        int_mj[idx] = int_mj[idx]/s_j_tilde[idx]
        #print(int_mj[idx])
        zeros = np.zeros(len(mu))
        
        mu_j = np.max([int_mj, zeros] , axis=0)
        
        M = dia_matrix((mu_j, [0]), shape=(len(mu), len(mu))).tocoo()
        return M
        
    def reg_matrix(self):
        """
        adding regularization
        """
        X0, X1 = np.meshgrid(self.x0, self.x1)
        J = self.basis.eval(X0.ravel(), X1.ravel())
        J = J.toarray()
        
        m_0 = np.ones(len(J[0])) * self.mu_0
        M_0 = dia_matrix( (m_0, [0]), shape=( len(m_0), len(m_0) ) ).tocoo()  #order 0
        
        m_1 = np.vstack( ([2.] * len(m_0), [-1.] * len(m_0), [-1.] * len(m_0), [-1.] * len(m_0), [-1.] * len(m_0)) )
        m_1[0, 0] = m_1[0, -1] = 3.
        M_1 = dia_matrix((m_1, [0, -1, 1, self.n0, -self.n0]), shape=(len(m_0),len(m_0))).tocoo()
        M_1 *= self.mu_1
        return M_0, M_1
    
    def fit(self):
        """a fit of the data -- the simplest possible
        """
        if self.mu == 0.:
            X0, X1 = np.meshgrid(self.x0, self.x1)
            J = self.basis.eval(X0.ravel(), X1.ravel())
            M0, M1 = self.reg_matrix()
            w = 1. / self.yerr**2
            W = dia_matrix((w, [0]), shape=(self.n, self.n))
            H = J.T @ W @ J + M0.T @ M0 + M1.T @ M1
            #H = J.T @ W @ J
            B = J.T @ W @ self.y
            fact = cholmod.cholesky(H, beta=1.E-6)
            self.theta = fact(B)
        else : 
            X0, X1 = np.meshgrid(self.x0, self.x1)
            J = self.basis.eval(X0.ravel(), X1.ravel())
            M = self.adapt_reg_matrix()
            D = self.basis.hessian(x=X0.ravel(), y=X1.ravel())
            D = D[0] + D[1] + D[2]
            w = 1. / self.yerr**2
            W = dia_matrix((w, [0]), shape=(self.n0, self.n0))
            H = J.T @ W @ J + (D @ M).T @ (D @ M)
            B = J.T @ W @ self.y
            fact = cholmod.cholesky(H, beta=1.E-6)
            self.theta = fact(B)
        resid = self.y-J @ self.theta
        errs = self.yerr
        return resid, errs
    
    def plot(self, color='b', marker='.'):
        """plot the data and the model
        """
        mu = self.mu
        fig = pl.figure()
        gs = GridSpec(2, 1, height_ratios=[7,2])

        ax1 = fig.add_subplot(gs[0], projection='3d')
        #ax1.errorbar(self.x, self.y, yerr=self.yerr, ls='', color=color, marker=marker, label='data', zorder=0.5)
        ax1.set_zlabel('model & data')
        ax1.set_xlabel('x0')
        ax1.set_ylabel('x1')
        ax2 = fig.add_subplot(gs[1], sharex=ax1)
        ax2.set_xlabel('x')
        ax2.set_ylabel('residuals')
        
        X0, X1 = np.meshgrid(self.x0, self.x1)
        ax1.errorbar(X0.ravel(), X1.ravel(), self.y, zerr = self.yerr, ecolor=('black',0.1), ls='', marker='.', color='blue')
        if self.mu ==0.:
            ax1.set_title('µ0 = ' +  str(self.mu_0) + ' , µ1 = ' + str(self.mu_1))
        else : 
            ax1.set_title('µ max = ' + str(self.mu))
            

        # pl.grid(ls=':')
        # pl.plot(self.basis.grid, np.zeros(len(self.basis.grid)), 'k|')
        
        resid = []
        errs = []
        if hasattr(self, 'theta'):
            #xx = self.basis._grid.copy()
            xx = self.basis.bx.grid
            yy = self.basis.by.grid
            XX, YY = np.meshgrid(xx, yy)
            JJ = self.basis.eval(XX.ravel(), YY.ravel())
            #ax1.plot(xx, yy, JJ@self.theta, ls='', color='red', marker='.', alpha=1., label='nodes', zorder=10., linewidth=2)
            fitting = JJ@self.theta
            fitting = np.reshape(fitting, (self.b0, self.b1))
            ax1.plot_surface(XX, YY, fitting, cmap=cm.coolwarm, label='nodes')

            #xx = np.linspace(self.x0_min-self.delta, self.x0_max+self.delta, 200)
            #JJ = self.basis.eval(xx)
            #ax1.plot(xx, JJ@self.theta, 'r-', label='model', zorder=2.)

            JJ = self.basis.eval(X0.ravel(), X1.ravel())
            x = np.linspace(self.x0_min, self.x0_max, len(X0.ravel()))
            ax2.errorbar(x, self.y-JJ @ self.theta, yerr=self.yerr, ls='', marker='.', color='k')
            
            residuals_data = self.y-JJ @ self.theta
            pl.figure()
            pl.hexbin(X0.ravel(), X1.ravel(), residuals_data/self.yerr, gridsize=15)
            pl.colorbar()
            pl.title('Weighted Residuals')
            
        pl.legend(loc='best')

def main_hand_made_fit(bsize=20, n=100, beta=1., order=4):
    gen = ToyDataGenGenerator(bsize=bsize, n=n, order=order)
    r = gen.generate()
    gen.fit()
    gen.plot()

def main_hand_made_fit_2D(bsize=20, mu_max=0., mu_0=50., mu_1=50., plot=True, n0=30, n1=30):
    gen = ToyDataGenGenerator2D(b0_size=bsize, b1_size=bsize, n0=n0, n1=n1, mu_max=mu_max, mu_0=mu_0, mu_1=mu_1)
    r = gen.generate()
    resid, err = gen.fit()
    if plot:
        gen.plot()
    return resid, err

def check_grad(model, p):
    """
    """
    v,jacobian = model(p, jac=True)
    dx = 1.E-7
    pars = model.pars.copy()
    pars.free = p
    df = []
    for i in range(len(pars.full)):
        k = pars.indexof(i)
        if k < 0:
            continue
        pars.full[i] += dx
        vp = model(pars.free, jac=False)
        df.append((vp-v)/dx)
        pars.full[i] -= dx
    return np.array(jacobian.todense()), np.vstack(df).T


def check_deriv(pen, p, dx=1.E-6):
    """
    """
    v, grad, hess = pen(p=p, deriv=True)
    p0 = p.copy()

    df, d2f = [], []
    for i in range(len(p0)):
        p0[i] += dx
        vp = pen(p0, deriv=False)
        p0[i] -= (2*dx)
        vm = pen(p0, deriv=False)
        df.append((vp-vm)/(2*dx))
        p0[i] += dx
    return np.array(grad), np.vstack(df).T


class Model:
    """A spline description of the data

    Encpsulating the sline evaluation in a model, like that
    allows to easily fix parameters, use the nacl minimizer,
    with regularization penalties.
    """
    def __init__(self, x, grid=None, order=4):
        self.x = x
        self.grid = grid
        self.basis = bspline.BSpline(grid, order=4)
        self.J = self.basis.eval(self.x)
        self.pars = FitParameters([('theta', len(self.basis))])

    def __call__(self, p=None, jac=False):
        if p is not None:
            self.pars.free = p

        vals = self.J @ self.pars['theta'].full
        if not jac:
            return vals

        j = self.pars.indexof(self.J.col)
        idx = j>=0

        N = self.J.shape[0]
        n_free_pars = len(self.pars.free)
        JJ = coo_matrix((self.J.data[idx], (self.J.row[idx], j[idx])), shape=(N,n_free_pars))
        return vals, JJ

class Model_2D:
    """A spline description of the data in 2D

    Encpsulating the sline evaluation in a 2D model, like that
    allows to easily fix parameters, use the nacl minimizer,
    with regularization penalties.
    """
    def __init__(self, x0, x1, grid_x0=None, grid_x1=None, order=4):
        self.x0 = x0
        self.x1 = x1
        self.grid_x0 = grid_x0
        self.grid_x1 = grid_x1
        self.basis = bspline.BSpline2D(grid_x0, grid_x1, x_order=order, y_order=order)
        X0, X1 = np.meshgrid(x0, x1)
        self.J = self.basis.eval(X0.ravel(), X1.ravel())
        self.pars = FitParameters([('theta', len(self.basis))])

    def __call__(self, p=None, jac=False):
        if p is not None:
            self.pars.free = p

        vals = self.J @ self.pars['theta'].full
        if not jac:
            return vals

        j = self.pars.indexof(self.J.col)
        idx = j>=0

        N = self.J.shape[0]
        n_free_pars = len(self.pars.free)
        JJ = coo_matrix((self.J.data[idx], (self.J.row[idx], j[idx])), shape=(N,n_free_pars))
        return vals, JJ


class Regularization:
    """Regularization penalty

    TODO: it would be a good idea if the adaptive regularization was performed
    here. Or at least if there was a method to do it on the fly here.
    """
    def __init__(self, pars, block_name='theta', mu0=1.E-6, mu1=1.E-3):
        """
        """
        # should be a direct handle to the parameters
        # otherwise, if we decide to fix the model,
        # this will not be propagated
        self.pars = pars   # .copy()

        self.block_name = block_name
        self.mu0 = mu0
        self.mu1 = mu1
        self.npars = len(self.pars.full)
        self.matrix = self.init_reg_matrix()

    def init_reg_matrix(self):
        """
        """
        pars_full = self.pars.copy()
        pars_full.release()

        n = len(pars_full[self.block_name].full)
        N = len(pars_full.full)

        # order 0
        P = dia_matrix((np.ones(N), [0]), shape=(n, n)).tocoo()
        i = pars_full.indexof(P.row)
        j = pars_full.indexof(P.col)
        P = coo_matrix((P.data, (i,j)), shape=(N,N))

        # order 1
        # data = -np.ones((N,3))
        # data[:,2] = data[:,0] = 1.
        # data[1:-1,1] = -2.
        #
        # second order penality, from the laplacian matrix and slightly hacked
        # to make the end of the diagonal similar to the beginning
        data = np.ones((n,3))
        data[:,1] = -2
        Q = dia_matrix((data.T, [0,1,2]), shape=[n,n]).tocoo()
        # print(Q.todense())
        i = pars_full.indexof(Q.row)
        j = pars_full.indexof(Q.col)
        Q = coo_matrix((Q.data, (i,j)), shape=(N,N))
        A = Q.T @ Q
        B = A[:3,:3]
        A[-3:,-3:] = B[::-1,::-1]

        return self.mu0 * P + self.mu1 * A

    def ndof(self):
        return -len(self.pars.free)

    def get_log(self):
        return {}

    def __call__(self, p=None, deriv=False):
        """
        """
        if p is not None:
            self.pars.free = p

        pp = self.pars.full
        penalty = pp.T @ self.matrix @ pp

        if not deriv:
            return penalty

        n = self.matrix.shape[0]
        idx = self.pars.indexof(np.arange(n)) >= 0

        grad = 2. * (self.matrix @ pp)[idx]
        hess = 2. * self.matrix[:,idx][idx,:]

        return penalty, grad, hess


class SimplePedestalErrorModel:
    """Error snake variance

    A simple model: just a constant pedestal error added to the data
    """
    def __init__(self, model):
        """constructor
        """
        self.model = model

    def get_struct(self):
        """structure of the error model specific parameters
        """
        return [("gamma", 1)]

    def __call__(self, pars, jac=False):
        """
        """
        v, J = None, None
        if jac:
            v, J = self.model(pars, jac=True)
        else:
            v = self.model(pars, jac=False)
        g = pars['gamma'].full[0]

        var = g**2

        if not jac:
            return var

        N = len(v)
        n_free_pars = len(pars.free)
        dvar = np.full(2. * g)
        i = np.arange(N)
        j = pars['gamma'].indexof(np.zeros(N))
        idx = j>=0
        J = coo_matrix((dvar[idx], (i[idx], j[idx])), shape=(N,n_free_pars))

        return var, J


class ConstantErrorSnake:
    """Simplistic Error snake

    This model is slightly more complicated: the variance depends on the model value:

    ..math::
        \sigma = \gamma \times f(\lambda,p)
    """
    def __init__(self, model):
        pass

    def get_struct(self):
        return [('gamma', 1)]

    def __call__(self, p, jac=False):
        pass


class VariableErrorSnake:
    """Realistic Error Snake

    This model is even more complicated: the variance depends on the model value
    and varies as a function of math:`$x$`

    """
    def __init__(self, model, basis=None):
        pass

    def get_struct(self):
        pass

    def __call__(self, p, jac=False):
        pass



class CalibErrorModel:

    def __init__(self):
        pass

    def __call__(self, p, jac=False):
        pass


def plot_model_and_data(model, data, title='', reg_lambda=None):
    fig = pl.figure()
    gs = GridSpec(3, 1, height_ratios=[4,2,2])

    ax1 = fig.add_subplot(gs[0])
    ax1.errorbar(data.xx, data.y, yerr=data.yerr, ls='', marker='.')
    xx = np.linspace(model.basis.grid.min(), model.basis.grid.max(), 200)
    J = model.basis.eval(xx)
    ax1.plot(xx, J @ model.pars['theta'].full, 'r-', zorder=10)
    pl.setp(ax1.get_xticklabels(), visible=False)

    ax1.set_ylabel('model \& data')
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    res = data.y-model(model.pars.free)
    ax2.errorbar(data.xx, res, yerr=data.yerr, ls='', marker='.')
    ax2.set_xlabel('x')
    ax2.set_ylabel('residuals')
    pl.setp(ax2.get_xticklabels(), visible=False)

    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    pars = model.pars.copy()
    xx = np.linspace(model.basis.grid.min(), model.basis.grid.max(), 500)
    J = model.basis.eval(xx)
    for i in range(len(pars.full)):
        pars.full[:] = 0.
        pars.full[i] = 3 * res.std()
        if reg_lambda is not None:
            color = pl.cm.jet(int(reg_lambda[i]/reg_lambda.max() * 256))
            # color = 'r' if reg_lambda[i]>0. else 'b'
        else:
            color = pl.cm.jet(int(i * 256/len(pars.full)))
        ax3.plot(xx, J@pars.full, ls='-', color=color)
    ax3.set_xlabel('x')

    pl.subplots_adjust(hspace=0.05)
    fig.suptitle(title)
    
def plot_model_and_data_2D(model, data, title='', reg_lambda=None):
    fig = pl.figure()
    gs = GridSpec(3, 1, height_ratios=[4,2,2])

    ax1 = fig.add_subplot(gs[0], projection='3d')
    #X0, X1 = np.meshgrid(data.xx0, data.xx1)
    ax1.errorbar(data.xx0, data.xx1, data.y, zerr=data.yerr, ecolor=('black',0.1), ls='', marker='.', color='blue')
    
    #ax1.errorbar(data.xx, data.y, yerr=data.yerr, ls='', marker='.')
    xx0 = np.linspace(model.basis.bx.grid.min(), model.basis.bx.grid.max(), 200)
    xx1 = np.linspace(model.basis.by.grid.min(), model.basis.by.grid.max(), 200)
    
    XX0, XX1 = np.meshgrid(xx0, xx1)
    
    J = model.basis.eval(XX0.ravel(), XX1.ravel())
    #ax1.plot(xx, J @ model.pars['theta'].full, 'r-', zorder=10)
    YY = J@model.pars['theta'].full
    YY = np.reshape(YY, (200,200))
    ax1.plot_surface(XX0, XX1, YY, cmap=cm.coolwarm)
    # pl.setp(ax1.get_xticklabels(), ax1.get_yticklabels(), visible=False) ??

    ax1.set_zlabel('model \& data')
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    res = data.y-model(model.pars.free)
    ax2.errorbar(data.xx0, res, yerr=data.yerr, ls='', marker='.')
    ax2.set_xlabel('x')
    ax2.set_ylabel('residuals')
    #pl.setp(ax2.get_xticklabels(), visible=False)

    #ax3 = fig.add_subplot(gs[2], sharex=ax1)
    #pars = model.pars.copy()
    #xx = np.linspace(model.basis.bx.grid.min(), model.basis.bx.grid.max(), 500)
    #J = model.basis.eval(xx)
    #for i in range(len(pars.full)):
    #    pars.full[:] = 0.
    #    pars.full[i] = 3 * res.std()
    #    if reg_lambda is not None:
    #        color = pl.cm.jet(int(reg_lambda[i]/reg_lambda.max() * 256))
    #        # color = 'r' if reg_lambda[i]>0. else 'b'
    #    else:
    #        color = pl.cm.jet(int(i * 256/len(pars.full)))
    #    ax3.plot(xx, J@pars.full, ls='-', color=color)
    #ax3.set_xlabel('x')

    pl.subplots_adjust(hspace=0.05)
    fig.suptitle(title)


def main(bsize=10, n=100, mu_reg=10., mu_reg_model=1., mu0=1.E-6, mu1=1.E-3, delta=10., order=4, fix=False,
         adapted_fit_1=False, adapted_fit_2=False, forced=False):
    """
    """
    gen = ToyDataGenGenerator(bsize=bsize, n=n, delta=delta, order=order)
    gen.generate()

    model = Model(gen.x, gen.basis.grid)
    n = len(model.pars['theta'].full)
    if fix:
        for i in range(6):
            model.pars['theta'].fix(i)
            model.pars['theta'].fix(n-i-1)

    reg = Regularization(pars = model.pars, mu0=mu0, mu1=mu1)
    # error_snake = ErrorSnake()
    # calib_error_model = CalibErrorModel()

    logging.info('FIRST FIT')
    ll = LogLikelihood(model, data=gen.get_data(), reg=[reg]) # , reg=reg, variance_model=error_snake)
    minz = Minimizer(ll)
    n_free_pars = len(model.pars.free)
    ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
    # ret = minz.minimize(p_init=np.random.rand(n_free_pars), beta=1.E-6)
    plot_model_and_data(model, gen.get_data(), 'raw')

    # iterate with adapted regularization
    if adapted_fit_1:
        logging.info('ADAPTED FIT')
        model.pars.release()
        reg = Regularization(pars=model.pars, mu0=mu0, mu1=mu1)
        _, J = model(model.pars.free, jac=1)
        l = np.array(np.maximum(mu_reg - J.sum(axis=0), 0.) / reg.matrix.sum(axis=0)).squeeze()
        L = dia_matrix((l, [0]), shape=reg.matrix.shape)
        pl.figure()
        pl.plot(l, 'k.')
        reg.matrix = reg.matrix @ L
        ll = LogLikelihood(model, data=gen.get_data(), reg=[reg])
        minz = Minimizer(ll)
        ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
        plot_model_and_data(model, gen.get_data(), title='adapted')
        pl.figure()
        pl.imshow(reg.matrix.todense())
        pl.title('adapted')

    if adapted_fit_2:
        logging.info('ADAPTED FIT 2')
        model.pars.release()
        reg = Regularization(pars=model.pars, mu0=2., mu1=1.)
        _, J = model(model.pars.free, jac=1)
        # l = np.array(np.maximum(mu_reg - J.sum(axis=0), 0.) / reg.matrix.sum(axis=0)).squeeze()
        # b = np.bincount(J.col, weights=J.data, minlength=J.shape[1])
        # bb = np.maximum(np.bincount(J.col, minlength=J.shape[1]), 1)
        # b /= bb
        # l = np.zeros_like(b)
        # l[b<0.2] = mu_reg

        cols = np.arange(J.shape[1])
        bins = np.arange(-0.5, J.shape[1]+0.5, 1.)
        d = np.digitize(J.col, bins, right=False) - 1
        l = np.array([0. if (d==col).sum() == 0 else J.data[d==col].max() for col in cols])
        idx = l<0.5
        l[idx] = mu_reg
        l[~idx] = mu_reg_model
        print(d)
        print(l)

        L = dia_matrix((l, [0]), shape=reg.matrix.shape)
        reg.matrix = reg.matrix @ L

        # model.pars.release()
        # nn = len(model.pars.full)
        # model.pars.fix(nn-1)
        # model.pars.fix(0)

        pl.figure()
        pl.plot(l, 'b')
        pl.title('$\Lambda$ (adapted regularization 2)')
        ll = LogLikelihood(model, data=gen.get_data(), reg=[reg])
        minz = Minimizer(ll)
        n_free_pars = len(model.pars.free)
        ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
        plot_model_and_data(model, gen.get_data(), title='adapted 2', reg_lambda=l)
        pl.figure()
        pl.imshow(reg.matrix.todense())
        pl.title('adapted 2')


        if forced:
            logging.info('FORCED')
            model.pars.full[:7] = 0.
            model.pars.full[-8:] = 0.
            plot_model_and_data(model, gen.get_data(), title='forced')
            v = ll(model.pars.free)
            msg = f'chi2={ll.log["main_chi2"]:.6e} | log_det_v={ll.log["log_det_v"]} | cons='
            msg += f'{ll.log["cons"]:8.6e}'
            msg += ' | reg='
            msg += f'{ll.log["reg"]:.6e}'
            logging.info(msg)

        # logging.info('FIT FORCED')
        # nn = len(model.pars.full)
        # for i in range(8):
        #     model.pars.fix(i)
        #     model.pars.fix(nn-i-1)
        # n_free_pars = len(model.pars.free)
        # ll = LogLikelihood(model, data=gen.get_data(), reg=[reg])
        # minz = Minimizer(ll)
        # ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
        # plot_model_and_data(model, gen.get_data(), title='forced fit')



    return model, gen.get_data(), minz, ret

def main_2D(bsize=10, n0=40, n1=50, mu_reg=10., mu_reg_model=1., mu0=1.E-6, mu1=1.E-3, delta=10., order=4, fix=False,
         adapted_fit_1=False, adapted_fit_2=False, forced=False):
    """
    """
    n=n0*n1
    gen = ToyDataGenGenerator2D(b0_size=bsize, b1_size=bsize, n0=n0, n1=n1)
    gen.generate()

    model = Model_2D(gen.x0, gen.x1, gen.basis.bx.grid, gen.basis.by.grid)
    n = len(model.pars['theta'].full)
    if fix:
        #for i in range(6):
        #    model.pars['theta'].fix(i)
        #    model.pars['theta'].fix(n-i-1)
        pass

    reg = Regularization(pars = model.pars, mu0=mu0, mu1=mu1)
    # error_snake = ErrorSnake()
    # calib_error_model = CalibErrorModel()

    logging.info('FIRST FIT')
    ll = LogLikelihood(model, data=gen.get_data(), reg=[reg]) # , reg=reg, variance_model=error_snake)
    minz = Minimizer(ll)
    n_free_pars = len(model.pars.free)
    ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
    # ret = minz.minimize(p_init=np.random.rand(n_free_pars), beta=1.E-6)
    plot_model_and_data_2D(model, gen.get_data(), 'raw')

    # iterate with adapted regularization
    if adapted_fit_1:
        logging.info('ADAPTED FIT')
        model.pars.release()
        reg = Regularization(pars=model.pars, mu0=mu0, mu1=mu1)
        _, J = model(model.pars.free, jac=1)
        l = np.array(np.maximum(mu_reg - J.sum(axis=0), 0.) / reg.matrix.sum(axis=0)).squeeze()
        L = dia_matrix((l, [0]), shape=reg.matrix.shape)
        pl.figure()
        pl.plot(l, 'k.')
        reg.matrix = reg.matrix @ L
        ll = LogLikelihood(model, data=gen.get_data(), reg=[reg])
        minz = Minimizer(ll)
        ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
        plot_model_and_data(model, gen.get_data(), title='adapted')
        pl.figure()
        pl.imshow(reg.matrix.todense())
        pl.title('adapted')

    if adapted_fit_2:
        logging.info('ADAPTED FIT 2')
        model.pars.release()
        reg = Regularization(pars=model.pars, mu0=2., mu1=1.)
        _, J = model(model.pars.free, jac=1)
        # l = np.array(np.maximum(mu_reg - J.sum(axis=0), 0.) / reg.matrix.sum(axis=0)).squeeze()
        # b = np.bincount(J.col, weights=J.data, minlength=J.shape[1])
        # bb = np.maximum(np.bincount(J.col, minlength=J.shape[1]), 1)
        # b /= bb
        # l = np.zeros_like(b)
        # l[b<0.2] = mu_reg

        cols = np.arange(J.shape[1])
        bins = np.arange(-0.5, J.shape[1]+0.5, 1.)
        d = np.digitize(J.col, bins, right=False) - 1
        l = np.array([0. if (d==col).sum() == 0 else J.data[d==col].max() for col in cols])
        idx = l<0.5
        l[idx] = mu_reg
        l[~idx] = mu_reg_model
        print(d)
        print(l)

        L = dia_matrix((l, [0]), shape=reg.matrix.shape)
        reg.matrix = reg.matrix @ L

        # model.pars.release()
        # nn = len(model.pars.full)
        # model.pars.fix(nn-1)
        # model.pars.fix(0)

        pl.figure()
        pl.plot(l, 'b')
        pl.title('$\Lambda$ (adapted regularization 2)')
        ll = LogLikelihood(model, data=gen.get_data(), reg=[reg])
        minz = Minimizer(ll)
        n_free_pars = len(model.pars.free)
        ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
        plot_model_and_data(model, gen.get_data(), title='adapted 2', reg_lambda=l)
        pl.figure()
        pl.imshow(reg.matrix.todense())
        pl.title('adapted 2')


        if forced:
            logging.info('FORCED')
            model.pars.full[:7] = 0.
            model.pars.full[-8:] = 0.
            plot_model_and_data(model, gen.get_data(), title='forced')
            v = ll(model.pars.free)
            msg = f'chi2={ll.log["main_chi2"]:.6e} | log_det_v={ll.log["log_det_v"]} | cons='
            msg += f'{ll.log["cons"]:8.6e}'
            msg += ' | reg='
            msg += f'{ll.log["reg"]:.6e}'
            logging.info(msg)

        # logging.info('FIT FORCED')
        # nn = len(model.pars.full)
        # for i in range(8):
        #     model.pars.fix(i)
        #     model.pars.fix(nn-i-1)
        # n_free_pars = len(model.pars.free)
        # ll = LogLikelihood(model, data=gen.get_data(), reg=[reg])
        # minz = Minimizer(ll)
        # ret = minz.minimize_lm(p_init=np.random.rand(n_free_pars), lamb=1.E-6)
        # plot_model_and_data(model, gen.get_data(), title='forced fit')



    return model, gen.get_data(), minz, ret

# def main(bsize=20, n=100):
#     gen = ToyDataGenGenerator(bsize=bsize, n=n)
#     r = gen.generate()
#     model = Model(gen.x, gen.y, gen.basis.grid)

#     ll = LogLikelihood2(model)
#     minz = Minimizer(ll)

#     return minz




# def get_naked_regularization_matrix(size, order=0):
#     """
#     Regularization matrix
#     """
#     if order == 0:
#         data = np.ones(size)
#         return dia_matrix((data, [0]), shape=(size,size)).tocoo()

#     data = np.vstack(([3.] * size, [-1.] * size, [-1.] * size))
#     data[0, 0] = data[0, -1] = 2.
#     mat = dia_matrix((data, [0, -1, 1]), shape=(size,size)).tocoo()
#     return mat


# class Model:
#     """
#     Toy model evaluated on a 1D spline basis
#     """
#     def __init__(self, x_range=(-10., 10.), basis_knots=10, x_data=None):
#         self.basis = self.init_basis(x_range=x_range, basis_knots=basis_knots)
#         self.init_pars()
#         self.x_data=x_data

#     def init_pars(self):
#         d = [('M', self.basis.nj)]
#         fp = FitParameters(list(set(d)))
#         fp['M'].full[:] = 1.
#         self.pars = fp

#     def init_basis(self, x_range=(-10., 10.), basis_knots=20):
#         x_grid = np.linspace(x_range[0], x_range[1], basis_knots)
#         basis = bspline.BSpline(x_grid, order=4)
#         return basis

#     def evals(self):
#         m = self.pars['M'].full
#         j = self.basis.eval(self.x_data)
#         #return gaussian(j@x)
#         return j@m

#     def jac(self):
#         m = self.pars['M'].full  #coeffs
#         j = self.basis.eval(self.x_data)   #J
#         M = j@m
#         n = len(m)  #len of coeffs
#         jj = []  #jacobian of the model
#         j_ = j.toarray()
#         for i in range(n):
#             #yy = -2*X*gaussian(X)
#             yy = -2*self.x_data*M
#             yy = j_[:,i]*yy
#             jj.append(yy)
#         jj = np.array(jj)
#         jj=jj.T
#         return csc_matrix(j)

#     def __call__(self, pars, deriv=True):
#         if deriv:
#             v = self.evals()
#             j = self.jac()
#             return v, j
#         else:
#             v = self.evals()
#             return v

# def chi2(model, Y, W, mat):
#     """
#     work in progress, minimizing chi2 with reg matrix
#     """
#     v, jac = model(model.pars.full, deriv=True)
#     pars = model.pars.full
#     R = Y - v
#     chi2_l = R.T@W@R
#     chi2_reg = pars.T@mat@pars
#     return chi2_l + chi2_reg


# def fit():
#     """
#     Fitting the surface on randomly generated data that follow a gaussian
#     """
#     x, err, f = gen_data()   #x, err on f, f
#     model = Model(x_data=x)
#     basis = model.basis

#     mat = get_naked_regularization_matrix(size=model.basis.nj, order=0)  #hasnt been used yet

#     #shouldn't be necessary but im projecting the generated surface on the same basis of the model
#     J = basis.eval(x)
#     W = dia_matrix((1./err**2, 0), shape=(len(x), len(x)))
#     H = J.T @ W @ J
#     factor = cholmod.cholesky(H, beta=1e-3)
#     Y = J@factor(J.T@W@f)

#     #initialising chi2
#     chi2_ndof = 2.
#     chi2_old = 10.

#     chi2_t = []
#     r_average = []  #average residuals
#     n=0  #number of iterations

#     #for i in range(10):
#     while np.abs(chi2_old - chi2_ndof) >0.001:
#         chi2_old = chi2_ndof

#         v, jac = model(model.pars.full, deriv=True)
#         R = Y - v
#         h = jac.T@W@jac
#         ff = cholmod.cholesky(h, beta=1e-3)
#         dtheta = ff(jac.T@W@R)
#         model.pars.full+=dtheta
#         n+=1
#         #chi2_ndof = np.sum(R**2/err**2)

#         #smth along the line of M.T@mat@M added to chi2

#         chi2_ndof = R.T@W@R
#         chi2_t.append(chi2_ndof)
#         r_average.append(np.sum(R)/len(R))
#     v_final, jj = model(model.pars.full)

#     resid = Y - v_final
#     return resid, model, x, f, err, n, chi2_t, r_average   #return final residuals, the model after fit, the generated data: x; f; err_f, n iteration, chi2, r_average

# def plot(r):
#     """
#     Plotter. Here 'r' is the result of the fit (so r=fit() ).
#     """
#     m = r[1]
#     pl.figure()
#     pl.errorbar(r[2], r[3], r[4], fmt='.', label='generated data')
#     pl.plot(r[2], m(m.pars.full,deriv=False), 'r.', label = 'fit')
#     pl.xlabel('x')
#     pl.ylabel('y')
#     pl.title('Toy Model Gaussian fit')
#     pl.legend()
#     pl.show()

#     pl.figure()
#     pl.plot(r[-2], 'k.')
#     pl.xlabel('iterations')
#     pl.ylabel('chi2')
#     pl.title('total chi2')
#     pl.show()

#     pl.figure()
#     pl.plot(r[2], r[0]/r[4], 'b.')
#     pl.xlabel('x')
#     pl.ylabel('R/err')
#     pl.title('weighted residuals')
#     pl.show()

#     #model after fit
#     J = m.basis.eval(m.basis.grid)
#     M = J@m.pars['M'].full

#     pl.figure()
#     pl.plot(m.basis.grid, M, 'g.')
#     pl.xlabel('x')
#     pl.ylabel('y')
#     pl.title('model')
#     pl.show()
