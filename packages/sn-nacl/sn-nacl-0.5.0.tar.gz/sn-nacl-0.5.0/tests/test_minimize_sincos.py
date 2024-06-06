import numpy as np
import scipy.sparse
import croaks
from saunerie.fitparameters import FitParameters
from salt3.minimizers import minimize_nr_var_quad, minimize_nr, minimize
import salt3.models

def gen_sincos(N=100, A=1., B=-0.2, omega_a=0.72, omega_b=0.52, ey=0.1,
               x=None, y=None, yerr=None, plot=False,
               seed=None):
    """
    Generate a dataset
    """

    if isinstance(seed, int):
        np.random.seed(seed)
        
    if x is None or y is None or yerr is None:
        x = np.random.uniform(-5., 5., N)
        y = A*np.sin(omega_a*x) + B*np.cos(omega_b*x)
        y += np.random.normal(scale=0.1, size=N)
        yerr = np.full(N, ey)

    if plot:
        import pylab as pl
        pl.figure()
        pl.errorbar(x, y, yerr=ey, ls='', color='b', marker='.')

    data = np.rec.fromarrays((x,y,yerr), names=['x', 'y', 'ey'])
    return croaks.DataProxy(data, wavelength='x', flux='y', flux_err='ey')


class SinCosToyModel():
    
    def __init__(self, data):
        self.dp = data
        self.pars = self.init_pars()
        
    def init_pars(self):
        fp = FitParameters([('A', 1), ('B', 1), ('omega_a', 1), ('omega_b')])
        return fp

    def __call__(self, p, dp=None, jac=False):
        """
        """
        self.pars.free = p
        
        if dp is None:
            dp = self.dp
        x,y,ey = dp.wavelength, dp.flux, dp.flux_err
        N = len(x)
        
        A = self.pars['A'].full[0]
        B = self.pars['B'].full[0]
        omega_a = self.pars['omega_a'].full[0]
        omega_b = self.pars['omega_b'].full[0]        
        
        v = A * np.sin(omega_a*x) + B * np.cos(omega_b*x)

        if jac:
            ia = np.arange(N)
            ja = np.full(N, 0)
            dfdA = np.sin(omega_a*x)
            
            ib = np.arange(N)
            jb = np.full(N, 1)
            dfdB = np.cos(omega_b*x)

            iom_a = np.arange(N)
            jom_a = np.full(N, 2)
            dfdom_a = A*x*np.cos(omega_a*x)

            iom_b = np.arange(N)
            jom_b = np.full(N, 3)
            dfdom_b = - B*x*np.sin(omega_b*x)
            
            i = np.hstack((ia,ib,iom_a, iom_b))
            j = np.hstack((ja,jb,jom_a, jom_b))
            data = -np.hstack((dfdA, dfdB, dfdom_a, dfdom_b)) / ey[i]
            idx = self.pars.indexof(j)>=0
            
            jacobian = scipy.sparse.coo_matrix((data[idx], (i[idx],j[idx])),
                                        shape=(N,4))
            
            return (y-v)/ey, jacobian

        return (y-v)/ey


class SinCosToyConstraints():
    """
    Constraints on the model parameters
    """
    def __init__(self, pars, vals=[1.2, 0.2]):
        self.pars = pars
        n = len(self.pars.full)
        i = [0, 1, 2, 3]
        j = [0, 0, 1, 1]
        v = [1, -1., 1, -1.]
        self.H = scipy.sparse.coo_matrix((v, (i,j)), shape=(n,2)).tocsr()
        self.d = self.vals = np.array(vals)
        
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


    
def main(A=1., B=-0.2, omega_a=0.72, omega_b=0.52,
         minimizer=minimize_nr,#_var_quad,
         plot=False, seed=0):
    """
    """
    dp = gen_sincos(A=A, B=B, omega_a=omega_a, omega_b=omega_b, seed=seed)
    f = SinCosToyModel(dp)
    ff = salt3.models.VarModelResiduals(dp, f)
    cons = SinCosToyConstraints(f.pars)
    x0 = np.array([10., 10., 0.8, 0.8])
    x = minimizer(ff, x0, cons=cons)
    if len(x) == 2:
        x = x[0]
    f.pars.free = x
    print(plot)
    if plot:
        import pylab as pl
        pl.ion()
        import matplotlib as mpl
        pl.figure()
        gs = mpl.gridspec.GridSpec(4,1)
        pl.subplot(gs[0:3,0])
        pl.errorbar(dp.wavelength, dp.flux, yerr=dp.flux_err, ls='', marker='.', color='b')
        xx = np.linspace(dp.wavelength.min(), dp.wavelength.max(), 100)
        xx.sort()
        ddp = gen_sincos(x=xx,
                         y=np.full(len(xx), 0),
                         yerr=np.full(len(xx), 1))
        v = f(x, dp=ddp)
        pl.plot(ddp.wavelength, -v, 'r-')
        pl.ylabel('y')
        
        pl.subplot(gs[3,0])
        pl.errorbar(dp.wavelength, f(x)*dp.flux, yerr=dp.flux_err, marker='.', ls='', color='b')
        pl.grid(1)
        pl.xlabel('x')
        pl.ylabel('res')
        pl.subplots_adjust(hspace=0.05)

    return dp, f, cons, x
    

def test_sincosfit_nr():
    # old target x_target = [0.99669018, -0.20330982,  0.72477005,  0.52477005]
    # first minimizer: minimize_nr : old result was x = [ 0.955678, -0.244322,  0.724236,  0.524236]
    # new minimize_nr_var_quad : x = [0.955678, -0.244322,  0.724236,  0.524236]
    dp, f, cons, x = main(A=1., B=-0.2, omega_a=0.72,
                          omega_b=0.52, minimizer=minimize_nr_var_quad,
                          plot=True, seed=1)
    np.testing.assert_allclose(np.array([0.99669018, -0.20330982,  0.72477005,  0.52477005]), x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)
    
    
def test_sincosfit_nr_qr():
    # another minimizer: minimize_nr_qr [does not scale well with parameter vector size]
    dp, f, cons, x = main(A=1., B=-0.2, omega_a=0.72, omega_b=0.52,
                          minimizer=minimize_nr_var_quad, plot=0, seed=1)
    np.testing.assert_allclose(np.array([ 0.99669018, -0.20330982,  0.72477005,  0.52477005]), x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)
    

if __name__ == "__main__":
    dp, f, cons, x = main(A=1., B=-0.2, omega_a=0.72, omega_b=0.52,
                          minimizer=minimize,#_nr_var_quad,
                          plot=1)
