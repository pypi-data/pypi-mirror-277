import numpy as np
import scipy
import matplotlib.pyplot as pl
pl.ion()
from astropy.io import fits as pf
from scipy.sparse import coo_matrix, dia_matrix, dok_matrix, diags
from scipy.optimize import leastsq, fmin_ncg, check_grad, approx_fprime
from saunerie.lsqfit import Chi2
from saunerie.fitparameters import FitParameters
from saunerie.bspline import BSpline, CardinalBSplineC, integ
from croaks import NTuple
from numpy.polynomial.legendre import leggauss
from sksparse.cholmod import cholesky, cholesky_AAt
from saunerie import optim, plottools
from scipy.integrate import quad
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)
from astropy.modeling import models, fitting
from scipy.integrate import simps

# The model y is a linear function of x.
# In all this file, we define differents models for a variance. The variance may either be define as a polynomial function of x or as a linear function of f(x), f is a linear function of x.
# There are four different type of variance : 3 polynomial function each labeled by the degre of the polynome n_gamma, it can be 1 (constant) , 2 (linear) or 4.
# The fourth one, is where the variance depends linearly of f(x), in the following it will be labelled by n_gamma = 'dep'  


# coefficient are define as follow :
# y = 1.235 * x + 9.123

# variance models :
  # polynomial function of x:
     # n_gamma = 2 :  var = 1.356
     # n_gamma = 2 :  var = 1.356 * x + 2.222
     # n_gamma = 4 :  var = 1/30. * (x**3 - 19. * x**2 + 133. * x + 229.)
  # linear function of f(x) :
     # n_gamma = 'dep' : var = 0.01 * f(x) + 0.005 

def variance(x, n):
    """
    create the "n" variance describes by the code just above.
    
    Input : - x = Array, argument of the variance function, it may be x (if n == &, 2 or 4) or y (if n == 'dep').
            - n = 1, 2, 4 or 'dep', code of the variance we want to create.
    
    Output : Array, the variance wanted.
    """
    if n == 1:
        return 1.356 * np.ones(x.shape)
    elif n == 2:
        return 1.325*x + 2.2222
    elif n == 4:
        return 1/30.*(x**3 - 19.*x**2 + 133.*x + 229.)
    elif n == 'dep':
        return 0.01 * x + 0.005
    
    
def gen_var(N, ng, a = 1.235, b = 9.123):
    """
    return the definition interval of the function, the linear function and the variance.
    
    Input : - N = int, number of points of the definition interval.
            - ng = 1, 2, 4, 'dep', the n_gamma.
            - a = float, the slope of the function.
            - b = float, the intercept.
    
    Output : - x = array(N), the definition interval.
             - y = array(N), linear function.
             - var = array(N), variance at each point.
    """
    x = np.linspace(1,10,N)
    mod = a * x + b
    if ng == 'dep':
        var = variance(mod, ng)
    else :
        var = variance(x, ng)
    n = []
    for i in range(N):
        n.append(np.random.normal(0, np.sqrt(np.abs(var[i])), 1)[0])
    n = np.array(n)
    y = a * x + b + n
    return x, y, var



class SModel(object):
    """
    definition of a new classe, a linear function : y = \alpha * x + \beta
    parameters are alpha and beta.
    """
    def __init__(self, x):
        self.nb_sn = 1 
        self.xdata = x
        self.pars = self.para_init()

    def para_init(self):
        fp = [("alpha", self.nb_sn), ("beta", self.nb_sn)]
        fp = FitParameters(fp)
        fp['alpha'] = 1.#1.235 
        fp['beta'] = 10. #9.123 
        return fp


    def __call__(self, p, jac=False, xdata=None):
        if xdata is None:
            xdata = self.xdata
        self.pars.free = p
        v = p[0] * xdata + p[1]
        if jac:
            N = len(xdata)

            # derivatives wrt alpha:
            ii_a = np.zeros((N))
            jj_a = np.arange(0,N)
            val_a = xdata

            # derivatives wrt Beta:
            ii_b = np.ones((N))
            jj_b = np.arange(0,N)
            val_b = np.ones((len(xdata)))

            i = np.hstack((ii_a, ii_b))
            j = np.hstack((jj_a, jj_b))
            val_jac = np.hstack((val_a, val_b))
            idx_fix = np.where(j != -1)
            Jac = coo_matrix((val_jac[idx_fix], (i[idx_fix],j[idx_fix])), shape = (len(self.pars.free),N))
            return  v , Jac.T
        else :
            return v

