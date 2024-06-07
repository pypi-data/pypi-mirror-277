"""
This module implements the 7 constraints that are needed to train a
nacl.model.SALT2Like model on a dataset.

All these constraints are outlined and discussed in Guy's thesis (see. )

The contraints are implemented as quadratic penalties that are added to the
:math:`\chi^2`. These penalities are typically of the form:

.. math ::
    (f(\theta) - \alpha)^2

where :math:`f(\\theta)` is a function of the parameters, and :math:`\\alpha`
is a number.

Since there are several constraints, it is convenient to express them in vector
form:

.. math ::
    (\vec{F}(\\theta) - \vec{\alpha})^T \cdot (\vec{F}(\theta) - \vec{\alpha})


"""
import numpy as np
from scipy.sparse import coo_matrix, dok_matrix
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

class AllParametersFixedError(Exception): pass


def solve_constraints(cons, pars):
    """
    """
    H = cons.get_linearized_constraints(pars.free)
    rhs = cons.get_rhs()
    Q,R = np.linalg.qr(H.T.todense())
    dx = np.linalg.solve(R.T, rhs - H @ pars.full)
    dx = np.array(Q.dot(dx)).squeeze()

    pp = pars.copy()
    pp.full[:] = dx

    return pp.free


def ab_flux_at_10Mpc(Mb=-19.5):
    return 10**(-0.4 * (30+Mb))


class Constraint:
    """Generic contraint
    """
    def __init__(self, model, rhs):  # , pars_struct=None):
        """
        """
        self.model = model
        self.rhs = rhs
        # if pars_struct:
        #     self.pars_struct = pars_struct
        # else:
        #     self.pars_struct = self.model.pars.copy()
        #     self.pars_struct.release()

    def __call__(self, p=None, deriv=False):
        pass

class LinearConstraint(Constraint):
    """Generic linear contraints
    """
    def __init__(self, model, rhs):
        """
        """
        super().__init__(model, rhs)
        self.h_matrix = None
        self.rhs = rhs

    def init_h_matrix(self, pars):
        raise NotImplementedError()

    def init_pars(self, pars):
        """
        """
        self.h_matrix = self.init_h_matrix(pars)

    def __call__(self, pars, deriv=False):
        """evaluate the constraint
        """
        if self.h_matrix is None:
            self.h_matrix = self.init_h_matrix(pars)

        cons = self.h_matrix @ pars.full - self.rhs
        cons = float(cons)
        if not deriv:
            return cons
        return cons, self.h_matrix, None


class ConstraintSet:
    """Combine a series of constraints (linear or not)

    This class combines a set of constraints and produces a (quadratic)
    penality, added to the Log Likelihood. Compute the gradient and the hessian
    of this penality if required.
    """

    def __init__(self, constraints, mu=1.E10):
        """constructor
        """
        # self.model = model
        self.constraints = constraints
        self.mu = mu

    def init_pars(self, pars):
        """
        """
        for c in self.constraints:
            c.init_pars(pars)

    def __call__(self, pars, deriv=False):
        """evaluate the penality
        """
        npars = len(pars.full)

        pen = 0.
        # if no derivatives specified, return the sum of the quadratic
        # penalities associated with each constraint
        if not deriv:
            for cons in self.constraints:
                pen += cons(pars, deriv=False)**2
            return self.mu * float(pen)

        # otherwise, compute and return the gradient and hessian
        # along with the quadratic penality
        grad = coo_matrix(([], ([], [])), shape=(1,npars))
        hess = coo_matrix(([], ([],[])), shape=(npars,npars))
        for cons in self.constraints:
            # p=None, because self.model.pars was just updated
            c, dc, d2c = cons(pars, deriv=True)
            pen  += c**2
            # we have restored the true grad convention (-2 -> +2)
            grad += +2. * float(c) * dc
            hess += +2. * dc.T.dot(dc)
            if d2c is not None:
                hess += 2. * c * d2c

        # fixed parameters ?
        idx = pars.indexof() >= 0
        pen = float(pen)
        grad = np.array(grad[:,idx].todense()).squeeze()
        hess = hess[:,idx][idx,:]

        return self.mu * pen, self.mu * grad, self.mu * hess

    def get_rhs(self):
        return np.array([c.rhs for c in self.constraints])



class int_M0_at_phase_cons(LinearConstraint):
    """constraint on the integral of the M0 surface at peak

    This function builds a linear constraint on the M0 parameters.

    .. note:: at this stage, the constraints are a function of the *full*
       parameter vector, not just the free parameters.
    """
    def __init__(self, model, rhs, phase):
        super().__init__(model, rhs)
        self.phase = phase
    def init_h_matrix(self, pars):
        J_phase = self.model.basis.by.eval(np.array([self.phase])).toarray()
        pp = pars.copy()
        pp.release()
        gram_dot_filter = self.model.get_gram_dot_filter()
        C = coo_matrix(np.outer(J_phase, gram_dot_filter).ravel())
        # pars = self.model.all_pars_released
        npars = len(pp.full)
        i = np.full(len(C.col), 0)
        j = pp['M0'].indexof(C.col)
        M = coo_matrix((C.data, (i, j)), shape=(1, npars))
        M.data *= (self.model.norm / self.model.int_ab_spec)
        return M


