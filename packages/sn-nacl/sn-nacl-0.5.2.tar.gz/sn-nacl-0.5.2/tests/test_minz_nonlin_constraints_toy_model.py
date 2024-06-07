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
from nacl.models.constraints import Constraint, LinearConstraint, ConstraintSet
from nacl.models.regularizations import NaClSplineRegularization
from nacl.minimize import LogLikelihood2, Minimizer
import helpers



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


class AixBiCDTrainingDataset:
    """Simplistic training dataset for tests
    """
    def __init__(self, nlc=10, npts=100,
                 a_i=None, b_i=None,
                 sigma_meas=0.1, sigma_unknown=1.):
        """constructor - initialize a recarray with simulated data
        """
        self.nlc = nlc
        self.a_i = a_i
        if a_i is None:
            self.a_i = np.random.uniform(- 5.,  5., nlc)
        self.b_i = b_i
        if b_i is None:
            self.b_i = np.random.uniform(-10., 10., nlc)
        # self.c = - self.b_i.sum()
        # self.b_i -= self.b_i.sum()
        self.c = 0.
        self.npts = npts
        self.sigma_meas = sigma_meas
        self.sigma_unknown = sigma_unknown

        i_, x_, y_, ey_, valid_ = [], [], [], [], []
        for i in range(nlc):
            x = np.random.uniform(-1, 1, npts)
            sigma_tot = np.sqrt(sigma_meas**2 + sigma_unknown**2)
            noise = np.random.normal(scale=sigma_tot, size=npts)
            y = self.a_i[i] * x + self.b_i[i] + self.c + noise
            ey = np.full(npts, sigma_meas)
            i_.append(np.full(npts, i))
            x_.append(x)
            y_.append(y)
            ey_.append(ey)
            valid_.append(np.full(npts, 1))

        self.data = np.rec.fromarrays(
            (np.hstack(i_), np.hstack(x_), np.hstack(y_),
             np.hstack(ey_), np.hstack(valid_)),
                names=('i', 'x', 'y', 'ey', 'valid'))

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


class AiBiCDModel:

    def __init__(self, training_dataset, var_class=None):
        """
        """
        self.training_dataset = training_dataset
        self.data = training_dataset.data
        self.variance_model = None
        if var_class is not None:
            self.variance_model = var_class(self)
        self.pars = self.init_pars()
        if self.variance_model is not None:
            self.variance_model.init_pars(self.pars)

    def get_struct(self):
        nlc = self.training_dataset.nlc
        return [('a_i', nlc), ('b_i', nlc), ('c', 1), ('d', 1)]

    def init_pars(self):
        s = self.get_struct()
        if self.variance_model:
            s += self.variance_model.get_struct()
        fp = FitParameters(s)
        fp['a_i'] = 1.
        return fp

    def __call__(self, p, jac=False):
        tds = self.training_dataset
        a_i = self.pars['a_i'].full[tds.data.i]
        b_i = self.pars['b_i'].full[tds.data.i]
        c = self.pars['c'].full[0]
        d = self.pars['d'].full[0]
        v = a_i * self.data['x'] + b_i + c + d
        if not jac:
            return v

        model_vals = v

        N = len(self.data)
        i,j,v = [], [], []
        i.append(np.arange(N))
        j.append(np.full(N, self.pars['a_i'].indexof(tds.data.i)))
        v.append(self.data['x'])

        i.append(np.arange(N))
        j.append(np.full(N, self.pars['b_i'].indexof(tds.data.i)))
        v.append(np.full(N, 1.))

        i.append(np.arange(N))
        j.append(np.full(N, self.pars['c'].indexof()))
        v.append(np.full(N, 1))

        i.append(np.arange(N))
        j.append(np.full(N, self.pars['d'].indexof()))
        v.append(np.full(N, 1))

        i = np.hstack(i)
        j = np.hstack(j)
        v = np.hstack(v)
        idx = j >= 0
        n_free_pars = len(self.pars.free)
        J = sparse.coo_matrix((v[idx], (i[idx],j[idx])),
                              shape=(N,n_free_pars))

        return model_vals, J



class C2DConstraint(Constraint):

    def __init__(self, model, rhs, pars_struct=None):
        super().__init__(model, rhs, pars_struct)

    def __call__(self, p=None, deriv=False):
        """
        """
        pars = self.model.pars
        cons = pars['c'].full**2 - pars['d'].full
        cons = cons.sum()
        cons -= self.rhs

        if not deriv:
            return cons

        # if deriv
        npars_full = len(self.model.pars.full)
        j = np.hstack((self.pars_struct['c'].indexof(),
                       self.pars_struct['d'].indexof()))
        v = np.hstack((2. * pars['c'].full, [-1.]))
        i = np.zeros(len(j))
        dcons = sparse.coo_matrix((v, (i,j)), shape=(1, npars_full))

        # second derivatives
        jj = self.pars_struct['d'].indexof()
        d2cons = sparse.coo_matrix((np.full(len(jj), 2.), (jj, jj)),
                          shape=(npars_full, npars_full))

        return cons, dcons, d2cons