# This file has been written in a way such that the two variance model, the one depending on x and the one depening on f(x), are separated.
# They have their own class model and their own minimization fuction.
# To sinthetize :
   # polynomial function of x : - model : WModel
   #                            - minimization function : fit_sqp_lin
   #
   # linear function of f(x) : - model : WdepModel
   #                           - minimization function : fit_lin_var
# They are not the same, model return different element, one is the inverse of the other, and functions do not take exactly same inputs.

        
class WModel(object):
    """
    Model for a polynomial dependance of x for the variance.
    """
    def __init__(self, x, n):
        self.xdata = x
        self.n_g = n                                                                                                                                                                           
        self.pars = self.para_init()

    def para_init(self):
        if self.n_g == 4:
            fp = [("gamma3", 1), ("gamma2", 1), ("gamma1", 1), ("gamma0", 1)]
            fp = FitParameters(fp)
            fp['gamma3'] = 1./35.
            fp['gamma2'] = -0.63
            fp['gamma1'] = 4.43
            fp['gamma0'] = 7.63
            return fp

        elif self.n_g == 1:
            fp = [("gamma0", 1)]
            fp = FitParameters(fp)
            fp['gamma0'] = 1.5
            return fp
        
        elif self.n_g == 2:
            fp = [("gamma1", 1), ("gamma0", 1)]
            fp = FitParameters(fp)
            fp['gamma1'] = 1.5
            fp['gamma0'] = 2.
            2
            return fp

    def __call__(self, p):
        """
        return the matrix of the inverse of the variance on the diagonal.
        
        Inputs : - p = Array, parameters of the model.
        
        Output : - Array, 1/V equivalent of the matrix w.
        """
        if len(p) == 4:
            return np.diag(1/(p[3] + p[2] * self.xdata + p[1] * self.xdata**2 + p[0] * self.xdata**3))
        elif len(p) == 1:
            return np.diag(1/(p[0]*np.ones(self.xdata.shape)))
        elif len(p) == 2:
            return np.diag(1/(p[1] + p[0] * self.xdata))

# minimization function of the polynomial dependance

