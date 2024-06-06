import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

from scipy import sparse
import numpy as np
import pylab as pl
import pandas
from nacl.lib.fitparameters import FitParameters
from nacl.dataset import TrainingDataset
from nacl.models.salt import SALT2Like
from nacl.models.constraints import SALT2LikeConstraints
from nacl.models.regularizations import NaClSplineRegularization
from nacl.minimize import LogLikelihood2, Minimizer
import helpers


class AxBTrainingDataset:
    """Simplistic training dataset for tests
    """
    def __init__(self, N=100, a=1., b=0., sigma_meas=0.1, sigma_unknown=1.):
        """constructor - initialize a recarray with simulated data
        """
        x = np.random.uniform(-1, 1, N)
        sigma_tot = np.sqrt(sigma_meas**2 + sigma_unknown**2)
        print(sigma_meas, sigma_unknown, sigma_tot)
        noise = np.random.normal(scale=sigma_tot, size=N)
        y = a * x + b + noise
        ey = np.full(N, sigma_meas)
        valid = np.full(N, 1)
        self.data = np.rec.fromarrays((x, y, ey, valid),
                                      names=('x', 'y', 'ey', 'valid'))

    def nb_meas(self, valid_only=False):
        if valid_only:
            return self.data['valid'].sum()
        return len(self.data)

    def get_all_fluxes(self):
        return self.data['y']

    def get_all_fluxerr(self):
        return self.data['ey']

    def get_valid(self):
        return self.data['valid']

    def plot(self, ax=None, model=None):
        if ax is None:
            fig, axes = pl.subplots(nrows=1, ncols=1, figsize=(8,8))
        axes.errorbar(self.data['x'], self.data['y'],
                      yerr=self.data['ey'],
                      ls='', marker='.', color='k')
        if model is not None:
            a = model.pars['a'].full[0]
            b = model.pars['b'].full[0]
            pl.plot(self.data['x'], a*self.data['x']+b, 'r-')
        return axes


class Model:

    def __init__(self, training_dataset, var_class=None):
        self.training_dataset = training_dataset
        self.data = training_dataset.data
        if var_class is not None:
            self.variance_model = var_class(self)
        self.pars = self.init_pars()
        if self.variance_model is not None:
            self.variance_model.init_pars(self.pars)

    def get_struct(self):
        return [('a', 1), ('b', 1)]

    def init_pars(self):
        s = self.get_struct()
        if self.variance_model:
            s += self.variance_model.get_struct()
        fp = FitParameters(s)
        fp['a'] = 1.
        return fp

    def __call__(self, p, jac=False):
        a, b = self.pars['a'].full[0], self.pars['b'].full[0]
        v = a * self.data['x'] + b
        if not jac:
            return v

        model_vals = v

        N = len(self.data)
        i,j,v = [], [], []
        i.append(np.arange(N))
        j.append(np.full(N, self.pars['a'].indexof()))
        v.append(self.data['x'])

        i.append(np.arange(N))
        j.append(np.full(N, self.pars['b'].indexof()))
        v.append(np.full(N, 1.))

        i = np.hstack(i)
        j = np.hstack(j)
        v = np.hstack(v)
        idx = j >= 0
        n_free_pars = len(self.pars.free)
        J = sparse.coo_matrix((v[idx], (i[idx],j[idx])),
                              shape=(N,n_free_pars))

        return model_vals, J


class VarianceModel:

    def __init__(self, model):
        self.training_dataset = model.training_dataset
        self.data = model.data

    def get_struct(self):
        return [('sigma', 1)]

    def init_pars(self, pars):
        self.pars = pars
        self.pars['sigma'].full[:] = 0.5

    def __call__(self, jac=False, model_flux=None, model_jac=None):
        """
        """
        N = len(self.data)
        sigma = self.pars['sigma'].full[0]
        v = np.full(N, sigma**2)
        if not jac:
            return v

        i = np.arange(N)
        j = np.full(N, self.pars['sigma'].indexof())
        vv = np.full(N, 2. * sigma)
        idx = j >= 0
        n_free_pars = len(self.pars.free)
        J = sparse.coo_matrix((vv[idx], (i[idx], j[idx])),
                               shape=(N, n_free_pars))
        return v, J

    def noise(self, N):
        v = self(jac=False)
        return np.random.normal(scale=np.sqrt(v))


def main_axb(N_realizations=1, N=100, plot=False):
    """
    """
    res = []
    for i in range(N_realizations):
        data = AxBTrainingDataset(N=100)
        model = Model(data, var_class=VarianceModel)
        ll = LogLikelihood2(model, variance_model=model.variance_model)
        minz = Minimizer(ll)
        model.pars.full[0] = 2.
        model.pars.full[1] = 2.
        model.pars.full[2] = 4.
        # model.pars.fix()
        # model.pars['sigma'].release()
        # model.pars['sigma'].fix()
        # s = minz.minimize(model.pars.free)
        # model.pars.release()
        # model.pars.fix()
        # model.pars['sigma'].release()
        s = minz.minimize(model.pars.free)
        pp = s['pars']
        res.append((pp['a'].full[0], pp['b'].full[0], pp['sigma'].full[0]))

    res = np.rec.fromrecords(res, names=['a', 'b', 'sigma'])

    if plot:
        fig, axes = pl.subplots(nrows=2, ncols=2, figsize=(8,8))
        axes[0,0].hist(res['a'], bins=20)
        axes[0,0].set_xlabel('a')
        axes[0,0].set_title('a')
        axes[0,0].axvline(1, ls=':', color='r')

        axes[0,1].hist(res['b'], bins=20)
        axes[0,1].set_xlabel('b')
        axes[0,1].set_title('b')
        axes[0,1].axvline(0, ls=':', color='r')

        axes[1,0].hist(res['sigma'], bins=20)
        axes[1,0].set_xlabel('$\sigma$')
        axes[1,0].set_title('$\sigma$')
        axes[1,0].axvline(1, ls=':', color='r')

    return res, s


if __name__ == '__main__':
    res, s = main_axb(1)