class int_dM0_at_phase_cons(LinearConstraint):
    """constraint on the integral of the phase derivatives of M0 at peak
    """
    def __init__(self, model, rhs, phase):
        super().__init__(model, rhs)
        self.phase = phase
    def init_h_matrix(self, pars):
        J_dphase = self.model.basis.by.deriv(np.array([self.phase])).toarray()
        gram_dot_filter = self.model.get_gram_dot_filter()
        C = coo_matrix(np.outer(J_dphase, gram_dot_filter).ravel())
        pp = pars.copy()
        pp.release()
        # pars = self.model.all_pars_released
        npars = len(pp.full)
        j = pp['M0'].indexof(C.col)
        i = np.full(len(C.col), 0)
        v = C.data # / self.model.int_M0_phase_0 # (1.E5 * self.model.int_ab_spec)
        idx = j >= 0
        M = coo_matrix((v[idx], (i[idx], j[idx])),
                        shape=(1, npars))
        M.data *= (self.model.norm)
        return M


class int_M1_at_phase_cons(LinearConstraint):
    """constraint on the integral of the M1 surface at peak
    """
    def __init__(self, model, rhs, phase):
        super().__init__(model, rhs)
        self.phase = phase
    def init_h_matrix(self, pars):
        J_phase = self.model.basis.by.eval(np.array([self.phase])).toarray()
        gram_dot_filter = self.model.get_gram_dot_filter()
        C = coo_matrix(np.outer(J_phase, gram_dot_filter).ravel())
        pp = pars.copy()
        pp.release()
        # pars = self.model.all_pars_released
        npars = len(pp.full)
        j = pp['M1'].indexof(C.col)
        i = np.full(len(C.col), 0)
        v = C.data   #/ model.int_M0_phase_0
        idx = j >= 0
        M = coo_matrix((v[idx], (i[idx], j[idx])),
                        shape=(1, npars))
        M.data *= self.model.norm
        return M


class int_dM1_at_phase_cons(LinearConstraint):
    """constraint on the integral of the phase derivatives of M1 at peak
    """
    def __init__(self, model, rhs, phase):
        super().__init__(model, rhs)
        self.phase = phase
    def init_h_matrix(self, pars):
        J_dphase = self.model.basis.by.deriv(np.array([self.phase])).toarray()
        gram_dot_filter = self.model.get_gram_dot_filter()
        C = coo_matrix(np.outer(J_dphase, gram_dot_filter).ravel())
        pp = pars.copy()
        pp.release()
        # pars = self.model.all_pars_released
        npars = len(pp.full)
        j = pp['M1'].indexof(C.col)
        i = np.full(len(C.col), 0)
        v = C.data  # / model.int_M0_phase_0
        idx = j >= 0
        M = coo_matrix((v[idx], (i[idx], j[idx])),
                        shape=(1, npars))
        M.data *= self.model.norm
        return M


class mean_col_cons(LinearConstraint):
    """constraint on the mean of the color parameters
    """
    def __init__(self, model, rhs):
        super().__init__(model, rhs)
    def init_h_matrix(self, pars):
        nsn = len(pars['X0'].full)
        pp = pars.copy()
        pp.release()
        # pars = self.model.all_pars_released
        npars = len(pp.full)
        j = pp['c'].indexof(np.arange(nsn))
        i = np.full(nsn, 0)
        v = np.full(nsn, 1./nsn)
        idx = j >= 0
        M = coo_matrix((v[idx], (i[idx], j[idx])), shape=(1, npars))
        return M


class mean_x1_cons(LinearConstraint):
    """constraint on the mean of the x1 parameters
    """
    def __init__(self, model, rhs):
        super().__init__(model, rhs)
    def init_h_matrix(self, pars):
        nsn = len(pars['X0'].full)
        pp = pars.copy()
        pp.release()
        # pars = self.model.all_pars_released
        npars = len(pp.full)
        j = pp['X1'].indexof(np.arange(nsn))
        i = np.full(nsn, 0)
        v = np.full(nsn, 1./nsn)
        idx = j >= 0
        M = coo_matrix((v[idx], (i[idx], j[idx])),
                            shape=(1, npars))
        return M