def fit_sqp_lin(y, x, variance, n_gamma = 2, max_iter = 100, ll = 0.1, dchi2_min = 0.1, reml = False, plot = True):
    """
    Minimization of the chi2.

    Inputs : - y = Array, the f(x) values.
            - x = Array, the definition interval.
            - variance = Array, the variance considered.
            - n_gamma = 1, 2, 4, degree of the polynome
            - max_iter = int, is the maximum number of iteration wanted.
            - ll = float, help to inverse the hessian matrix, by adding somthing one its diagonal.
            - dchi2_min = float, variation of chi2 desired to reach.
            - reml = bool, to consider the reml technic, NOT use here !
            - plot = bool, True will plot.

    Outputs : - p = Array, the final parameter of the linear model.
             - g  = Array, the final parameter of the variance model.
             - model = SModel, model of the straight line.  
             - var_model = WModel, model of the variance.
    """
    model = SModel(x)
    var_model = WModel(x, n = n_gamma)
    
    p = model.pars.free
    g = var_model.pars.free
    print(g)
    dp = np.zeros(p.shape)
    dg = np.zeros(g.shape)

    v, J = model(p, jac = True)
    w = var_model(g)

    res = y - v 
    
    chi2 = (np.linalg.multi_dot([res.T,w,res]).sum() )/ (len(y) - (p.shape[0] + g.shape[0]))#+ np.log(np.linalg.det(w))

    Dchi = 0.
    niter = 0
    
    while niter < max_iter:
        v, J = model(p, jac = True)
        w = var_model(g)

        res = y - v
        H = 2 * np.linalg.multi_dot([J.toarray().T, w, J.toarray()]) + ll * diags(np.ones(J.shape[1]))

        def construction(H = H, res = res, J = J, n_gamma = n_gamma, g = g ,reml = reml):
            """    
            Create Hessian matrix and the gradient vector needed to minimized the chi2, in order to fit models of the straight line and variances on data, using Newton-Raphson's method.
            """
            H = coo_matrix(H)
            H00 = H.data
            i00 = H.row
            j00 = H.col

            if n_gamma == 1 :
                H11 = (w.dot(w) * (2*g)**2).trace()
                i11 = p.shape[0] + n_gamma - 1
                j11 = p.shape[0] + n_gamma - 1

                val = np.hstack((H00, H11))
                i = np.hstack((i00, i11)) 
                j = np.hstack((j00, j11))
                H_l = coo_matrix((val, (i,j)), shape = (p.shape[0] + n_gamma, p.shape[0] + n_gamma))
            
                resul = np.hstack((2 * np.linalg.multi_dot([J.toarray().T, w,res]), 2*g*(np.linalg.multi_dot([res.T, w**2, res]) - w.trace())))
                return H_l, resul


            elif n_gamma == 2:
                X = np.diag(x)

                dev1 = 2 * (g[0] * X**2 + g[1] * X)
                dev0 = 2 * (g[0] * X + g[1]) 
                
                H11 = (np.linalg.multi_dot([w, dev1, w, dev1]).trace()) 
                i11 = [2]
                j11 = [2]
                
                H12 = np.linalg.multi_dot([w, dev1, w, dev0]).trace()
                i12 = [2]
                j12 = [3]

                H21 = np.linalg.multi_dot([w, dev0, w, dev1]).trace()
                i21 = [3]
                j21 = [2]
                
                H22 = np.linalg.multi_dot([w, dev0, w, dev0]).trace()
                i22 = [3]
                j22 = [3]


                val = np.hstack((H00, H11, H12, H21, H22))
                i = np.hstack((i00, i11, i12, i21, i22)) 
                j = np.hstack((j00, j11, j12, j21, j22)) 
                H_l = coo_matrix((val, (i,j)), shape = (p.shape[0] + n_gamma, p.shape[0] + n_gamma))

                resul = np.hstack((2 * np.linalg.multi_dot([J.toarray().T, w, res]), np.linalg.multi_dot([res.T, w, dev1, w, res]) - (w).dot(dev1).trace(), np.linalg.multi_dot([res.T, w, dev0, w, res]) - (w).dot(dev0).trace()))
                return H_l, resul
                    
            elif n_gamma == 4:
                X = np.diag(x)

                dev3 = 2 * ( g[0] * X**6 + g[1] * X**5 +  g[2] * X**4 + g[3] * X**3)
                dev2 = 2 * ( g[0] * X**5 + g[1] * X**4 +  g[2] * X**3 + g[3] * X**2)
                dev1 = 2 * ( g[0] * X**4 + g[1] * X**3 +  g[2] * X**2 + g[3] * X)
                dev0 = 2 * ( g[0] * X**3 + g[1] * X**2 +  g[2] * X + g[3])
                
                H11 = (np.linalg.multi_dot([w, dev3, w, dev3]).trace())
                i11 = [2]
                j11 = [2]
                
                H12 = np.linalg.multi_dot([w, dev3, w, dev2]).trace()
                i12 = [2]
                j12 = [3]

                H13 = np.linalg.multi_dot([w, dev3, w, dev1]).trace()
                i13 = [2]
                j13 = [4]

                H14 = np.linalg.multi_dot([w, dev3, w, dev0]).trace()
                i14 = [2]
                j14 = [4]
                
                H21 = np.linalg.multi_dot([w, dev2, w, dev3]).trace()
                i21 = [3]
                j21 = [2]

                H22 = np.linalg.multi_dot([w, dev2, w, dev2]).trace()
                i22 = [3]
                j22 = [3]

                H23 = np.linalg.multi_dot([w, dev2, w, dev1]).trace()
                i23 = [3]
                j23 = [4]

                H24 = np.linalg.multi_dot([w, dev2, w, dev0]).trace()
                i24 = [3]
                j24 = [5]

                H31 = np.linalg.multi_dot([w, dev1, w, dev3]).trace()
                i31 = [4]
                j31 = [2]

                H32 = np.linalg.multi_dot([w, dev1, w, dev2]).trace()
                i32 = [4]
                j32 = [3]
		
                H33 = np.linalg.multi_dot([w, dev1, w, dev1]).trace()
                i33 = [4]
                j33 = [4]

                H34 = np.linalg.multi_dot([w, dev1, w, dev0]).trace()
                i34 = [4]
                j34 = [5]

                H41 = np.linalg.multi_dot([w, dev0, w, dev3]).trace()
                i41 = [5]
                j41 = [2]
                
                H42 = np.linalg.multi_dot([w, dev0, w, dev2]).trace()
                i42 = [5]
                j42 = [3]
		
                H43 = np.linalg.multi_dot([w, dev0, w, dev1]).trace()
                i43 = [5]
                j43 = [4]

                H44 = np.linalg.multi_dot([w, dev0, w, dev0]).trace()
                i44 = [5]
                j44 = [5]
                

                val = np.hstack((H00, H11, H12, H13, H14, H21, H22, H23, H24, H31, H32, H33, H34, H41, H42, H43, H44))
                i = np.hstack((i00, i11, i12, i13, i14, i21, i22, i23, i24, i31, i32, i33, i34, i41, i42, i43, i44))
                j = np.hstack((j00, j11, j12, j13, j14, j21, j22, j23, j24, j31, j32, j33, j34, j41, j42, j43, j44))
                H_l = coo_matrix((val, (i,j)), shape = (p.shape[0] + n_gamma, p.shape[0] + n_gamma))

                resul = np.hstack((2 * np.linalg.multi_dot([J.toarray().T, w, res]), np.linalg.multi_dot([res.T, w, dev3, w, res]) - (w).dot(dev3).trace(), np.linalg.multi_dot([res.T, w, dev2, w, res]) - (w).dot(dev2).trace(), np.linalg.multi_dot([res.T, w, dev1, w, res]) - (w).dot(dev1).trace(), np.linalg.multi_dot([res.T, w, dev0, w, res]) - (w).dot(dev0).trace()))

                return H_l, resul


        H_l, resul = construction(H = H, J = J, n_gamma = n_gamma, g = g, reml = reml)
        var = np.linalg.inv(H_l.toarray()).dot(resul)
        dp = var[:p.shape[0]]
        dg = var[p.shape[0]:]

        
        # Here are the two ways of implementing the line search : the first one, only on the light cures parameters & the second on both models parameters.
        # One can comment or decomment the wanted fonction phi and crit.
        
        def phi(p):
            return ((w * ( y - model(p, jac = False)))**2).sum()

        def crit(t):
            return phi(p + t * dp)

        vect = np.hstack((p,g))
        """
        def phi(vect, n = len(p)):
            p = vect[:n]
            g = vect[n:]
            val = model(p)
            V = var_model(val, g)
            variance = np.diag(V) #+ np.diag(sig**2)
            w = variance
            return ((w * ( y - val))**2).sum()

        def crit(t):
            return phi(vect + t * var)
        """
        t, fval, ni, funcalls = scipy.optimize.brent(crit, brack=(0,1), full_output=True)

        p = p + t * dp
        g = g + t * dg
        print(p, dp, g, dg)
        v = model(p, jac=False)
        w = var_model(g)                
        res = w * (y- v)

        new_chi2 = (np.log(2 * np.pi) * len(res)  + (res**2).sum())  / (len(y) - (p.shape[0] + g.shape[0])) #+ np.log(np.linalg.det(w))
            
        dchi2 = new_chi2 - chi2
        logging.info(' red chi2: %f -> %f [dchi2=%f]' % (chi2, new_chi2, dchi2))

        chi2 = new_chi2
        if niter >= 1 :
            if dchi2 > 0.:
                logging.info('increasing chi2 !')
                niter += 1
                continue #break

            if abs(dchi2) <= dchi2_min:
                logging.info('dchi2 < dchi2_min, exiting')
                niter += 1
                break#continue

            if niter > max_iter:
                break

        niter += 1

    if plot :
        pl.figure()
        pl.plot(x,y, 'k.')
        
        pl.errorbar(x, p[0] * x + p[1], yerr = np.sqrt(variance), ls = '--', color='r', linewidth = 2, label = 'real')
        if n_gamma == 1:
            pl.errorbar(x, p[0] * x + p[1], yerr = np.sqrt(g[0]), ls = '-.', color='b', label='simu')
            pl.text(6,11, ' n_iter : %i (dchi< %f) \n\n p0 : %f, p1: %f \n g0 : %f' % (niter,dchi2_min,p[0],p[1],g[0]), fontsize= 15)
        if n_gamma == 2:
            pl.errorbar(x, p[0] * x + p[1], yerr = np.sqrt(g[0] * x + g[1]), ls = '-.', color='b', label='simu')
            pl.text(6,12, ' n_iter : %i (dchi< %f) \n\n p0 : %f, p1: %f \n g0 : %f, g1: %f' % (niter,dchi2_min,p[0],p[1],g[0],g[1]), fontsize= 15)
        if n_gamma == 4:
            pl.errorbar(x, p[0] * x + p[1], yerr = np.sqrt(g[0] * x**3 + g[1] * x**2 + g[2] * x + g[3]), ls = '-.', color='b', label='simu')
            pl.text(6,12, ' n_iter : %i (dchi< %f) \n\n p0 : %f, p1: %f \n g0 : %f, g1: %f, g2 : %f, g3: %f' % (niter,dchi2_min,p[0],p[1],g[0],g[1],g[2],g[3]), fontsize= 15)
        pl.legend()
    return p, g, model, var_model