def sum_bi(model, pars_struct=None):
    """
    """
    pars = model.pars
    npars = len(pars.full)

    i, j, v = [], [], []
    j = pars['b_i'].indexof()
    i = np.full(len(j), 0)
    v = np.full(len(j), 1.)
    mat = sparse.coo_matrix((v, (i,j)), shape=(1, npars)).tocsr()

    return LinearConstraint(model, mat, 0., pars_struct)

def c_d(model, pars_struct=None):
    pars = model.pars
    npars = len(pars.full)

    i, j, v = [], [], []
    j = np.hstack((pars['c'].indexof(), pars['d'].indexof()))
    i = np.full(len(j), 0)
    v = np.array([1., -1.])
    mat = sparse.coo_matrix((v, (i, j)), shape=(1, npars)).tocsr()

    return LinearConstraint(model, mat, 0., pars_struct)


def plot_reco(rec_data, tds, par_num=0, title=''):

    fig, axes = pl.subplots(figsize=(8,8), nrows=2, ncols=3)

    delta = rec_data.a_i.apply(lambda x: x[par_num]) - tds.a_i[par_num]
    axes[0,0].hist(delta, bins=20)
    axes[0,0].axvline(ls=':', color='r')
    axes[0,0].set_xlabel('$\Delta a$')

    delta = rec_data.b_i.apply(lambda x: x[par_num]) - tds.b_i[par_num]
    axes[0,1].hist(delta, bins=20)
    axes[0,1].axvline(ls=':', color='r')
    axes[0,1].set_xlabel('$\Delta b$')

    delta = rec_data.c - tds.c
    axes[0,2].hist(delta, bins=20)
    axes[0,2].axvline(ls=':', color='r')
    axes[0,2].set_xlabel('$\Delta c$')

    delta = rec_data.sigma - tds.sigma_unknown
    axes[1,0].hist(delta, bins=20)
    axes[1,0].axvline(ls=':', color='r')
    axes[1,0].set_xlabel('$\Delta \sigma$')

    axes[1,1].hist(rec_data.cons, bins=20)
    axes[1,1].set_xlabel('constraints')

    axes[1,2].hist(rec_data.chi2/rec_data.ndof)
    axes[1,2].set_xlabel('$\chi^2 / ndof$')

    if title:
        fig.suptitle(title)


def main_aixbicd(nlc=10, n_realizations=1, npts=100, plot=False,
                 a_i=None, b_i=None,
                 sigma_meas=0.25, sigma_unknown=1.2):
    """
    """
    ret = []
    if a_i is None:
        a_i = np.random.uniform(-10., 10., nlc)
    if b_i is None:
        b_i = np.random.uniform(-10., 10., nlc)
        b_i -= b_i.mean()
    for i in range(n_realizations):
        tds = AixBiCDTrainingDataset(nlc=nlc, npts=npts,
                                     a_i=a_i, b_i=b_i,
                                     sigma_meas=sigma_meas,
                                     sigma_unknown=sigma_unknown)
        model = AiBiCDModel(tds, var_class=VarianceModel)
        cons = ConstraintSet(model, [sum_bi(model),
                                     # c_d(model)
                                     C2DConstraint(model, 0.)
                                     ])
        ll = LogLikelihood2(model,
                            variance_model=model.variance_model,
                            cons=[cons])
        minz = Minimizer(ll)
        # n_free_pars = len(model.pars.free)
        n_pars = len(model.pars.full)
        model.pars.full[:] = np.random.uniform(-100., 100, n_pars)
        model.pars['sigma'].full[:] = 10.
        res = minz.minimize(model.pars.free)
        ret.append(((np.array(list(map(float, model.pars['a_i'].full))),
                   np.array(list(map(float, model.pars['b_i'].full))),
                   np.array([model.pars['c'].full[0]]),
                   np.array([model.pars['d'].full[0]]),
                   np.array([model.pars['sigma'].full[0]]),
                   float(cons(model.pars.free)),
                   float(res['chi2']),
                   float(res['ndof']),
                   res['status'])))

    cols = ['a_i', 'b_i', 'c', 'd', 'sigma']
    cols += ['cons', 'chi2', 'ndof', 'status']
    ret = pandas.DataFrame.from_records(ret, columns=cols,
                                        coerce_float=True)

    if plot:
        plot_reco(ret, tds,
                  title=f'AixBiCDModel [{n_realizations} realizations]')

    return ret, tds


if __name__ == '__main__':
    tds = AixBiCDTrainingDataset(sigma_unknown=2.1)
    model = AiBiCDModel(tds, var_class=VarianceModel)
    c = sum_bi(model)
    cc = C2DConstraint(model, 0.)
    cons = ConstraintSet(model, [c, cc], mu=1.E6)
    ll = LogLikelihood2(model, variance_model=model.variance_model, cons=[cons])
    minz = Minimizer(ll)
    model.pars.full[:] = np.random.uniform(-1., 1, size=23)
    model.pars['sigma'].full[:] = 10.
    r = minz.minimize_lm(model.pars.free,
                         dchi2_stop=1.E-3,
                         geo=True,
                         max_iter=1000,
                         max_attempts=40, accept=10., reject=10., lamb=1000.)