class x1_var_cons(Constraint):

    def __init__(self, model, rhs):
        self.model = model
        self.rhs = rhs

    def __call__(self, pars, deriv=False):
        """
        """
        # if p is not None:
        #     self.model.pars.free = p.free

        # CHECK: do we need all_pars_released, or just self.model.pars ?
        pp = pars.copy()
        pp.release()
        # pars = self.model.all_pars_released
        npars = len(pp.full) # len(self.model.all_pars_released.full)
        nsn = len(pp['X0'].full)

        # constraint function: h(X1) = \sum_i X1**2
        cons = (pp['X1'].full**2).sum() / nsn  # pp or pars ?
        if not deriv:
            return cons

        # first derivatives of h
        pars.full[:] = 0.
        j = pars['X1'].indexof(np.arange(nsn))
        i = np.full(nsn, 0)
        v = pars['X1'].full
        idx = j >= 0
        J = coo_matrix((v[idx], (i[idx], j[idx])), shape=(1, npars)) # was +1

        # second derivatives of h
        i = pars['X1'].indexof(np.arange(nsn))
        v = np.full(nsn, 2./nsn)
        idx = j >= 0
        H = coo_matrix((v[idx], (i[idx], i[idx])), shape=(npars, npars))

        return cons, J, H


def salt2like_linear_constraints(model, mu=1.E6, Mb=-19.5, dm15=1.): # was 0.96
    """
    """
    m0_0 = int_M0_at_phase_cons(model, 14381300.77605067, phase=0.) # ab_flux_at_10Mpc(Mb=Mb),
    dm0_0 = int_dM0_at_phase_cons(model, 0., phase=0.)
    m1_0 = int_M1_at_phase_cons(model, 0., phase=0.)
    m1_15 = int_M1_at_phase_cons(model, dm15, phase=15.)  # rhs was 0.96
    # dm1 = int_dM1_at_phase_cons(model, 0.)
    col = mean_col_cons(model, 0.)
    x1  = mean_x1_cons(model, 0.)
    # x1_var = x1_var_cons(model, 1.)

    return ConstraintSet([m0_0, dm0_0, m1_0, m1_15, col, x1], mu=mu)


def salt2like_classical_constraints(model, mu=1.E6, Mb=-19.5):
    """
    """
    # m0_0 = int_M0_at_phase_cons(model, ab_flux_at_10Mpc(Mb=Mb), phase=0.)
    m0_0 = int_M0_at_phase_cons(model, 14381300.77605067, phase=0.)
    dm0_0 = int_dM0_at_phase_cons(model, 0., phase=0.)
    m1_0 = int_M1_at_phase_cons(model, 0., phase=0.)
    dm1 = int_dM1_at_phase_cons(model, 0.)
    col = mean_col_cons(model, 0.)
    x1  = mean_x1_cons(model, 0.)
    x1_var = x1_var_cons(model, 1.)

    return ConstraintSet(model,
                         [m0_0, dm0_0, m1_0, dm1,
                          col, x1, x1_var], mu=mu)


# class SALT2LikeConstraints:
#     """This class implements the 7 constraints (6 linear, 1 non-linear)
#     that are used when training a SALT2Like model.


#     It is typically called within the minimize.LogLikelihood class. It
#     returns the value of the contraints (squared, ready to add the to chi2),
#     the contraints gradient and hessian.
#     """

#     # this dict maps the constraint name to the corresponding
#     # block parameter name
#     _blocks = {'M0': 'M0', 'M1': 'M1', 'dM0': 'M0', 'dM1': 'M1',
#                'c': 'c', 'X1': 'X1', 'X1_var': 'X1'}

#     def __init__(self, model, mu=1.E10,
#                  active={'M0': 10**(-0.4 * (30-19.5)),
#                          'M1': 0., 'dM0': 0., 'dM1': 0.,
#                          'c': 0., 'X1': 0., 'X1_var': 1.}):
#         """
#         """
#         self.model = model
#         self.mu = mu
#         self.active = active
#         self.n_linear_cons = self.get_n_linear_cons()

#         # note: self.ncons and self.rhs cannot be known
#         # in advance because some paramters blocks may be fixed
#         # in which case the constraint is disabled
#         # self.ncons = 0
#         self.rhs = []

#         # the constraints act on the full parameter vector.
#         # So, we need to use a copy of it, with all parameters
#         # free to build the constraint matrices.
#         self.pars_full = self.model.pars.copy()
#         self.pars_full.release()
#         # number of parameters (free and fixed) and
#         # number of supernovae
#         self.npars = len(self.pars_full.full)
#         self.nsn = len(self.pars_full['X0'].full)
#         # whether the x1_vars need to be evaluated.
#         self.eval_x1_var = 'X1_var' in self.check_active()

#         # fetch the normalization filter (its projection on the spline basis)
#         # and multiply it with the model gram. This will be needed
#         # to compute the M0, M1, dM0 and dM1 constraints
#         key = self.model.normalization_band_name
#         coeffs, _ = self.model.filter_db[key]
#         self._gram_dot_filter = self.model.gram.dot(coeffs)

#         # and finally, initialize the requested (linear) constraints
#         self._init_constraints()

#     def get_n_cons(self):
#         """
#         """
#         ncons = 0
#         for cons_name in self.check_active():
#             block_name = self._blocks[cons_name]
#             idx = self.model.pars[block_name].indexof() >= 0
#             if idx.sum() > 0:
#                 ncons += 1
#         return ncons

#     def check_active(self):
#         ret = {}
#         for cons_name in self.active:
#             block_name = self._blocks[cons_name]
#             idx = self.model.pars[block_name].indexof() >= 0
#             if idx.sum() > 0:
#                 ret[cons_name] = self.active[cons_name]
#         return ret