class WdepModel(object):
    """
    Model for a polynomial dependance of f(x) for the variance.
    """
    def __init__(self, x):
        self.xdata = x
        self.pars = self.para_init()

    def para_init(self):
        fp = [("gamma0", 1), ("gamma1", 1)]
        fp = FitParameters(fp)
        fp['gamma0'] = 0.015
        fp['gamma1'] = 0.0045
        return fp
    
    def __call__(self, pvar, pmod, J = None):
        """
        return the matrix of the variance on the diagonal.

        Inputs : - pvar = Array, parameters of the variance model.
                 - pmod = Array, parameters of the straight line model.

        Output : - variance model evaluate with teh new parameters
                 - if J is given : dV = coo_matrix, the jacobian of the variance model.
        """

        value = pmod[0]*self.xdata + pmod[1]
        if J == None:
            return pvar[0] * value + pvar[1]
        else :
            N = len(pvar) + len(pmod)
            n = len(value)

            # derive parametre de J:                                                                                                                                                     
            ii_J = J.col
            jj_J = J.row
            val_J = value[J.row] * J.data * pvar[0]

            # derive V_{0}:                                                                                                                                                              
            ii_v = (J.shape[1] ) * np.ones(value.shape)
            jj_v = range(n)
            val_v = value

            # derive V_{1}:
            ii_v1 = (J.shape[1] + 1) * np.ones(value.shape)
            jj_v1 = range(n)
            val_v1 = np.ones(value.shape)

            i = np.hstack((ii_J, ii_v, ii_v1))
            j = np.hstack((jj_J, jj_v, jj_v1))
            val_jac = np.hstack((val_J, val_v, val_v1))

            dV = coo_matrix((val_jac, (i,j)), shape = (N, n))
            return pvar[0] * value + pvar[1], dV




