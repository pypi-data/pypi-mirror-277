import os
import os.path as op
import numpy as np
import scipy.sparse
import saunerie
import croaks
from saunerie.fitparameters import FitParameters

from salt3.minimizers import minimize_nr_var_quad,minimize_nr
import salt3.generator
import salt3.models
import salt3.plots

from helpers import locate_test_datafile
from helpers import check_grad


class ToySplineModelFull():
    
    def __init__(self, dp, phase_range=[-100., 100.], grid_size=30):
        self.dp = dp
        self.nb_sn = len(dp.sn_set)
        self.spline_basis = saunerie.bspline.CardinalBSplineC(grid_size, phase_range)
        self.n_theta = grid_size
        self.pars = self.init_pars(dp)

        sn_index = dp.sn_index
        flx = self.pars['flux'].full[sn_index]
        tmax = self.pars['tmax'].full[sn_index]
        s = self.pars['s'].full[sn_index]   
        phases = (self.dp.date-tmax) / (1.+s)
        self.jacobian = self.spline_basis.eval(phases)
                
    def init_pars(self, dp):
        fp = FitParameters([('flux', self.nb_sn),
                            ('tmax', self.nb_sn),
                            ('s', self.nb_sn),
                            ("theta", len(self.spline_basis))])
        fp['flux'].full[:] = 1.
        fp['tmax'].full[:] = 0.
        fp['s'].full[:] = 0.
        fp['theta'].full[:] = 1.E-6
        return fp

    def __call__(self, p, jac=False, dp=None):
        """
        """
        self.pars.free = p

        if dp is None:
            dp = self.dp

        sn_index = dp.sn_index
        flx = self.pars['flux'].full[sn_index]
        tmax = self.pars['tmax'].full[sn_index]
        s = self.pars['s'].full[sn_index]        
        phases = (dp.date-tmax)  / (1.+s)
        
#        if dp is not None:
#            jacobian = self.spline_basis.eval(phases)
#        else:
#            jacobian = self.jacobian

        jacobian = self.spline_basis.eval(phases)

        v = flx * (jacobian @ self.pars['theta'].full)

        if jac:
            N = len(dp.nt)
            n = len(self.spline_basis)
            i = np.arange(N)

            # where are phases defined ?
            dB = self.spline_basis.deriv(phases)
            
            # dmodel_dflux 
            i_dm_dflux = i
            j_dm_dflux = self.pars['flux'].indexof(sn_index)
            v_dm_dflux = jacobian @ self.pars['theta'].full

            # dmodel_dtmax
            i_dm_dtmax = i
            j_dm_dtmax = self.pars['tmax'].indexof(sn_index)
            v_dm_dtmax = flx * (-1. / (1.+s)) * (dB @ self.pars['theta'].full)

            # dmodel_ds
            i_dm_ds = i
            j_dm_ds = self.pars['s'].indexof(sn_index)
            v_dm_ds = flx * (-(dp.date-tmax)/(1+s)**2) * (dB @ self.pars['theta'].full)

            # dmodel_dtheta
            i_dm_dtheta = jacobian.row
            j_dm_dtheta = self.pars['theta'].indexof(jacobian.col)
            v_dm_dtheta = self.pars['flux'].full[sn_index[jacobian.row]] * jacobian.data
            
            i = np.hstack((i_dm_dflux, i_dm_dtmax, i_dm_ds, i_dm_dtheta))
            j = np.hstack((j_dm_dflux, j_dm_dtmax, j_dm_ds, j_dm_dtheta))
            val = np.hstack((v_dm_dflux, v_dm_dtmax, v_dm_ds, v_dm_dtheta))
            
            idx_fix = np.where(j != -1)[0]
            DZ = scipy.sparse.coo_matrix((val[idx_fix], (i[idx_fix], j[idx_fix])), shape=(N, len(self.pars.free)))
            #            DZ.data /=  -dp.flux_err[DZ.row]
            
            # return (dp.flux-v)/flux_err, DZ
            return v, DZ
        
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
    

