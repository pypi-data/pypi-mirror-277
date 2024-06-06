import numpy as np
import scipy.sparse
import croaks
from saunerie.fitparameters import FitParameters
from salt3.minimizers import minimize_nr_var_quad, minimize_nr
import salt3.models


def gen_c1poly(N=100, a=-0.1, b=-0.2, c=1.2, d=-0.2, e=1.2, ey=0.1,
               seed=None):
    """
    Generate a test dataset
    """

    if isinstance(seed, int):
        np.random.seed(seed)
    
    x = np.random.uniform(-10, 10., N)
    y = np.zeros(N)
    idx = x<0.
    y[idx] = a*x[idx]**2 + b*x[idx] + c
    idx = x>=0.
    y[idx] = d*x[idx] + e
    y += np.random.normal(scale=ey, size=N)
    ret = np.rec.fromarrays((x,y,np.full(N, ey)), names=['x', 'y', 'ey'])
    ret = croaks.DataProxy(ret, flux = 'y', wavelength = 'x', flux_err = 'ey')
    return ret


class C1PolyResiduals():
    
    def __init__(self, data):
        self.data = data.nt
        self.pars = FitParameters([('p1', 3), ('p2', 2)])
        
    def __call__(self, p, jac=False):
        self.pars.free = p
        a,b,c = self.pars['p1'].full
        d,e = self.pars['p2'].full
        x,y,ey = self.data['x'], self.data['y'], self.data['ey']
        N = len(x)
        v = np.zeros(N)

        idx = x<0
        v[idx] = a*x[idx]**2 + b*x[idx] + c
        idx = x>=0
        v[idx] = d*x[idx] + e
        o = np.ones(N)
        
        if jac:
            i = np.tile(np.arange(N), 5)
            j = np.repeat(np.arange(5), N)
            d = np.vstack((x**2/ey, x/ey, o/ey, x/ey, o/ey)).T
            idx = d[:,1]<0
            ii = np.where(idx)[0]
            d[ii, 3] = d[ii, 4] = 0.
            idx = d[:,1]>=0
            ii = np.where(idx)[0]
            d[ii,0] = d[ii,1] = d[ii,2] = 0
            jacobian = scipy.sparse.coo_matrix((-d.T.flatten(), (i,j)), shape=(N,5))
        
            return (y-v)/ey, jacobian

        return (y-v)/ey

    
class C1PolyConstraints():
    
    def __init__(self, pars):
        """
        """
        self.pars = pars # .copy()
        self.pars_free = pars.copy()
        self.pars_free.release()
        n = len(self.pars.full)
        i = [2,   4,  1,   3]
        j = [0,   0,  1,   1]
        v = [1., -1., 1., -1.]
        self.H = scipy.sparse.coo_matrix((v, (i,j)), shape=(n, 2)).T
        self.d = self.vals = np.array([0., 0.])
        
    #    def __len__(self):
    #        return 2

    def get_rhs(self):
        return self.d
    
    def __call__(self, p, jac=False):
        """
        """
        self.pars.free = p
        self.pars_free.full[:] = self.pars.full[:]

        # the constraint class return the delta with the target value 
        v = -self.H @ self.pars.full + self.vals
        
        if jac:
            return v, self.H
        return v        

    
class C1PolyRegz():
    """
    This one is not constraint free
    """
    def __init__(self, pars, mu=1.E-6):
        self.pars = pars
        d = np.full(5, mu)
        self.P = scipy.sparse.dia_matrix((d, [0]), shape=(5,5))
        print(self.P.todense())
        
    def __call__(self, p):
        self.pars.free = p
        v = self.pars.full.T.dot(self.P.dot(self.pars.full))
        return v, self.P


def main(N=100, plot=False, minimizer=minimize_nr_var_quad, **kw):
    """
    """
    
    data = gen_c1poly(N=N, **kw)
    m = C1PolyResiduals(data)
    cons = C1PolyConstraints(m.pars)
    regz = C1PolyRegz(m.pars, mu=1.E-8)
    f = salt3.models.VarModelResiduals(data, m)
    x = minimizer(f, m.pars.free, cons = cons, reg = regz)    

    if plot:
        import pylab as pl
        data = data.nt
        pl.figure()
        pl.errorbar(data['x'], data['y'], yerr=data['ey'], ls='', marker='.', color='b')
        d = np.rec.fromarrays((np.linspace(-10., 10, 500),
                               np.zeros(500),
                               np.ones(500)), names=['x', 'y', 'ey'])
        d = croaks.DataProxy(d, flux = 'y', wavelength = 'x', flux_err = 'ey')
        mm = C1PolyResiduals(d)
        v = mm(x[0])
        pl.plot(d.nt['x'], -v, 'r-')
        pl.xlabel('x')
        pl.ylabel('y')
    if len(x) == 2:
        x = x[0]
    return data, m, cons, x
    

def test_c1polyfit_nr():
    dp, f, cons, x = main(minimizer=minimize_nr_var_quad,
                          plot=0, seed=0)
    np.testing.assert_allclose(np.array([-0.10092981, -0.2041651 ,  1.23490678, -0.2041651 ,  1.23490678]), x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)

    
def test_c1polyfit_nr_qr():
    dp, f, cons, x = main(minimizer=minimize_nr_var_quad, plot=0, seed=0)
    np.testing.assert_allclose(np.array([-0.10092981, -0.2041651 ,  1.23490678, -0.2041651 ,  1.23490678]), x, atol=1.E-6)
    np.testing.assert_allclose(np.zeros_like(cons(x, jac=False)), cons(x, jac=False), atol=1.E-8)

    
if __name__ == "__main__":
    dp, f, cons, x = main(minimizer=minimize_nr_var_quad, plot=1)