def hessian(x, w, p, g, J, dV):
    """                                                                                                                                                                                                       
    Create Hessian matrix needed to minimized the chi2, in order to fit models of straight line and variances on data, using Newton-Raphson's method.                                                             
    Appearing on the left hand side of the equation.

    Input : - x = Array, is defition interval of the function. 
            - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(x) * len(x)).
            - p = Array, is the parameter of the STRAIGHT LINE model.
            - g = Array, is the parameter of the VARIANCE model.
            - J = coo_matrix, is the Jacobian of the straight line model.
            - dV = coo_matrix, is the Jacobian of the variance model.

    Output : - H = coo_matrix, sparse hessian matrix.
    """
    H0 = 2 * J.T * w * J
    H = coo_matrix(H0)
    H00 = H.data
    i00 = H.row
    j00 = H.col

    def trace(i, j, w = w, dV = dV):
        dV = dV.toarray()
        dVi = coo_matrix(np.diag(dV[i]))
        dVj = coo_matrix(np.diag(dV[j]))
        return (w * dVi * w * dVj).toarray().trace() 

    npar = p.shape[0] + g.shape[0]
    Tr = np.array([trace(i,j) for i in range(npar) for j in range(i, npar)])
    ii = [i for i in range(npar) for j in range(i, npar)]
    jj = [j for i in range(npar) for j in range(i, npar)]
    #tr = coo_matrix((Tr,(ii,jj)),shape = (npar, npar))                                                                                                                                                    
    #H_l = tr + tr.T - np.diag(tr.toarray().diagonal())                                                                                                                                                    
    H_l = coo_matrix((np.hstack((Tr,Tr)), (np.hstack((ii,jj)), np.hstack((jj, ii)))), shape = ( npar, npar))
    H_l = coo_matrix((np.hstack((H_l.data, -np.diag(H_l.toarray())/2.)), (np.hstack((H_l.row, range(H_l.toarray().shape[0]))), np.hstack((H_l.col, range(H_l.toarray().shape[0]))))), shape = (npar,npar))
    H = coo_matrix((H00, (i00, j00)), shape = ( npar, npar))
    return H + H_l

def grad(res, w, J, dV, p, g):
    """
    Create gradient vector needed to minimized the chi2, in order to fit models of straight line and variances on data, using Newton-Raphson's method.
    Appearing on the right hand side of the equation.

    Input : - res = Array, is the residual of the measurement substracted by the model.
            - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(res) * len(res)).
            - J = coo_matrix, is the Jacobian of the linear model.                                                                                                                                            
            - dV = coo_matrix, is the Jacobian of the variance model.
            - p = Array, is the parameter of the straight line model.
            - g = Array, is the parameter of the VARIANCE model.

    Output : - (-1) * resul = Array, the needed gradient vector.
    """
    def grad_theta(i, J = J, res = res, dV = dV, w = w):
        """
        Calculate the term i of the gradient vector.

        Input : - i = int, represent the i-th parameter term of the gradient.
        
        Output : - Float, the ith term
        """
        grad = (w.toarray().dot(np.diag(dV.toarray()[i]))).trace() - np.linalg.multi_dot([res.T, w.toarray(), np.diag(dV.toarray()[i]), w.toarray(), res])
        if i < p.shape[0]:
            grad += - 2 * np.linalg.multi_dot([J.toarray().T[i], w.toarray(), res])
        return grad
    resul = np.array([grad_theta(i) for i in range(p.shape[0] + g.shape[0])])
    return -resul

        