#     def get_n_linear_cons(self):
#         ncons = self.get_n_cons()
#         active = self.check_active()
#         if 'X1_var' in active:
#             return len(active) - 1
#         return len(active)

#     def _init_constraints(self):
#         """initialize the 6 linear contraints
#         and the rhs of X1_var (if active)
#         """
#         self.ncons = self.get_n_cons()
#         active = self.check_active()
#         self.rhs = np.zeros(self.ncons)
#         self.Jac = dok_matrix((self.ncons, self.npars))

#         cons_index = 0
#         for cons_name in ['M0', 'M1', 'dM0', 'dM1', 'c', 'X1']:
#             if cons_name not in active:
#                 continue
#             f = getattr(self, 'get_' + cons_name + '_cons_jac')
#             try:
#                 Jac = f(cons_index)
#             except AllParametersFixedError:
#                 logging.warning(f'Warning: {cons_name} disabled ' + \
#                                     'all corresponding parameters are fixed')
#                 continue
#             self.Jac += Jac
#             self.rhs[cons_index] = self.active[cons_name]
#             cons_index += 1
#         if self.eval_x1_var:
#             self.rhs[self.ncons-1] = self.active['X1_var']


#     def get_M0_cons_jac(self, cons_index):
#         """matrix of the constraint on the normalization of M0
#         """
#         # some explanation may be needed:
#         # we first evaluate the bspline basis in the phase-direction
#         J_phase = self.model.basis.by.eval(np.array([0.])).toarray()

#         # we then compute all the cross-products of the phase
#         # functions and the coefficients of the gram x filter_coefficients
#         # and we re-order them so that they match the 2D-basis order
#         # (ravel does the job)
#         # note that some of the non-zero values at the end of this
#         # operation are exceedingly small and should be set to zero.
#         # This comes from the filter projection -- and I think the problem
#         # should be solved at this stage.
#         C = coo_matrix(np.outer(J_phase, self._gram_dot_filter).ravel())

#         # finally, we embed this all in a (ncons x npars) matrix
#         # since all parameters have been freed here, there is no
#         # need to filter out the fixed parameters
#         pars = self.pars_full
#         i = np.full(len(C.col), cons_index)
#         j = pars['M0'].indexof(C.col)
#         M = coo_matrix((C.data, (i, j)),
#                         shape=(self.ncons, self.npars))
#         M.data *= (self.model.norm / self.model.int_ab_spec)
#         return M

#     def get_M1_cons_jac(self, cons_index):
#         """
#         """
#         J_phase = self.model.basis.by.eval(np.array([0.])).toarray()
#         C = coo_matrix(np.outer(J_phase, self._gram_dot_filter).ravel())
#         pars = self.pars_full
#         j = pars['M1'].indexof(C.col)
#         i = np.full(len(C.col), cons_index)
#         v = C.data / self.model.int_M0_phase_0
#         idx = j >= 0
#         M = coo_matrix((v[idx], (i[idx], j[idx])),
#                        shape=(self.ncons, self.npars))
#         M.data *= self.model.norm
#         return M

#     def get_dM0_cons_jac(self, cons_index, dphase=0.): # was -0.25
#         """
#         """
#         # A mon avis, ca deconne dur ici...
#         J_dphase = self.model.basis.by.deriv(np.array([dphase])).toarray()
#         C = coo_matrix(np.outer(J_dphase, self._gram_dot_filter).ravel())

#         pars = self.pars_full
#         j = pars['M0'].indexof(C.col)
#         i = np.full(len(C.col), cons_index)
#         v = C.data # / self.model.int_M0_phase_0 # (1.E5 * self.model.int_ab_spec)
#         idx = j >= 0
#         M = coo_matrix((v[idx], (i[idx], j[idx])),
#                        shape=(self.ncons, self.npars))
#         M.data *= (self.model.norm)
#         return M

#     def get_dM1_cons_jac(self, cons_index):
#         """
#         """
#         J_dphase = self.model.basis.by.deriv(np.array([0.])).toarray()
#         C = coo_matrix(np.outer(J_dphase, self._gram_dot_filter).ravel())
#         pars = self.pars_full
#         j = pars['M1'].indexof(C.col)
#         i = np.full(len(C.col), cons_index)
#         v = C.data / self.model.int_M0_phase_0
#         idx = j >= 0
#         M = coo_matrix((v[idx], (i[idx], j[idx])),
#                        shape=(self.ncons, self.npars))
#         M.data *= self.model.norm
#         return M

#     def get_col_cons_jac(self, cons_index):
#         """
#         """
#         nsn = len(self.model.pars['X0'].full)
#         pars = self.pars_full
#         j = pars['c'].indexof(np.arange(nsn))
#         i = np.full(nsn, cons_index)
#         v = np.full(nsn, 1./nsn)
#         idx = j >= 0
#         return coo_matrix((v[idx], (i[idx], j[idx])),
#                           shape=(self.ncons, self.npars))

