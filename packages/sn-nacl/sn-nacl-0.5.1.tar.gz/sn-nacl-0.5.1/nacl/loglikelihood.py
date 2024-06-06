"""Log Likelihood
"""

import numpy as np
import scipy.sparse as sparse
import logging

try:
    from sparse_dot_mkl import gram_matrix_mkl, dot_product_mkl
except:
    logging.warning('module: `sparse_dot_mkl` not available')
else:
    logging.info('sparse_dot_mkl found. Building hessian should be faster.')


from saltworks import FitParameters

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",
                    level=logging.INFO)



class LogLikelihood:
    """New log likelihood class
    """
    def __init__(self, model, variance_model=None,
                 cons=None, reg=None, priors=None,
                 data=None, error_pedestal=None,
                 force_default_spgemm=False):
        """
        """
        # the log-likelihood constituents
        self.model = model
        self.cons = cons
        self.reg = reg
        self.priors = priors
        self.variance_model = variance_model

        # now, we can create a parameter vector
        self.pars = self.init_pars()

        self.force_default_spgemm = force_default_spgemm

        self.data = data
        if data is not None:
            self.y, self.yerr, self.bads = np.array(data.y), np.array(data.yerr), np.array(data.bads)
        else:
            self.y, self.yerr, self.bads = np.array(model.y), np.array(model.yerr), np.array(model.bads)

        # in general, it is better to fit a real error model but if you are lazy
        # (we are all) you may prepare an error pedestal and add it in
        # quadrature to the measurement errors
        self.error_pedestal = error_pedestal
        self.log = {}

    def init_pars(self):
        """create and initialize full parameter vector
        """
        # retrieve the fitparameter structure from our constituents
        # Note: constraints and regularization objects are not expected
        # to add parameters to the problem.
        struct = self.model.get_struct()
        if self.variance_model is not None:
            struct.extend(self.variance_model.get_struct())
        if self.priors is not None:
            for p in self.priors:
                struct.extend(p.get_struct())

        pars = FitParameters(struct)

        # now, initialize the parameter vector note: constraints and
        # regularization may change the initialization parameters, but they
        # don't have to...
        try:
            self.model.init_pars(pars)
        except:
            self.model.init_pars()
        if self.variance_model is not None and hasattr(self.variance_model, 'init_pars'):
            self.variance_model.init_pars(pars)
        if self.cons is not None:
            for c in self.cons:
                if hasattr(c, 'init_pars'):
                    c.init_pars(pars)
        if self.reg is not None:
            for r in self.reg:
                if hasattr(r, 'init_pars'):
                    r.init_pars(pars)
        if self.priors is not None:
            for r in self.priors:
                if hasattr(r, 'init_pars'):
                    r.init_pars(pars)
        return pars

    def ndof(self):
        """return the degrees of freedom
        """
        nmeas = (~self.bads).sum()
        n_free_pars = len(self.pars.free)
        return int(nmeas - n_free_pars)

    def get_log(self):
        return self.log.copy()

    def __call__(self, p, deriv=False):
        """
        """
        self.pars.free = p
        self.log = {}

        # the ingredients
        main_chi2 = 0.
        cons_penalty = 0.
        reg_penalty = 0.
        bads = self.bads

        # evaluate the model and variance model
        pred, J = _eval_model(self.model, self.pars, jac=deriv)

        # diagonal variance and main chi2
        # total variance is the sum of the measurement errors
        # and the variance model
        var = self.yerr**2
        if self.variance_model:
            vv, J_var  = _eval_model(self.variance_model, self.pars, jac=deriv)
            var += vv

        # we assume here that the user knows what s/he is doing and that s/he
        # has carefully prepare an error pedestal of the correct dimension, to
        # add to the model. We do not check anything here.
        if self.error_pedestal is not None:
            var += self.phot_error_pedestal ** 2

        # the residuals and the chi2
        res = self.y - pred
        sig = np.sqrt(var)
        w_res = res / sig
        # TODO: check: bads !
        self.w_res = w_res
        main_chi2 = (w_res**2)[~bads].sum()

        # the log of the determinant
        if self.variance_model is not None:
            log_det_v = np.log(var[~bads]).sum()
        else:
            log_det_v = 0.

        # and the total log-likelihood before taxes
        llk = main_chi2 + log_det_v

        # evaluate the penalties and add them to the chi2
        # quadratic regularization
        reg_penalty, reg_grad, reg_hess = _eval_penalties(self.reg, self.pars, deriv=deriv)
        llk += reg_penalty

        # quadratic constraints
        cons_penalty, cons_grad, cons_hess = _eval_penalties(self.cons, self.pars, deriv=deriv)
        llk += cons_penalty

        # general priors
        prior_penalty, prior_grad, prior_hess = _eval_penalties(self.priors, self.pars, deriv=deriv)
        llk += prior_penalty

        self.log = {'llk': llk,
                    'main_chi2': main_chi2,
                    'log_det_v': log_det_v,
                    'cons': np.sum(cons_penalty),
                    'reg': np.sum(reg_penalty),
                    'priors': np.sum(prior_penalty)}

        if not deriv:
            return llk

        # OK That was the easy part.
        # Now, we need to compute the derivatives

        # 1. the gradient and hessian have several components
        # first, the two classical ones: J^TWJ and J^TWR
        # J^TWJ is difficult to compute.
        w = 1. / np.sqrt(var)
        N = len(self.y)
        W = sparse.dia_matrix((w, [0]), shape=(N,N))
        # in general we discard the bads only at the last minute.
        # we make an exception for w_J
        w_J = (W @ J)[~bads,:]

        grad = -2. * w_J.T @ w_res[~bads]
        w_J = w_J.tocsr()


        # gram_matrix_mkl implements a multiproc version
        # -- much faster if several cores are available
        if 'gram_matrix_mkl' in globals() and not self.force_default_spgemm:
            logging.debug('hessian: H = J.T @ J (gram_matrix_mkl)')
            # there seem to be a bug in gram_matrix_mkl when one of the matrix
            # dimensions is one. typically refuses to contract (N,1) matrix into
            # a scalar. Hence this workaround
            if len(w_J.data) == 0:
                hess = 2. * w_J.T @ w_J
            elif 1 in w_J.shape:
                hess = 2. * dot_product_mkl(w_J.T, w_J, reorder_output=True)
            else:
                # `reorder_output=True` seems essential here.
                # otherwise, the Newton-Raphson step is wrong, typically
                # by a factor 0.5 ... this is scary, I know...
                # print(f'[DEBUG]  {w_J.shape} {w_J.__class__} {w_J.data}')
                hess = 2. * gram_matrix_mkl(w_J, transpose=False, reorder_output=True).tolil() # was transpose=False !
                # print(f'[DEBUG] {hess.shape} {hess.__class__}')
                row, col = hess.nonzero()
                hess[col,row] = hess[row,col]
        # slow single core version
        else:
            logging.debug('hessian: H = J.T @ J (slow version)')
            hess = 2. * w_J.T @ w_J

        # then, if a variance model has been specified, we need to
        # add its contributions to the gradient and the hessian
        if self.variance_model is not None:
            logging.debug('variance model')
            WW = sparse.dia_matrix((w**2, [0]), shape=(N,N))
            J_var = (WW @ J_var)[~bads, :]

            # gradient
            # TODO: check that bad removal did not introduce a bug here
            mvJ = J_var.tocoo()
            w_res_mvJ = sparse.coo_matrix(
                (mvJ.data * w_res[mvJ.row],
                 (mvJ.row, mvJ.col)),
                shape=mvJ.shape)
            rWdVWr = 1. * w_res_mvJ.T @ w_res

            grad += -1. * rWdVWr
            tr_WdV = 1. * np.array(J_var.T.sum(axis=1)).squeeze()
            grad += tr_WdV

            # hessian
            tr_WdVWdV = 1. * J_var.T.dot(J_var)
            hess += tr_WdVWdV

        # OK. That was the hard part
        # now, the quadratic penalties
        if cons_grad is not None and cons_hess is not None:
            grad += cons_grad
            hess += cons_hess

        if reg_grad is not None and reg_hess is not None:
            grad += reg_grad
            hess += reg_hess

        if prior_grad is not None and prior_hess is not None:
            grad += prior_grad
            hess += prior_hess

        msg = f'chi2={main_chi2:.6e} | log_det_v={log_det_v} | cons='
        msg += f'{cons_penalty:8.6e}'
        msg += ' | reg='
        msg += f'{reg_penalty:.6e}'
        msg += ' | prior='
        msg += f'{prior_penalty:.6e}'
        logging.info(msg)

        return llk, grad, hess


def _eval_model(f, pars, jac):
    """A wrapper around the model, to make its evaluation more generic
    """
    val, J = None, None
    if not jac:
        val = f(pars, jac=False)
    else:
        val, J = f(pars, jac=True)
    return val, J


def _eval_penalties(penalties, pars, deriv, return_log=False):
    """A wrapper to simplify the call to the quadratic penalties
    """
    _log = []
    val, grad, hess = 0., None, None
    if penalties is None:
        return val, grad, hess

    for pen in penalties:
        if pen is None:
            return val, grad, hess
        if not deriv:
            v = pen(pars, deriv=False)
            val += v
        else:
            v, gr, hs = pen(pars, deriv=True)
            val += v
            grad = gr if grad is None else grad + gr
            hess = hs if hess is None else hess + hs
        if return_log:
            _log.append(v)
    if return_log:
        return val, grad, hess, _log
    return val, grad, hess