def fit_lin_var(N, max_iter = 100, ll = 0.1, dchi2_min = 0.1, plot = True):
    """
    Minimization of the chi2.

    Inputs :- N = int, number of point for the function.  
            - max_iter = int, is the maximum number of iteration wanted.
            - ll = float, help to inverse the hessian matrix, by adding somthing one its diagonal.
            - dchi2_min = float, variation of chi2 desired to reach.
            - plot = bool, True will plot.

    Outputs : - p = Array, the final parameter of the linear model.
             - g  = Array, the final parameter of the variance model.
    """
    x, y, vari = gen_var(N = N, ng = 'dep')
    model = SModel(x)
    var_model = WdepModel(x)

    p = model.pars.free
    g = var_model.pars.free
    dp = np.zeros(p.shape)
    dg = np.zeros(g.shape)

    v, J = model(p, jac = True)
    V, dV = var_model(g, p, J=J)
    w = np.diag(1/V) #+ np.diag((1/vari))
    
    res = y - v
    chi2 = (np.linalg.multi_dot([res.T,w,res]) + len(res) * np.log(np.pi) + np.log(np.diag(w)).sum()) / (N - 4)
    Dchi = 0.
    niter = 0

    while niter < max_iter:
        v, J = model(p, jac = True)
        V, dV = var_model(g, p, J=J)
        w = coo_matrix(np.diag(1/V)) #+ np.diag((1/vari)))

        res = y - v
        H = hessian(x = x, w = w, p = p, g = g, J = J, dV = dV) + ll * diags(np.ones(p.shape[0]+ g.shape[0]))
        resul = grad(res = res, w = w, J = J, dV = dV, p = p, g = g)
        var = np.linalg.inv(H.toarray()).dot(resul)
        dp = var[:p.shape[0]]
        dg = var[p.shape[0]:]
        
        vect = np.hstack((p,g))

        # Here are the two ways of implementing the line search : the first one, only on the straight line parameters & the second on both models parameters.
        # One can comment or decomment the wanted fonction phi and crit.
        
        def phi(p):
            return ((w * ( y - model(p, jac = False)))**2).sum()

        def crit(t):
            return phi(p + t * dp)

        """
        def phi(vect, n = p.shape[0]):
            p = vect[:n]
            g = vect[n:]
            val = model(p, jac = False)
            
            V = var_model(g, p)
            #V = var_model(val, g)
            #variance = np.diag(V) #+ np.diag(sig**2)
            #w = np.linalg.inv(variance)
            w = np.diag(1/V) 
            return ((w * ( y - val))**2).sum()

        def crit(t):
            return phi(vect + t * var)
        """

        t, fval, ni, funcalls = scipy.optimize.brent(crit, brack=(0,1), full_output=True)

        
        p = p + t * dp
        g = g + t * dg
        
        print('p', p, '\n', 'dp', dp, '\n', 'g', g, '\n', 'dg', dg,'\n', 't', t, '\n')

        v = model(p, jac=False)
        V = var_model(g, p)
        res = y - v
        w = np.diag(1/V) 
        new_chi2 = (np.linalg.multi_dot([res.T,w,res]) + len(res) * np.log(np.pi) + np.log(np.diag(w)).sum()) /	(N - 4)
        dchi2 = new_chi2 - chi2
        logging.info('iter %f : red chi2: %f -> %f [dchi2=%f]' % (niter, chi2, new_chi2, dchi2))

        chi2 = new_chi2
        if niter >= 1 :
            if dchi2 > 0.:
                logging.info('increasing chi2 !')
                niter += 1
                continue

            if abs(dchi2) <= dchi2_min:
                logging.info('dchi2 < dchi2_min, exiting')
                niter += 1
                break

            if niter > max_iter:
                break

        niter += 1
    if plot:
        pl.figure()
        pl.plot(x, y, color = 'k', marker = '.', ls ='')
        pl.errorbar(x, p[0] * x + p[1], yerr = np.sqrt(vari), ls = '--', color='r', linewidth = 2, label='real')
        pl.errorbar(x, p[0] * x + p[1], yerr = np.sqrt(g[0] * (p[0] * x + p[1]) + g[1]), ls = '-.', color='b', label = 'simu')
        pl.title('N : %i' % (N))
        pl.legend()
        pl.text(6,12, ' n_iter : %i (dchi< %f) \n\n p0 : %f, p1: %f \n g0 : %f, g1: %f' % (niter,dchi2_min,p[0],p[1],g[0],g[1]), fontsize= 15)
    return p, g