#     def get_X1_cons_jac(self, cons_index):
#         nsn = len(self.model.pars['X0'].full)
#         pars = self.pars_full
#         j = pars['X1'].indexof(np.arange(nsn))
#         i = np.full(nsn, cons_index)
#         v = np.full(nsn, 1./nsn)
#         idx = j >= 0
#         return coo_matrix((v[idx], (i[idx], j[idx])),
#                           shape=(self.ncons, self.npars))

#     def eval_x1_var_cons(self, deriv=False):
#         """
#         .. note : we assume that <X1> = 0
#         """
#         assert('X1_var' in self.active)
#         assert len(self.model.pars['X1'].free) > 0

#         pars = self.pars_full
#         nsn = len(pars['X0'].full)

#         # CHECK: are we sure we shouldn't use full instead of free ?
#         cons = (self.model.pars['X1'].full**2).sum() / nsn
#         if not deriv:
#             return cons


#         # first derivatives
#         pars.full[:] = 0.
#         pars['X1'].free = self.model.pars['X1'].full * 2. / nsn

#         j = pars['X1'].indexof(np.arange(nsn))
#         cons_index = self.ncons - 1
#         i = np.full(nsn, cons_index)
#         v = pars['X1'].full
#         idx = j >= 0
#         J = coo_matrix((v[idx], (i[idx], j[idx])),
#                        shape=(self.ncons, self.npars))

#         # second derivatives
#         i = pars['X1'].indexof(np.arange(nsn))
#         v = np.full(nsn, 2./nsn)
#         idx = j >= 0
#         H = coo_matrix((v[idx], (i[idx],i[idx])),
#                        shape=(self.npars, self.npars))

#         return cons, J, H

#     def __call__(self, p, deriv=False):
#         """evaluate the activated constraints and their derivatives
#         """
#         # this is done once for all, with everay __call__
#         # the subfunctions get_XXX or eval_x1_var_cons are not
#         # supposed to update the parameter vector
#         self.model.pars.free = p
#         self.pars_full.full[:] = self.model.pars.full[:]

#         # linear constraints
#         cons = self.Jac @ self.model.pars.full

#         if not deriv:
#             # penalities from the non-linear constraint
#             if self.eval_x1_var:
#                 v  = self.eval_x1_var_cons(deriv=False)
#                 cons[-1] = v
#             cons -= self.rhs
#             return self.mu * (cons**2).sum()

#         H_x1 = None
#         if self.eval_x1_var:
#             v, J, H_x1 = self.eval_x1_var_cons(deriv=True)
#             cons[-1] = v
#             J = J + self.Jac
#         else:
#             J = self.Jac
#         J = J.tocoo()

#         # cons_x1_var = cons[-1]
#         cons -= self.rhs

#         penality = self.mu * (cons**2).sum()
#         jj = self.model.pars.indexof(J.col)
#         idx = jj >= 0
#         n_free_pars = len(self.model.pars.free)
#         JJ = coo_matrix((J.data[idx], (J.row[idx], jj[idx])),
#                         shape=(self.ncons, n_free_pars))
#         grad = -self.mu * 2. * JJ.T.dot(cons)
#         hess =  self.mu * 2. * JJ.T.dot(JJ)
#         # if H_x1 is not None:
#         #     H_x1 = H_x1.tocsr()
#         #     idx = self.model.pars.indexof() >= 0
#         #     hess += (self.mu * 2. * cons[-1] * H_x1[idx,:][:,idx])

#         return penality, grad, hess

#     def get_linearized_constraints(self, p):
#         """return the linearized constraints

#         .. note:: full parameter size !
#         """
#         _, J, _ = self.eval_x1_var_cons(deriv=True)
#         J = J + self.Jac
#         return J

#     def get_rhs(self):
#         """
#         """
#         return self.rhs

# # original class written by Guy
# # it has been rewritten above, to simplify the handling of parameters
# class Constraints2D:
#     r"""
#     Local (sparse) constraints to apply to the spline part of the salt model.
#     The SED model is defined as :

#      .. math::
#         S(\lambda, t) = X_0 [M_0(\lambda, p) + X_1 M_1(\lambda, p)] \, e^{CL(\lambda) \, C}

#     where the 2D surfaces are defined on the same spline basis :

#     .. math::
#         M_{0|1}(\lambda, \mathrm{p}) = \sum_{k\ell} \theta_{k\ell}^{0|1} \mathcal{B}^t_k(\mathrm{p})
#         \mathcal{B}^m_l(\mathrm{\lambda})

#     Constraints are:

#     .. math::
#         \int M_0(\lambda, p = 0, ) T_B(\lambda) \frac{\lambda}{hc} d\lambda = 1 \\

#          \int M_1(\lambda, p = 0, ) T_B(\lambda) \frac{\lambda}{hc} d\lambda = 1 \\

#         \int \left.\frac{\partial M_0(\lambda, p = 0)}{\partial t}\right|_{t = t_{max}^{B^\star}}
#         T_B(\lambda) \frac{\lambda}{hc} d\lambda = 0 \\

