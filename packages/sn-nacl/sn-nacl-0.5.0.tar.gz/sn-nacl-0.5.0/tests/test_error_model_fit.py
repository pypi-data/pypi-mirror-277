#    rVdVVr             tr_VdV            tr_VdVVdV
#    1                  1                 1             ok. brent.
#    1                  1                -1             cholesky failed.
#    1                 -1                 1             converged. wrong res.
#    1                 -1                -1             cholesky failed
#   -1                  1                 1             brent. wrong res.
#   -1                  1                -1             cholesky failed.
#   -1                 -1                 1             brent wrong res.
#   -1                 -1                -1             cholesky failed.




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

def plot_chi2(chi2):
    """
    """
    chi2.debug = True
    pars = chi2.model.pars
    x = np.linspace(0.2, 5., 100)
    full_chi2 = []
    main_chi2 = []
    log_det_v = []
    for xx in x:
        pars['sigma'].full[0] = xx
        full_chi2.append(chi2(pars.free))
        main_chi2.append(chi2.chi2_debug)
        log_det_v.append(chi2.log_det_v_debug)
    pl.plot(x, full_chi2, 'k.-')
    pl.plot(x, main_chi2, 'r:')
    pl.plot(x, log_det_v, 'g:')


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
        self.c = - self.b_i.sum()
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
        return [('a_i', nlc), ('b_i', nlc), ('c', 1) , ('d', 1)]

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
        v = a_i * self.data['x'] + b_i + c  + d
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


class Constraint:

    def __init__(self, model, rhs, pars_struct=None):
        """
        """
        self.model = model
        self.rhs = rhs
        if pars_struct:
            self.pars_struct = pars_struct
        else:
            self.pars_struct = self.model.pars.copy()
            self.pars_struct.release()

    def __call__(self, p=None, deriv=False):
        pass


class LinearConstraint(Constraint):

    def __init__(self, model, h_matrix, rhs, pars_struct=None):
        """
        """
        super().__init__(model, rhs, pars_struct)
        self.h_matrix = h_matrix
        self.rhs = rhs
        # if pars_struct:
        #     self.pars_struct = pars_struct
        # else:
        #     self.pars_struct = self.model.pars.copy()
        #     self.pars_struct.release()

    def __call__(self, p=None, deriv=False):
        """
        """
        cons = self.h_matrix @ self.model.pars.full - self.rhs
        cons = float(cons)
        if not deriv:
            return cons
        return cons, self.h_matrix, None


class ModelBCD2Constraint(Constraint):

    def __init__(self, model, rhs, pars_struct=None):
        super().__init__(model, rhs, pars_struct)

    def __call__(self, p=None, deriv=False):
        """
        """
        pars = self.model.pars
        cons = pars['b_i'].full**2 + pars['c'].full**2 + pars['d'].full**2
        cons = cons.sum()
        cons -= self.rhs

        if not deriv:
            return cons

        # if deriv
        npars_full = len(self.model.pars.full)
        j = np.hstack((self.pars_struct['b_i'].indexof(),
                       self.pars_struct['c'].indexof(),
                       self.pars_struct['d'].indexof()))
        v = np.hstack((2. * pars['b_i'].full,
                       2. * pars['c'].full,
                       2. * pars['d'].full))
        i = np.zeros(len(j))
        dcons = sparse.coo_matrix((v, (i,j)), shape=(1, npars_full))

        # second derivatives
        d2cons = sparse.coo_matrix((np.full(len(j), 2.), (j,j)),
                          shape=(npars_full, npars_full))

        return cons, dcons, d2cons