def control(N, n_gamma, npts = 100, max_iter = 100, dchi2_min = 0.00001, dbin = 0.001, plot = True ):
    """                                                                                                                                                                                                           
    Control plot : histogram of the variance parameters for found for all the N realisations.

    Input : - N  = int, number of realisation of the fit.
            - n_gamma = 1, 2, 4 or 'dep', model of the variance.
            - npts = int, number of points.
            - max_iter = int, is the maximum number of iteration wanted.
            - dchi2_ min = dchi2_min = float, variation of chi2 desired to reach.
            - dbin = float, interval of histograms binning
            - plot = bool, True if we want to see each plot of the fit function.

    Output : - histogram
             - coef = array, parameters of each straight line model fitted.
             - gammas = array, parameters of each variance model fitted.
    """
    coef = np.zeros((N,2))
    if type(n_gamma) == int : 
        gammas = np.zeros((N, n_gamma))
        for i in range(N):
            x, y, var = gen_var(N = npts, ng = n_gamma)
            c, g, v, vm = fit_sqp_lin(y, x, var, n_gamma = n_gamma, max_iter = max_iter, dchi2_min = dchi2_min, plot = False)
            coef[i] = c
            gammas[i] = g

    elif n_gamma == 'dep':
        gammas = np.zeros((N, 2))
        for i in range(N):
            c, g = fit_lin_var(N = npts, max_iter = max_iter, ll = 0.1, dchi2_min = dchi2_min, plot = False)
            coef[i] = c
            gammas[i] = g

    a = 1.235
    b = 9.123

    if plot :
        pl.figure()
        xx, yy = np.histogram(coef.T[0])
        rg = (yy.min(), yy.max())
        nbins = int((rg[1] - rg[0])/ dbin)
        xh, yh, hh = pl.hist(coef.T[0], bins = nbins)#, range = (a-1,a+1))
        med = np.median(coef.T[0])
        moy = coef.T[0].mean()
        pl.plot(a*np.ones((10)), np.linspace(0, xh.max(), 10), 'r--')
        pl.plot(med * np.ones((10)), np.linspace(0, xh.max(), 10), 'b--')
        pl.plot(moy * np.ones((10)), np.linspace(0, xh.max(), 10), 'k--')
        pl.title('%i simu  de %i npts: a = %f ( => a_simu moy = %f med = %f)' % (N, npts, a, moy, med)) #coef.T[0].mean()))

        pl.figure()
        xx, yy = np.histogram(coef.T[1])
        rg = (yy.min(), yy.max())
        nbins = int((rg[1] - rg[0])/ dbin)
        xh, yh, hh = pl.hist(coef.T[1])#, bins = nbins)#, range = (b-1,b+1))
        med = np.median(coef.T[1])
        moy = coef.T[1].mean()
        pl.plot(b*np.ones((10)), np.linspace(0, xh.max(), 10), 'r--')
        pl.plot(med*np.ones((10)), np.linspace(0, xh.max(), 10), 'b--')
        pl.plot(moy*np.ones((10)), np.linspace(0, xh.max(), 10), 'k--')
        pl.title('%i simu  de %i npts : b = %f ( => b_simu moy = %f med = %f)' % (N, npts, b, moy, med))

        if n_gamma == 1:
            realg = np.array([1.356])
        elif n_gamma == 2:
            realg = np.array([1.325, 2.2222])
        elif n_gamma == 4:
            realg = 1/30. * np.array([1., -19., 133., 229.])
        elif n_gamma == 'dep':
            realg = np.array([0.01, 0.005])
        
        for n in range(len(realg)):
            pl.figure()

            xx, yy = np.histogram(gammas.T[n])
            rg = (yy.min(), yy.max())
            nbins = int((rg[1] - rg[0])/ dbin)
            
            xh, yh, hh = pl.hist(gammas.T[n], bins = nbins, range = rg)
            med = np.median(gammas.T[n])
            moy = gammas.T[n].mean()

            pl.plot(realg[n] * np.ones((10)), np.linspace(0, xh.max(), 10), 'r--')
            pl.plot(med*np.ones((10)), np.linspace(0, xh.max(), 10), 'b--')        
            pl.plot(gammas.T[n].mean()*np.ones((10)), np.linspace(0, xh.max(), 10), 'k--')
            pl.title('%i simu  de %i npts : gamma_%i = %f ( => gamma_%i_simu moy = %f med = %f)' % (N, npts, n, realg[n], n, moy, med))

    return coef, gammas


