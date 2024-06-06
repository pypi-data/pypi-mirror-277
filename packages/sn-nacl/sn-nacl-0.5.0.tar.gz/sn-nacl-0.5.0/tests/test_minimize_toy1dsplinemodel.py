import os
import os.path as op
import numpy as np
import scipy.sparse
import saunerie
import croaks
from saunerie.fitparameters import FitParameters

from salt3.minimizers import minimize_nr_var_quad
import salt3.generator
import salt3.models
import salt3.plots

from helpers import locate_test_datafile
from helpers import check_grad


class ToySplineModel:
    """A simple Toy spline model of the form: 
    
    just one flux per SN and a spline template common to all SNe. 
    No tmax, no stretch. 

    This model is intrinsically degenerate and should be fitted with constraints. 
    
    Simple, sparse constraints such as:
     - S(phase=0) = 1.
     - S'(phase=0) = 0
     generally work well
    """
    def __init__(self, dp, phase_range=[-100., 100.], grid_size=30):
        self.dp = dp
        self.nb_sn = len(dp.sn_set)
        self.spline_basis = saunerie.bspline.CardinalBSplineC(grid_size, phase_range)
        self.n_theta = grid_size
        self.pars = self.init_pars(dp)
        phases = self.dp.date
        self.jacobian = self.spline_basis.eval(phases)
        
    def init_pars(self, dp):
        fp = FitParameters([('flux', self.nb_sn), ("theta", len(self.spline_basis))])
        fp['flux'].full[:] = 1.
        fp['theta'].full[:] = 1.E-6
        return fp

    def __call__(self, p, jac=False, dp=None):
        """
        """
        self.pars.free = p
        if dp is None:
            dp = self.dp
            jacobian = self.jacobian
        else:
            phases = dp.date
            jacobian = self.spline_basis.eval(phases)
            
        sn_index = dp.sn_index
        flx = self.pars['flux'].full[sn_index]
        
        v = flx * (jacobian @ self.pars['theta'].full)

        if jac:
            N = len(dp.nt)
            n = len(self.spline_basis)
            i = np.arange(N)
            
            # dmodel_dflux 
            i_dm_dflux = i
            j_dm_dflux = self.pars['flux'].indexof(sn_index)
            v_dm_dflux = jacobian @ self.pars['theta'].full

            # dmodel_dtheta
            i_dm_dtheta = jacobian.row
            j_dm_dtheta = self.pars['theta'].indexof(jacobian.col)
            v_dm_dtheta = self.pars['flux'].full[sn_index[jacobian.row]] * jacobian.data
            
            i = np.hstack((i_dm_dflux, i_dm_dtheta))
            j = np.hstack((j_dm_dflux, j_dm_dtheta))            
            val = np.hstack((v_dm_dflux, v_dm_dtheta))
            
            idx_fix = np.where(j != -1)[0]
            DZ = scipy.sparse.coo_matrix((val[idx_fix], (i[idx_fix], j[idx_fix])), shape=(N, len(self.pars.free)))
            
            return v, DZ
        
        return v


class ToySplineNonIntegralConstraints():
    """
    .. note:: this implementation of the constraints 
              does adapt the size of the H matrix 
              to the number of fixed parameters. 
              On the other hand, it does not eliminate
              the constraints that have become irrelevant. 
              Then, the H.T matrix which is returned by __call__() 
              may be of rank < 3
    """
    def __init__(self, pars, basis, vals=[1., 0.]):
        self.pars = pars
        self.basis = basis
        self.vals = self.d = np.array(vals)
        assert(len(self.d) == 2)
        
        n = len(self.pars.full)
        
        # first constraint: S(0) = 1
        jacobian = self.basis.eval(np.array([0]))
        i1 = pars['theta'].indexof(jacobian.col)
        j1 = np.full(len(jacobian.col), 0)
        v1 = jacobian.data.copy()
        # second constraint: S'(0) = 0
        Jp = self.basis.deriv(np.array([0]))
        i2 = pars['theta'].indexof(Jp.col)
        j2 = np.full(len(Jp.col), 1)
        v2 = Jp.data.copy()
        self.H = scipy.sparse.coo_matrix((np.hstack((v1,v2)), (np.hstack((i1,i2)), np.hstack((j1,j2)))), shape=(n,2)).tocsr()
        
    # def __len__(self):
    #     return 2

    def get_rhs(self):
        return self.d
        
    def __call__(self, p, jac=False):
        self.pars.free = p
        v = -self.H.T @ self.pars.full + self.vals
        
        if jac:
            i = np.where(self.pars.indexof() >= 0)[0]
            return v, self.H[i,:].T
        return v