class ToySplineNonIntegralConstraints():
    """
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
        
    #    def __len__(self):
    #        return 2

    def get_rhs(self):
        return self.d
        
    def __call__(self, p, jac=False):
        self.pars.free = p
        v = -self.H.T @ self.pars.full + self.vals
        
        if jac:
            i = np.where(self.pars.indexof() >= 0)[0]
            return v, self.H[i,:].T
        return v

    
class ToySplineNonIntegralConstraintsFull():
    """
    .. note:: what if one of the constraints is invalid 
       because all corresponding parameters have been fixed ? 
    """
    def __init__(self, pars, basis, vals=[1., 0., 0.]):
        self.pars = pars
        self.basis = basis
        self.vals = self.d = np.array(vals)
        assert(len(self.d) == 3)
        
        n = len(self.pars.full)

        pp = pars.copy()
        pp.release()
        nsn = len(pp['flux'].full)
        
        # first constraint: S(0) = 1
        jacobian = self.basis.eval(np.array([0]))
        #        i1 = pars['theta'].indexof(jacobian.col)
        i1 = pp['theta'].indexof(jacobian.col)
        j1 = np.full(len(jacobian.col), 0)
        v1 = J.data.copy()
        # second constraint: S'(0) = 0
        Jp = self.basis.deriv(np.array([0]))
        #        i2 = pars['theta'].indexof(Jp.col)
        i2 = pp['theta'].indexof(Jp.col)        
        j2 = np.full(len(Jp.col), 1)
        v2 = Jp.data.copy()
        # third constraint: \sum_i s_i = 0
        i3 = pp['s'].indexof(np.arange(nsn))
        j3 = np.full(nsn, 2)
        v3 = np.full(nsn, 1)
        
        self.H = scipy.sparse.coo_matrix((np.hstack((v1,v2,v3)), (np.hstack((i1,i2,i3)), np.hstack((j1,j2,j3)))), shape=(n,3)).tocsr()
        
    #    def __len__(self):
    #        return 3

    def get_rhs(self):
        return self.d
    
    def __call__(self, p, jac=False):
        self.pars.free = p
        v = -self.H.T @ self.pars.full + self.vals
        if jac:
            i = np.where(self.pars.indexof() >= 0)[0]
            return v, self.H[i,:].T
        return v
    

def main(N=200, minimize=minimize_nr,#_var_quad,
         mu_regularization=500.,
         plot=False, seed=None):
    """
    """
    lc_data = salt3.generator.generate_lc(N, tmax_range=(0., 0.),
                                          sig_range=(0., 0.),
                                          norm_range=(1000., 1000.),
                                          seed=seed)

    model = ToySplineModelFull(lc_data, grid_size=250) # phase_range=[lc_data.date.min(), lc_data.date.max()], grid_size=100)
    f = salt3.models.VarModelResiduals(lc_data, model)
    reg = ToySplineRegularization(f.pars, mu=mu_regularization)
    cons = ToySplineNonIntegralConstraints(model.pars, model.spline_basis)
    cons_full = ToySplineNonIntegralConstraintsFull(model.pars, model.spline_basis)

    # initialization fit (spline parameters only)
    f.pars['flux'].full[:] = 1000
    f.pars['theta'].full[:] = 1.E-6
    f.pars['flux'].fix()
    f.pars['tmax'].fix()
    f.pars['s'].fix()
    x = minimize(f, f.pars.free, reg=reg, cons=cons)
    if len(x) == 2:
        x = x[0]
    f.pars.free = x

    # real fit, with all parameters free
    f.pars.release()
    f.pars['flux'].full[:] = 10000
    x = minimize(f, f.pars.free, cons=cons_full, reg=reg)
    if len(x) == 2:
        x = x[0]
    f.pars.free = x
    
    if plot:
        import pylab as pl
        pl.ion()
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
        v = model(f.pars.free, dp=xdata, jac=False)
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
        J = model.spline_basis.eval(xx)
        pl.plot(xx, J @ model.pars['theta'].full, 'r-')
        pl.xlabel('x')
        pl.ylabel('LC template (spline model only)')
        pl.grid(1)


        
    return lc_data, f, cons_full, reg, x


def test_model_derivatives(N=200, seed=0):
    """
    """
    lc_data = salt3.generator.generate_lc(N=N, tmax_range=(-70., 70.),
                                          sig_range=(-1., 1.),
                                          norm_range=(10., 1000.),
                                          seed=seed)

    model = ToySplineModelFull(lc_data, grid_size=250) # phase_range=[lc_data.date.min(), lc_data.date.max()], grid_size=100)
    f = salt3.models.ModelResiduals(lc_data, model)
    
    J, JJ = check_grad(model, model.pars.free)
    D = np.abs(J-JJ)
    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-8)
    
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

    # en revanche, celui la, il plante ... 
    #    model.pars.full[:] += np.random.uniform(-1., 1., len(model.pars.full))
    #    J, JJ = check_grad(model, model.pars.free)
    #    D = np.abs(J-JJ)
    #    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)
    
    #    J,JJ = check_grad(f, model.pars.free)
    #    D = np.abs(J-JJ)
    #    np.testing.assert_allclose(np.zeros_like(D), D, atol=1.E-6)

    
    
def test_1dsplinemodelfullfit_nr():
    x_target = np.load(locate_test_datafile('test_1dsplinemodel_solution.npy'))
    lc, f, cons, reg, x = main(N=1000, minimize=minimize_nr,#_var_quad,
                               mu_regularization=10,
                               plot=0, seed=0)
    np.testing.assert_allclose(x_target, x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)    
    

if __name__ == "__main__":
    lc, f, cons, reg, x = main(N=1000, minimize=minimize_nr,#_var_quad,
                               mu_regularization=10., plot=True)
    