#          \int \left.\frac{\partial M_1(\lambda, p = 0)}{\partial t}\right|_{t = t_{max}^{B^\star}}
#          T_B(\lambda) \frac{\lambda}{hc} d\lambda = 0 \\

#          \left<c\right> = 0 \\

#          \left<X_1\right> = 0 \\

#          \left<(X_1 - \left<X_1\right>)^2\right> = 1 \\

#     Six first constraints are linear. They are implemented in the same form :

#     .. math::
#         C(\beta) =  \alpha - H_{pen} \beta

#     For practical reasons, :math:`H_{pen}` and :math:`\alpha` are divided by the square root of the constraints
#     quadratic penalty, :math:`\sigma_{pen} = \sqrt{\mu_{pen}}`

#     The last one is a quadratic constraint then it is called : :math:`C^1(X_1)`
#     Only the constraint involving the free parameters of the model are considered.

#     Attributes
#     ----------
#     model : nacl.salt
#         Model.
#     pars : nacl.lib.fitparameters
#         Model parameters.
#     basis : nacl.lib.bspline
#         Model basis 2D surfaces splines 2D basis (wavelength, phase)

#     parameters_cons : list
#         Free parameters of the model, parameters to constraints

#     x1_var_real : bool
#         If False, consider that the mean of the constraint on the :math:`X_1` is already true, which mean that

#          .. math::
#              C^1(X_1) = \left<(X_1)^2\right> = 1

#         If True :

#          .. math::
#              C^1(X_1) = \left<(X_1 - \left<X_1\right>)^2\right> = 1

#     vals : array
#          Values of the :math:`\alpha` vector, divided by :math:`\sigma_{pen}`

#     sig_vals : array
#         Values of the :math:`\sigma_{pen}` vector.

#     mu_pq : float
#         Values of the linear constraint quadratic penalty amplitude.
#     mu_pq_var_x1 :
#         Values of the :math:`X_1` variance constraint quadratic penalty amplitude.

#     H : scipy.sparse.coo_matrix
#         :math:`H_{pen}` divided by the square root of the constraints quadratic penalty, :math:`\sigma_{pen}`
#     """

#     def __init__(self, model, mu_pq, parameters_cons=['M0', 'X0', 'tmax'],
#                  mu_pq_var_x1=None, x1_var_real=False):
#         r"""
#         Constructor.
#         Creation of the sparse matrix :math:`H_{pen}`.
#         Since the constraints are linear, each line correspond to a constraint and the colon to the model parameters
#         (: :math:`\beta`) involved in this constraint.

#         Parameters
#         ----------
#         model : nacl.salt
#             Model.
#         mu_pq : float
#             Values of the linear constraint quadratic penalty amplitude.
#         parameters_cons : list
#             Free parameters of the model, parameters to constraints
#         mu_pq_var_x1 :
#             Values of the :math:`X_1` variance constraint quadratic penalty amplitude.
#         x1_var_real : bool
#             If False, consider that the mean of the constraint on the :math:`X_1` is already true, which mean that

#              .. math::
#                  C^1(X_1) = \left< (X_1)^2 \right> = 1

#             If True :

#              .. math::
#                  C^1(X_1) = \left< (X_1 - \left< X_1 \right> )^2 \right> = 1
#         """
#         self.model = model
#         self.parameters_cons = parameters_cons
#         self.x1_var_real = x1_var_real

#         self.pars = self.model.pars
#         self.basis = self.model.basis

#         n = len(self.pars.full)
#         pp = self.pars.copy()
#         pp.release()
#         nsn = len(pp['X0'].full)
#         self.vals = []  # vals
#         tr = self.model.filter_db.transmission_db['SWOPE::B']
#         tr_eval, _ = self.model.filter_db.insert(tr, z=0)
#         filter_z = self.model.gram.dot(tr_eval)
#         comp_t = 0
#         self.mu_pq = mu_pq
#         if mu_pq_var_x1 is None:
#             self.mu_pq_var_x1 = self.mu_pq
#         else:
#             self.mu_pq_var_x1 = mu_pq_var_x1
#         sigma = 1/np.sqrt(self.mu_pq)
#         self.sig_vals = []

#         i = np.array([])
#         j = np.array([])
#         v = np.array([])

#         if ('M0' in parameters_cons) & ('X0' in parameters_cons):
#             # first constraint: S(phase = 0, band = B) == 1.
#             surface0_eval = self.model.basis.by.eval(np.array([0.])).toarray()
#             jacobian = coo_matrix(np.outer(surface0_eval, filter_z).ravel())
#             i = np.hstack((i, pp['M0'].indexof(jacobian.col)))
#             j = np.hstack((j, np.full(len(jacobian.col), comp_t)))
#             v = np.hstack((v, jacobian.data.copy()))
#             comp_t += 1
#             self.vals.append(1)
#             self.sig_vals.append(sigma)