class ToySplineRegularization():
    
    def __init__(self, pars, mu=1.E-8):
        self.pars = pars
        self.mu = mu

        # build the regularization matrix
        n = len(self.pars['theta'].full)
        data = np.ones(n).astype(float)
        M = self.mu * scipy.sparse.dia_matrix((data, [0]), shape=(n,n)).tocoo()

        # build the large matrix which corresponds to the model parameters
        pp = pars.copy()
        pp.release()
        N = len(pp.full)
        i = pp['theta'].indexof(M.row)
        j = pp['theta'].indexof(M.col)
        idx = (i>=0) & (j>=0) # should be all true's
        self.M = scipy.sparse.coo_matrix((M.data[idx], (i[idx],j[idx])), shape=(N,N)).tocsr()
        
    def __call__(self, p, jac=True):
        self.pars.free = p
        v = float(self.pars.full.T @ self.M @ self.pars.full)
        if jac:
            i = np.where(self.pars.indexof() >= 0)[0]
            # there might be a more efficient way to slice the matrix ...
            return v, self.M[i,:][:,i]
        return v

    
def main(N=1000, minimize=minimize_nr_var_quad, mu_regularization=500., plot=False, seed=None):
    """
    """
    lc_data = salt3.generator.generate_lc(N, tmax_range=(0., 0.),
                                          sig_range=(0., 0.),
                                          norm_range=(1000., 1000.),
                                          seed=seed)
    
    model = ToySplineModel(lc_data, grid_size=250) # phase_range=[lc_data.date.min(), lc_data.date.max()]
    f = salt3.models.VarModelResiduals(lc_data, model)
    reg = ToySplineRegularization(f.pars, mu=mu_regularization)
    cons = ToySplineNonIntegralConstraints(model.pars, model.spline_basis)

    # rough initialization 
    f.pars['flux'].full[:] = 1000.
    f.pars['theta'].full[:] = 1.E-6
    
    f.pars['flux'].fix()
    x = minimize(f, f.pars.free, reg=reg, cons=cons)
    x = x[0]
    f.pars.free = x
    
    # release everybody and trash the fluxes a little 
    f.pars['flux'].release()
    f.pars['flux'].full[:] = 5000 + np.random.uniform(-1000, 1000, len(f.pars['flux'].full))
    x = minimize(f, f.pars.free, cons=cons, reg=reg, n_iter=1000)
    x = x[0]
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
        v = model(x, dp=xdata, jac=False)
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

    model = ToySplineModel(lc_data, grid_size=250) # phase_range=[lc_data.date.min(), lc_data.date.max()], grid_size=100)
    f = salt3.models.ModelResiduals(lc_data, model)
    
    jacobian, JJ = check_grad(model, model.pars.free)
    D = np.abs(jacobian-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
    J, JJ = check_grad(f, model.pars.free)
    D = np.abs(J-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)

    model.pars.free[:] += np.random.uniform(-1., 1., len(model.pars.free))
    J, JJ = check_grad(model, model.pars.free)
    D = np.abs(J-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
    J,JJ = check_grad(f, model.pars.free)
    D = np.abs(J-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)

    model.pars.full[:] += np.random.uniform(-1., 1., len(model.pars.full))
    J, JJ = check_grad(model, model.pars.free)
    D = np.abs(J-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
    J,JJ = check_grad(f, model.pars.free)
    D = np.abs(J-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)


# def test_toy1dsplinemodelfit_nr():
#     """
#     tests of the main (current) minimizer 
#     """
#     x_target = np.load(locate_test_datafile('test_toy1dsplinemodel_solution.npy'))
    
#     lc, f, cons, reg, x = main(N=1000, minimize=minimize_nr_var_quad,
#                                mu_regularization=500., plot=0, seed=0)
#     np.testing.assert_allclose(x_target, x, atol=1.E-6)
#     np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)    
    

def test_toy1dsplinemodelfit_nr_qr():
    """
    tests of the older minimizer : minimizer_nr_qr (when there are
    constraints, this one does not scale very well with the size of
    the parameter vector. Indeed, the sparsity of the Q,R
    decomposition is not guaranteed, even with sparse constraints).
    """
    x_target = np.load(locate_test_datafile('test_toy1dsplinemodel_solution.npy'))
    lc, f, cons, reg, x = main(N=1000, minimize=minimize_nr_qr, mu_regularization=500., plot=0, seed=0)
    np.testing.assert_allclose(x_target, x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)

    
def test_toy1dsplinemodelfit_nr_qr(datadir):
    """
    tests of the older minimizer : minimizer_nr_qr (when there are
    constraints, this one does not scale very well with the size of
    the parameter vector. Indeed, the sparsity of the Q,R
    decomposition is not guaranteed, even with sparse constraints).
    """
    x_target = np.load(locate_test_datafile('test_toy1dsplinemodel_solution.npy'))
    lc, f, cons, reg, x = main(N=1000, minimize=minimize_nr_qr, mu_regularization=500., plot=0, seed=0)
    np.testing.assert_allclose(x_target, x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)


    
if __name__ == '__main__':
    lc, f, cons, reg, x = main(N=1000, minimize=minimize_nr_var_quad, mu_regularization=500., plot=1)