class ConstraintSet:
    """Combine a series of constraints to produce a (quadratic) penality,
    added to the Log Likelihood. Compute the gradient and the hessian
    of this penality if required.
    """
    def __init__(self, model, constraints):
        """constructor
        """
        self.model = model
        self.constraints = constraints

    def __call__(self, p=None, deriv=False):
        """evaluate the penality
        """
        if p is not None:
            self.model.pars.free = p

        npars = len(self.model.pars.full)

        pen = 0.
        # if no derivatives specified, return the sum of the quadratic
        # penalities associated with each constraint
        if not deriv:
            for cons in self.constraints:
                pen += cons(p=p, deriv=False)**2
            return float(pen)

        # otherwise, compute and return the gradient and hessian
        # along with the quadratic penality
        grad = sparse.coo_matrix(([], ([], [])), shape=(1,npars))
        hess = sparse.coo_matrix(([], ([],[])), shape=(npars,npars))
        for cons in self.constraints:
            c, dc, d2c = cons(p=p, deriv=True)
            pen  += c**2
            # TODO: return +grad and change the minimizer.
            # here, we return -grad, which is misleading
            grad += -2. * float(c) * dc
            hess +=  2. * dc.T.dot(dc)
            if d2c is not None:
                hess += 2. * c * d2c

        # fixed parameters ?
        idx = self.model.pars.indexof() >= 0
        pen = float(pen)
        grad = np.array(grad[:,idx].todense()).squeeze()
        hess = hess[:,idx][idx,:]

        return pen, grad, hess


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


def test_aibicd_d_fixed_linear_constraint():
    tds = AixBiCDTrainingDataset(sigma_unknown=2.1)
    model = AiBiCDModel(tds, var_class=VarianceModel)
    model.pars['d'].fix()
    c = sum_bi(model)
    cons = ConstraintSet(model, [c])
    ll = LogLikelihood2(model, variance_model=model.variance_model, cons=[cons])
    minz = Minimizer(ll)
    ret = minz.minimize(model.pars.free)
    ret['model'] = model
    ret['cons'] = cons
    return ret