#         if ('M0' in parameters_cons) & ('tmax' in parameters_cons):
#             # second constraint: S'(phase = 0) == 0. band = B
#             surface_zero_derivative = self.model.basis.by.deriv(np.array([0.])).toarray()
#             integral_zero_derivative = coo_matrix(np.outer(surface_zero_derivative, filter_z).ravel())
#             i = np.hstack((i, pp['M0'].indexof(integral_zero_derivative.col)))
#             j = np.hstack((j, np.full(len(integral_zero_derivative.col), comp_t)))
#             v = np.hstack((v, integral_zero_derivative.data.copy()))
#             comp_t += 1
#             self.vals.append(0)
#             self.sig_vals.append(sigma)

#         if ('M1' in parameters_cons) & ('X1' in parameters_cons):
#             # third constraint: flux_broadband_max  = 0
#             surface1_eval = self.model.basis.by.eval(np.array([0.])).toarray()
#             jacobian = coo_matrix(np.outer(surface1_eval, filter_z).ravel())
#             i = np.hstack((i, pp['M1'].indexof(jacobian.col)))
#             j = np.hstack((j, np.full(len(jacobian.col), comp_t)))
#             v = np.hstack((v, jacobian.data.copy()))
#             comp_t += 1
#             self.vals.append(0)
#             self.sig_vals.append(sigma)

#         if ('M1' in parameters_cons) & ('tmax' in parameters_cons):
#             # fourth constraint: flux_broadband_max = 0
#             surface1_zero_derivative = self.model.basis.by.deriv(np.array([0.])).toarray()
#             integral1_zero_derivative = coo_matrix(np.outer(surface1_zero_derivative, filter_z).ravel())
#             i = np.hstack((i, pp['M1'].indexof(integral1_zero_derivative.col)))
#             j = np.hstack((j, np.full(len(integral1_zero_derivative.col), comp_t)))
#             v = np.hstack((v, integral1_zero_derivative.data.copy()))
#             comp_t += 1
#             self.vals.append(0)
#             self.sig_vals.append(sigma)

#         v *= self.model.norm

#         if 'X1' in parameters_cons:
#             # mean X1 = 0
#             i = np.hstack((i, pp['X1'].indexof(np.arange(nsn))))
#             j = np.hstack((j, np.full(nsn, comp_t)))
#             v = np.hstack((v, np.full(nsn, 1)))  # X1 new constraint 1e-5
#             comp_t += 1
#             self.vals.append(0)
#             self.sig_vals.append(sigma)

#         if 'c' in parameters_cons:
#             # mean c = 0
#             i = np.hstack((i, pp['c'].indexof(np.arange(nsn))))
#             j = np.hstack((j, np.full(nsn, comp_t)))
#             v = np.hstack((v, np.full(nsn, 1)))
#             comp_t += 1
#             self.vals.append(0)
#             self.sig_vals.append(sigma)

#         self.cl_i = None
#         self.sig_vals = np.array(self.sig_vals)
#         self.vals = np.array(self.vals)/self.sig_vals
#         v /= self.sig_vals[np.array(j).astype(int)]

#         self.H = coo_matrix((v, (i, j)), shape=(n, len(self.vals))).tocsr()

#         if 'X1' in self.parameters_cons:
#             self.var_x1 = self.var_x1
#         else:
#             self.var_x1 = None

#     def var_x1(self, beta, gamma=[], jac=False):
#         r"""
#         Evaluate the seventh constraints, on the variance of the :math:`X_1` parameters.

#         If the attributes x1_var_real is True, then compute :
#             the constraint :

#             .. math::
#                  C^1(X_1) = \left<(X_1 - \left<X_1\right>)^2\right> = 1

#             it firsts derivatives wrt :math:`X_1` :

#             .. math::
#                 \frac{dC(X_1)}{dX_1^i} = \frac{2}{N} (X_1 - \bar{X_1})^T \left(\begin{matrix}
#                 - \frac{1}{N} \\
#                 ... \\
#                 (1 - \frac{1}{N})_i \\
#                 ... \\
#                 - \frac{1}{N}
#                 \end{matrix} \right)

#             it seconds derivatives wrt :math:`X_1` :

#                 .. math::
#                     \frac{d^2C(X_1)}{dX_1^j dX_1^i} &= \frac{2}{N} \left(\begin{matrix}
#                     - \frac{1}{N} \\
#                     ... \\
#                     (1 - \frac{1}{N})_j \\
#                     ... \\
#                     - \frac{1}{N}
#                     \end{matrix} \right)^T  \left(\begin{matrix}
#                     - \frac{1}{N} \\
#                     ... \\
#                     (1 - \frac{1}{N})_i \\
#                     ... \\
#                     - \frac{1}{N}
#                     \end{matrix} \right)

#         If the attributes x1_var_real is False :

#         .. math::
#             C^1(X_1) =  \frac{1}{N} X_1^T X_1 \quad  \& \quad
#             \frac{\partial C^1(X_1)}{\partial X_1^i} = \frac{2}{N^2} X_1^T  \quad  \& \quad
#             \frac{\partial^2 C^1(X_1)}{ \partial X_1^j \partial X_1^i} = \frac{2}{N^2} \delta{ij}