def control_moy(n_gamma, N = 500, nb_pts  = [50, 100, 250, 500, 1000], max_iter = 10, dbin = 0.01, plot = True ):
    """
    plot of the mean and mediane of all parameter for the "n_gamma" variance model for differents initial number of points.
    
    Inputs : - n_gamma = 1, 2, 4 or 'dep', variance model code 
             - N = int, number of realisations
             - nb_pts = list of int, number of initiale points for the function.
             - max_iter = int, is the maximum number of iteration wanted.
             - dbin = float, interval of histograms binning.
             - plot = bool, True if we want to see each plot of the control function.

    Outputs : plots                                                                                   
    """
    A = np.zeros((len(nb_pts),1))
    B = np.zeros((len(nb_pts),1))

    MA = np.zeros((len(nb_pts),1))
    MB = np.zeros((len(nb_pts),1))
    
    SA = np.zeros((len(nb_pts),1))
    SB = np.zeros((len(nb_pts),1))
    if type(n_gamma) != int:
        n = 2
    else :
        n = n_gamma
    G = np.zeros((len(nb_pts),n))
    MG = np.zeros((len(nb_pts),n))
    SG = np.zeros((len(nb_pts),n))
    for nn in range(len(nb_pts)):
        c, g = control(N = N, max_iter = max_iter, n_gamma = n_gamma, npts = nb_pts[nn], dbin = dbin, plot = plot)
        A[nn] = c.T[0].mean()
        B[nn] = c.T[1].mean()
        MA[nn] = np.median(c.T[0])
        MB[nn] = np.median(c.T[1])

        SA[nn] = c.T[0].std()
        SB[nn] = c.T[1].std()
        for i in range(n):
            G[nn][i] = g.T[i].mean()
            MG[nn][i] = np.median(g.T[i])
            SG[nn][i] = g.T[i].std()
    a = 1.235
    b = 9.123

    if n_gamma == 1:
        realg = np.array([1.356])
    elif n_gamma == 2:
        realg = np.array([1.325, 2.2222])
    elif n_gamma == 4:
        realg = 1/30. * np.array([1., -19., 133., 229.])
    else:
        realg = np.array([0.01, 0.005])

    pl.figure()
    for ii in range(len(nb_pts)):
        #pl.plot(A[ii],nb_pts[ii], '.', label ='%i pts' %(nb_pts[ii]))
        pl.errorbar(nb_pts[ii], A[ii], yerr = SA[ii], fmt='.', label ='moy %i pts' %(nb_pts[ii]))
        pl.errorbar(nb_pts[ii], MA[ii], yerr = SA[ii], fmt='*', label ='med %i pts' %(nb_pts[ii]))
    pl.plot(np.linspace(0,1000,10), a*np.ones(10), 'r--', label= 'real')
    #pl.plot(a*np.ones(10), np.linspace(0,1000,10), 'r--', label= 'real')
    pl.title('a')
    pl.legend()
    
    pl.figure()
    for ii in range(len(nb_pts)):
        pl.errorbar(nb_pts[ii], B[ii], yerr = SB[ii], fmt = '.', label ='moy %i pts' %(nb_pts[ii]))
        pl.errorbar(nb_pts[ii], MB[ii], yerr = SB[ii], fmt = '*', label ='med %i pts' %(nb_pts[ii]))
    pl.plot(np.linspace(0,1000,10), b * np.ones(10),'r--',label= 'real')
    pl.title('b')
    pl.legend()
    
    for iii in range(n):
        pl.figure()
        for ii in range(len(nb_pts)):
            pl.errorbar(nb_pts[ii], G[ii][iii], yerr = SG[ii][iii],fmt = '.', label ='moy %i pts' %(nb_pts[ii]))
            pl.errorbar(nb_pts[ii], MG[ii][iii], yerr = SG[ii][iii],fmt = '*', label ='med %i pts' %(nb_pts[ii]))
        pl.plot(np.linspace(0,1000,10), realg[iii] * np.ones(10), '--', label= 'real')
        pl.title( 'gamma_%i' % (iii))
        pl.legend()