class AixBiCDConstraints:

    def __init__(self, model, mu=1.E10):
        self.model = model
        self.mu = mu
        self.pars_full = self.model.pars.copy()
        self.pars_full.release()
        self.rhs = np.array([0.])  # , 1000.])
        self.active = {}
        self.ncons = 1
        self.dh = {}
        self.dh[0] = self._init_dh_0()

    def _init_dh_0(self):
        """precompute the matrix of the first constraints
        """
        npars = len(self.model.pars.full)
        pars = self.pars_full

        # \sum b_i + c = 0
        i, j, v = [], [], []
        j = np.hstack((pars['b_i'].indexof(), pars['c'].indexof()))
        i = np.full(len(j), 0)
        v = np.full(len(j), 1.)
        return sparse.coo_matrix((v, (i,j)), shape=(1, npars)).tocsr()

    def eval_0(self, deriv=False):
        """
        """
        h = float(self.dh[0] @ self.model.pars.full[:])
        if not deriv:
            return h
        return h, self.dh[0], None

    def eval_1(self, deriv=False):
        """
        """
        pars = self.pars_full
        npars = len(pars.full)

        h = (pars['b_i'].full**2).sum() + \
             pars['c'].full[0]**2
             # pars['d'].full[0]**2

        if not deriv:
            return h

        # first derivatives
        i, j, v = [], [], []
        j.append(pars['b_i'].indexof())
        j.append(pars['c'].indexof())
        # j.append(pars['d'].indexof())
        j = np.hstack(j)
        i = np.zeros(len(j))
        v.append(2. * pars['b_i'].full)
        v.append(2. * pars['c'].full)
        # v.append(2. * pars['d'].full)
        v = np.hstack(v)
        dh = sparse.coo_matrix((v, (i, j)),
                                shape=(1, npars)).tocsr()
        # second derivatives
        i, j, v = [], [], []
        i = np.hstack((pars['b_i'].indexof(),
                       pars['c'].indexof(),
                       # pars['d'].indexof())
                       ))
        j = i
        v = np.full(len(i), 2.)
        d2h = sparse.coo_matrix((v, (i, j)),
                                shape=(npars, npars))

        return h, dh, None

    def check_active(self):
        """if some parameters are all fixed, the related constraints
        should probably be deactivated (?)
        """
        pass

    def __call__(self, p, deriv=False):
        """
        """
        self.model.pars.free = p
        self.pars_full.full[:] = self.model.pars.full[:]
        n_pars_full = len(self.model.pars.full)
        h = np.zeros(self.ncons)
        if not deriv:
            for i,f in enumerate([self.eval_0]):  # self.eval_1
                h[i] = f(deriv=False)
            cons = h - self.rhs
            return self.mu * (h**2).sum()

        dh  = sparse.coo_matrix(([], ([], [])),
                                shape=(self.ncons, n_pars_full)).tocsr()
        d2h = []

        # call all the constraints
        # in fact, we could precalculate the linear ones
        # and only call the non-linear ones.
        # but ok. no difference.
        # d2_available = False
        for i, f in enumerate([self.eval_0]):  # , self.eval_1]):
            h_, dh_, d2h_ = f(deriv=True)
            h[i] += h_
            dh[i,:] += dh_
            d2h.append(d2h_)

        cons = h - self.rhs
        penality = cons.T @ cons

        idx = self.model.pars.indexof()>=0
        grad = -2. * dh.T.dot(cons)[idx]
        hess =  2. * dh.T.dot(dh)[idx,:][:,idx]
        for i,d2 in enumerate(d2h):
            if d2 is not None:
                hess += 2. * cons[i] * d2

        return self.mu * penality, self.mu * grad, self.mu * hess

    # def __call__(self, p, deriv=False):
    #     """
    #     """
    #     self.model.pars.free = p
    #     self.pars_full.full[:] = self.model.pars.full[:]

    #     cons = self.Jac @ self.model.pars.full
    #     cons -= self.rhs

    #     cons_t_cons = float(cons.T @ cons)
    #     if not deriv:
    #         return self.mu * cons_t_cons

    #     JJ = self.Jac
    #     grad = -2. * self.mu * JJ.T.dot(cons)
    #     hess =  2. * self.mu * JJ.T.dot(JJ)

    #     return self.mu * cons_t_cons, grad, hess

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
    for i in range(n_realizations):
        tds = AixBiCDTrainingDataset(nlc=nlc, npts=npts,
                                     a_i=a_i, b_i=b_i,
                                     sigma_meas=sigma_meas,
                                     sigma_unknown=sigma_unknown)
        model = AiBiCDModel(tds, var_class=VarianceModel)
        model.pars['d'].fix()
        cons = AixBiCDConstraints(model, mu=1E10)
        ll = LogLikelihood2(model,
                            variance_model=model.variance_model,
                            cons=[cons])
        minz = Minimizer(ll)
        n_free_pars = len(model.pars.free)
        model.pars.full[:] = np.random.uniform(-100., 100, n_free_pars)
        model.pars['sigma'].full[:] = 10.
        res = minz.minimize(model.pars.free)
        ret.append(((np.array(list(map(float, model.pars['a_i'].full))),
                   np.array(list(map(float, model.pars['b_i'].full))),
                   np.array([model.pars['c'].full[0]]),
                   np.array([model.pars['sigma'].full[0]]),
                   float(cons(model.pars.free)),
                   float(res['chi2']),
                   float(res['ndof']),
                   res['status'])))

    cols = ['a_i', 'b_i', 'c', 'sigma']
    # for k, slc in model.pars._struct.slices.items():
    #     n = slc.stop-slc.start
    #     if n == 1:
    #         cols.append(k)
    #     else:
    #         for i in range(n):
    #             cols.append(f'{k}_{i}')
    cols += ['cons', 'chi2', 'ndof', 'status']
    ret = pandas.DataFrame.from_records(ret, columns=cols,
                                        coerce_float=True)

    if plot:
        plot_reco(ret, tds,
                  title=f'AixBiCDModel [{n_realizations} realizations]')

    return ret, tds


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