#         Parameters
#         ----------
#         beta : array
#             Model parameters.
#         gamma : array
#             Variance model parameters.
#         jac : bool
#             If derivatives are needed.

#         Returns
#         -------
#         cons : array
#             Value of the constraints multiply by the square root of mu_pq_var_x1

#         if jac is True :
#         jacobian_cons : array
#             Gradient of the constraints multiply by mu_pq_var_x1
#         hessian_cons :
#             Hessian of the constraints multiply by mu_pq_var_x1
#         """

#         self.pars.free = beta
#         pp = self.pars.copy()
#         nsn = len(pp['X1'].full)
#         diag = np.zeros_like(pp.free)
#         i = pp['X1'].indexof(np.arange(nsn))
#         xh, yh = np.meshgrid(i, i)
#         if self.x1_var_real is False:
#             diag[i] = np.ones(nsn)
#             cons = pp['X1'].free.var() - 1
#             dc0 = 2/nsn * diag * pp.free
#             dc = np.matrix(dc0[i])
#             jacobian_cons = 2 * dc0 * cons
#             # if gamma is not None:
#             # jacobian_cons = self.mu_pq * np.hstack((jacobian_cons, np.zeros(len(gamma))))
#             jacobian_cons = self.mu_pq_var_x1 * np.hstack((jacobian_cons, np.zeros(len(gamma))))
#             hh = np.diag([2/nsn] * len(i))
#             # hessian_cons = self.mu_pq * (2 * np.matrix(hh) * cons + 2 * dc.T @ dc)
#             hessian_cons = self.mu_pq_var_x1 * (2 * np.matrix(hh) * cons + 2 * dc.T @ dc)

#         # ## new implementation
#         # ## here mean is not Zero, mush longer for the fit to
#         # ## reach the constraints but when we start far from
#         # ## <X1> != 0 needed
#         elif self.x1_var_real:
#             jacobian_cons = np.zeros_like(pp.free)
#             x1mean = pp['X1'].free.mean()
#             x1v = pp['X1'].free - x1mean
#             cons = pp['X1'].free.var() - 1  # np.mean(x1v**2) - 1

#             dc_dxi = 2 / nsn ** 2 * (nsn * pp['X1'].free - (2 * nsn - 1) * x1mean)
#             jacobian_cons[i] = 2 * cons * dc_dxi
#             jacobian_cons = self.mu_pq_var_x1 * \
#                 np.hstack((jacobian_cons, np.zeros(len(gamma))))

#             dc_dxi_2 = 2 / nsn ** 2 * (nsn * np.diag(np.ones_like(x1v)) - \
#                                        (2 * nsn - 1) / nsn)
#             hessian_cons = self.mu_pq_var_x1 * 2 * (dc_dxi.reshape(-1, 1) @ \
#                                                     dc_dxi.reshape(-1, 1).T + \
#                                                     cons * dc_dxi_2)

#         idx = (yh.ravel() != -1) & (xh.ravel() != -1)
#         hessian_cons = coo_matrix((np.array(hessian_cons).ravel()[idx],
#                                    (yh.ravel()[idx], xh.ravel()[idx])),
#                                   shape=(len(pp.free)+len(gamma), len(pp.free)+len(gamma)))
#         cons *= np.sqrt(self.mu_pq_var_x1)
#         if jac:
#             return cons, jacobian_cons, hessian_cons
#         return cons

#     def get_rhs(self):
#         i = np.where(self.pars.indexof() >= 0)[0]
#         h = self.H[i, :].tocoo()
#         idx = np.bincount(h.col, minlength=len(self.vals)) > 0
#         return self.vals[idx]

#     def __call__(self, beta, jac=False):
#         r"""
#         Evaluate the linear constraints: :math:`C(\beta) = \alpha - H_{pen} \beta`

#         Parameters
#         ----------
#         beta : array
#             Model parameters.
#         jac : bool
#             If derivatives are needed.

#         Returns
#         -------
#         v : array
#             Value of the constraints multiply by the square root of :math:`\mu_{pq}`
#         if jac is True :
#         h : array
#             Matrix :math:`H_{pen}` by :math:`\mu_{pq}`
#         """
#         self.pars.free = beta
#         v = -self.H.T @ self.pars.full + self.vals
#         # we need to evaluate how many constraints are still valid,
#         # given which parameters are fixed. We do that by slicing the
#         # constraint matrix. There is probably a better and faster
#         # way, which avoids having to do this each time the
#         # constraints are evaluated
#         i = np.where(self.pars.indexof() >= 0)[0]
#         h = self.H[i, :].tocoo()
#         # verify that all columns of H are populated
#         j = np.where(np.bincount(h.col) > 0)[0]
#         h = h.tocsr()[:, j].tocoo()
#         # we need also to slice the return values
#         idx = np.bincount(h.col, minlength=len(self.vals)) > 0
#         if jac == 1:
#             return v[idx], h.T
#         return v[idx]
