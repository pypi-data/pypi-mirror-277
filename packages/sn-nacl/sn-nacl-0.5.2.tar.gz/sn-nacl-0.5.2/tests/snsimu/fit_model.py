#!/usr/bin/env python3
import numpy as np
import pylab as pl
import scipy
import re
pl.ion()
#from astropy.io import fits as pf
from scipy.sparse import coo_matrix, dia_matrix, dok_matrix, diags
from scipy.optimize import leastsq, fmin_ncg, check_grad, approx_fprime
from saunerie.lsqfit import Chi2
from saunerie.fitparameters import FitParameters
from saunerie.bspline import BSpline, CardinalBSplineC, integ
from croaks import NTuple
from numpy.polynomial.legendre import leggauss
from sksparse.cholmod import cholesky, cholesky_AAt
from saunerie import optim, plottools
#from scipy.integrate import quad
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)


from astropy.modeling import models, fitting
from scipy.integrate import simps
from astroquery.simbad import Simbad
import matplotlib.gridspec as gridspec

import new_fitmodel as nf

# first model :
# $$ y_{sn,t_{mjd}} = f_{sn} \times S\left(\frac{t_{mjd} - t_{max}}{1+s_{sn}}; \theta_{splines} \right) $$

theta_range = [-35, 35]

customSimbad = Simbad()
customSimbad.remove_votable_fields('coordinates')
customSimbad.add_votable_fields('sptype')

def sqp_cholm(model, var_model, y, h, x0, g0, n_iter=30, sigma=None, ll=0.001, dchi2=0.01):
    """ Solves a non-linear programming problem with equality constraints using a Gauss-Newton approximation of the Hessian
    The problem must write as follows:                                                                                                                                                                                Find x that minimize: \sum (y_i - model(x)_i)^2
    subject to the constraint h(x) = 0

    Parameters:
    -----------
    model: callable with the signature (params, jac=False)
           must return if jac: the model evaluated at point params
                         else: the model and its jacobian under the form of a sparse matrix
           can raise ValueError in which case the model is assumed undefined at x
    y: array
       The fit data
    h: callable with the same signature as model
    x0: array
        starting point
    n_iter: maximal number of iterations

    Returns:
    --------
    The best fit after n_iter iterations
    """
    n = len(x0)
    m = len(g0)
    nn = n+m
    x = x0
    g = g0
    iter = 0
    alpha = 0.7

    while iter < n_iter:
        print(iter)
        val, jacobian = model(x, jac=True)
        V, dV = var_model(g, val, x, jacobian=jacobian)
        residuals = y - val
        
        if sigma is not None:
            #jacobian.data /= sigma[jacobian.row]
            #residuals /= sigma
            variance = np.diag(V) + sigma**2
        else :
            variance = np.diag(V)
        w = coo_matrix(np.diag(1/variance))

        obj_start = (np.diag(w.toarray()) * residuals**2).sum() + len(residuals) * np.log(np.pi) + np.log(1./np.diag(w.toarray())).sum()
        
        B = hessian(w, x, g, jacobian, dV)
        R = model.regulz(ll, g)
        B += R
        gradf = - grad(residuals, w, jacobian, dV, x, g)
        
        if h is not None:
            cons, H = h(x, Nsn = len(g0), jac=True, mask=None)
            M = scipy.sparse.bmat([[B, H.T], [H, None]])
            #d0 = scipy.sparse.linalg.spsolve(M, -np.r_[gradf, cons])
            try:
                factor = cholesky(M, mode='simplicial')
            except:
                return x, B, M
            d0 = factor(-np.r_[gradf, cons])
            mu0 = d0[nn:]

            d0 = d0[:nn]
            def phi(vect):
                p = vect[:n]
                g = vect[n:]
                val = model(p)
                V = var_model(g, val, p)
                variance = np.diag(V) + sigma**2
                w = coo_matrix(np.diag(1/variance))
                return (w * ( y - val)**2).sum() + len(y) * np.log(np.pi) + np.log(1./np.diag(w.toarray())).sum() #((w * ( y - val))**2).sum()
            def crit(t):
                return phi(np.r_[x,g] + t * d0)

        t, fval, ni, funcalls = scipy.optimize.brent(crit, brack=(0, 1), full_output=True)
        dof = len(y) - nn
        print(('stepsize: %g, objective: %g -> %g, decrement: %g, D.o.F.: %d, objective/dof: %g' % (t, obj_start, fval, obj_start - fval, dof, fval / dof)))
        decrement = obj_start - fval
        print('g =',g)
        #print('dg =',d0[n:])
        x = x + t * d0[:n]
        g = g + t * d0[n:]
        print('constraint 1 : %f' % ((H[0] * np.r_[x,g]).sum()))
        print('constraint 2 : %f' % ((H[1] * np.r_[x,g]).sum()))
        if len(h.val) == 3:
            print('constraint 3 : %f' % ((H[2] * np.r_[x,g]).sum()))
        iter = iter + 1
        #345(4)
        if decrement < dchi2:
            break

    return x, g, B, M




def hessian(w, p, g, J, dV):
    """
    Create Hessian matrix needed to minimized the chi2, in order to fit models of light curves and variances on data, using Newton-Raphson's method.
    Appearing on the left hand side of the equation.
    Input : - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(x) * len(x)).
            - p = Array, is the parameter of the LIGTH CURVE model.
            - g = Array, is the parameter of the VARIANCE model.
            - J = coo_matrix, is the Jacobian of the Light curev model.
            - dV = coo_matrix, is the Jacobian of the variance model.
            - reml = bool, if the reml technic is needed
    Output : - H = coo_matrix, sparse hessian matrix
    """
    H0 = 2 * J.T * w * J
    H = coo_matrix(H0)
    H00 = H.data
    i00 = H.row
    j00 = H.col

    def trace(i, j, w = w, dV = dV):
        """
        Calculate the trace term of the product of 2 derivative (wrt the parameters i and j)  appearing in the equation.
        Input : - i = int, parameters of which we want to take de derivative.
                - j = int, parameters of which we want to take de derivative.
                - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(data) * len(data)).
                - dV = coo_matrix, is the Jacobian of the variance model.
                - reml = bool, if the reml technic is needed
        Output : - float, result of the trace.
        """
        dV = dV.toarray()
        #dVi = coo_matrix(np.diag(dV[i]))
        #dVj = coo_matrix(np.diag(dV[j]))
        dVi = dV[i]
        dVj = dV[j]
        #return (w * dVi * w * dVj).toarray().trace()
        wdiag = np.diag(w.toarray())
        return (wdiag*dVi*wdiag*dVj).sum()

    npar = p.shape[0] + g.shape[0]
    Tr = np.array([trace(i,j) for i in range(npar) for j in range(i, npar)])
    ii = [i for i in range(npar) for j in range(i, npar)]
    jj = [j for i in range(npar) for j in range(i, npar)]

    H_l = coo_matrix((np.hstack((Tr,Tr)), (np.hstack((ii,jj)), np.hstack((jj, ii)))), shape = ( npar, npar))
    H_l = coo_matrix((np.hstack((H_l.data, -np.diag(H_l.toarray())/2.)), (np.hstack((H_l.row, range(H_l.toarray().shape[0]))), np.hstack((H_l.col, range(H_l.toarray().shape[0]))))), shape = (npar,npar))
    H = coo_matrix((H00, (i00, j00)), shape = ( npar, npar))
    return H + H_l

def grad(res, w, J, dV, p, g):
    """
    Create gradient vector needed to minimized the chi2, in order to fit models of light curves and variances on data, using Newton-Raphson's method.                                                             
    Appearing on the right hand side of the equation.
    Input : - res = Array, is the residual of the measurement substracted by the model.            
            - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(x) * len(x)).
            - J = coo_matrix, is the Jacobian of the Light curev model.
            - dV = coo_matrix, is the Jacobian of the variance model.
            - p = Array, is the parameter of the LIGTH CURVE model.
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
    return - resul




class SModel(object):

    def __init__(self, xdata, rng_spline = theta_range, grid_size = 10):
        self.nb_sn = len(np.unique(xdata['id']))
        self.spline_basis = CardinalBSplineC(grid_size, rng_spline)
        self.xdata = xdata
        self.n_theta = grid_size
        self.pars = self.para_init(xdata)

    def para_init(self, xdata, plot = False):
        fp = [("flux", self.nb_sn), ("tmax", self.nb_sn), ("s", self.nb_sn), ("theta", len(self.spline_basis))]
        fp = FitParameters(fp)

        def fitpoly(x, y, yunc , deg, plot = True):
            fit = fitting.LevMarLSQFitter() #Linear
            poly_init = models.Polynomial1D(degree = deg)
            fitted_fn = fit(poly_init, x, y)#, weights=yunc)
            if plot:
                pl.figure()
                pl.plot(x, y, 'k.', label='Data')
                pl.plot(x, fitted_fn(x), 'b.', label='Fitted Model')
                pl.xlabel('x')
                pl.ylabel('y')
                pl.legend()
            return fitted_fn
        if plot:
            pl.figure()
        N = len(np.unique(xdata['id']))
        data = xdata #generate_Lc(N, plot = False)                                                                                                                                                                 
        nb_pt = 1000   #
        X_re = np.array([])
        Y_re = np.array([])
    
        for i in np.unique(data['id']):
            d = data[data['id']==i]
            #if np.where(d == d.max())[0] == 0   :
             #   break
            
            x = d['Date']
            y = d['Flux']
            yerr = d['FluxErr']
            pfit = fitpoly(x, y, yerr, 5, plot = False)
            rng = np.linspace(x.min(),x.max(),nb_pt)
            p = pfit(rng)
            m = p.max()
            t = rng[np.where(p == m)[0]][0]

            l = rng[np.where(p > m/2.)[0]]
            s = (l.max() - l.min())/(2*np.sqrt(2*np.log(2)))

            fp['flux'].full[i] = m
            fp['tmax'].full[i] = t
            fp['s'].full[i] = s #np.sqrt(mod2 - mod0**2)                                                                                                                                                                       
            X_re = np.hstack((X_re, (x-t)/((1+s)*(1+d['ZP']))))
            Y_re = np.hstack((Y_re, y/m))
            if plot:
                pl.plot(X_re, Y_re, 'r.')
        if plot:
            X, Y, Yerr = plottools.binplot(X_re, Y_re, nbins = 50, marker='p', color='Darkblue')

        spline = self.spline_basis

        J = spline.eval(X_re) 
        H = J.T * J + 0.01 * diags(np.ones(J.shape[1]))
        factor = cholesky(H.tocsc())
        theta = factor(J.T * Y_re)
        fp['theta'].full[:] = theta

        I1 = (theta * integ(spline)).sum()        
        I2 = (theta * integ(spline, n=1)).sum()
        I3 = (theta * integ(spline, n=2)).sum()
        print('first constraint int =', I1)
        print('second constraint int =', I2)
        print('third constraint int =', I3)

        fp['theta'].full /= I1
        fp['flux'].full *= I1

        return fp #, I1, I2

    
    def regulz(self, ll, g):
        """
        """
        n = len(self.pars.free) + len(g)
        d = np.zeros(n)
        d[:] = 1.
        d[self.pars.indexof('theta')] = 1.
        #        r = ll * diags(d)
        return ll * diags(d)


    def __call__(self, p, jac=False, xdata=None):
        if xdata is None:
            xdata = self.xdata
        #xdata = self.tdata
        self.pars.free = p
        ide = xdata['id']
        sp1 = (1. + self.pars['s'].full[ide])
        phases = (xdata['Date'] - self.pars['tmax'].full[ide]) / (sp1 * (1 + xdata['ZP'])) 
                
        flx = self.pars['flux'].full[ide]
        J = self.spline_basis.eval(phases)
        v = flx * (J * self.pars['theta'].full)

        if jac:
            N = len(xdata)
            n = len(self.spline_basis)
            isn = np.arange(N)

            inter_t = xdata[xdata['id']==0].shape[0]
            dB = self.spline_basis.deriv(phases)

            # derivée flux:                                                                                                                                                                                        
            ii_f = isn
            jj_f = self.pars['flux'].indexof(ide)
            val_f = J * self.pars['theta'].full

            #derivee tmax:                                                                                                                                                                                         
            ii_t = isn
            jj_t = self.pars['tmax'].indexof(ide)
            val_t = self.pars['flux'].full[ide] * (-1/(sp1 * (1 + xdata['ZP']))) * (dB * self.pars['theta'].full)

            #derivee s:                                                                                                                                                                                            
            ii_s = isn
            jj_s = self.pars['s'].indexof(ide)
            val_s = self.pars['flux'].full[ide] * (-phases/sp1) * (dB * self.pars['theta'].full)

            #derivee theta:                                                                                                                                                                                        
            ii_theta = J.row
            jj_theta = self.pars['theta'].indexof(J.col)
            val_theta = self.pars['flux'].full[ide[J.row]] * J.data

            i = np.hstack((ii_f, ii_t, ii_s, ii_theta))
            j = np.hstack((jj_f, jj_t, jj_s, jj_theta))
            val_jac = np.hstack((val_f, val_t, val_s, val_theta))

            idx_fix = np.where(j != -1)
            Jac = coo_matrix((val_jac[idx_fix], (i[idx_fix],j[idx_fix])), shape = ( N, len(self.pars.free))) #3 * self.nb_sn + self.nb_theta))                                                                     
            return  v , Jac
        else :
            return v


class VModel(object):
    """ 
    Two variance model can be implemented.
    variance model:  - variance = v **2 * flux**2, here v is a parameter and flux is the measure of the SN light curve
                     - variance = v **2 where the variance does not depend of the SN flux

    There are two models, labelled by the input "lab", 'cst' stands for constant and refers to the second one
    and anything else stands for 'dependant' and refers to the first one.
    """
    def __init__(self, n_theta, data, lab = 'cst'):
        """
        Initialisation of the model.
        Input : n_theta = Int, is the number of spline use in the model of light curves
                data = NTuple, is the light curve data
                lab = str, is the type of variance model wanted
        Output : Varience model
        """
        #self.value = model_sn                                                                                                                                                                                     
        self.data = data
        self.nb_sn = len(np.unique(data['id']))
        self.nb_theta = n_theta
        self.pars = self.para_init()
        self.lab = lab

    def para_init(self):
        """                                                                                                                                                                                                               Initialisation of the parameters of the model.
        the parameter v represent the standard deviation : sigma = np.sqrt(variance), one per Supernova
        Input :
        Output : FitParameters, class of parameter
        """
        fp = [("v", self.nb_sn)]
        fp = FitParameters(fp)
        #fp['v'].fix(0, val = 0.1 )
        fp['v'] = 0.075 #p['tmax'].fix(0)
        return fp

    def __call__(self, g, value, p, J=None):
        """
        Return the evalutaion of the model given a set of parameter p.

        Input : - value = NTuple, is the value of the light curve model
                - p = Array, is the VARIANCE MODEL parameters
                - J = Array, is the matrix of the derivation of the LIGHT CURVE MODEL.

        Output : - if J is given : Array, a diagonal matrix of the values of the variance model evaluate with the given parameter.
                 - else : - Array the same matrix as describe above
                          - dV = coo_matrix , sparse matrix of the derivative of the VARIANCE MODEL.
        """
        ide = self.data['id']

        self.pars.free = g

        if J == None:
            if self.lab == 'cst':
                return np.diag(self.pars['v'].full[ide]**2) #np.diag(p[ide])
            else :
                return np.diag((self.pars['v'].full[ide]*(value))**2) #np.diag(p[ide]*(value)**2)
        else :
            N = len(p) + len(g)
            n = len(value)
            isn = np.arange(n)

            # derive parametre de J:
            ii_J = J.col
            jj_J = J.row
            
            if self.lab == 'cst':
                val_J = np.zeros((len(J.data))) #2 * value[ide[J.row]] * J.data * p[ide[J.row]]
            else :
                val_J = 2 * value[ide[J.row]] * J.data * self.pars['v'].full[ide[J.row]]**2
            # derive V_{n}:

            ii_v = len(p) + ide #J.shape[1] + ide #len(p) + ide ######################################################################################################<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            jj_v = isn
            if self.lab == 'cst':
                val_v = np.ones(len(value)) #value**2
            else :
                val_v = 2 * self.pars['v'].full[ide] * value**2

            i = np.hstack((ii_J, ii_v))
            j = np.hstack((jj_J, jj_v))
            val_jac = np.hstack((val_J, val_v))

            dV = coo_matrix((val_jac, (i,j)), shape = (N, n))
            if self.lab == 'cst':
                return np.diag(self.pars['v'].full[ide]**2), dV #*(value)**2), dV
            else :
                return np.diag((self.pars['v'].full[ide]*(value))**2), dV




        
        
class IntegralConstraints():
    """
    """
    def __init__(self, pars, basis, vals=[1., 0., 10.], limits=None):
        """
        """
        self.basis = basis
        self.val = np.array(vals)
        #JJ = np.array([])
        #for i in range(len(vals)):
        self.JJ = np.vstack([integ(self.basis, i) for i in range(len(vals))]).T
                                 #integ(self.basis, 1),
                                 #integ(self.basis, 2)]).T
        #self.JJ = JJ.T
        self.reset_pars(pars)
        #        self.pars = pars                                                                                                                                                                                 
        #        s = pars._struct.slices['theta']
        
        if limits is not None:
            self._integral_limits(limits[0], limits[1], self.JJ)

    def reset_pars(self, pars):
        """                                                                                             
        """
        self.pars = pars
        n = len(self.pars.free)
        self.J = np.zeros((n,len(self.val)))
        i = self.pars.indexof('theta')
        idx = i>=0 #
        self.J[i[idx],:] = self.JJ[idx]
        
    def _integral_limits(self, xmin, xmax, J):
        """
        should be deprecated
        """
        # limit the constraints to a range in x    
        g = self.basis.grid
        gg = 0.5 * (g[1:] + g[:-1])
        ok = np.zeros(len(self.basis)).astype(bool)
        ok[self.basis.order-1:] = (gg>=xmin) & (gg<=xmax)
        J[~ok] = 0.
        self.ok = ok

    #    def init_pars(self):
    #        r = FitParameters([('LL', 3)])
    #        return r                                                                                                                                                                                              

    def __call__(self, p, Nsn, jac=False, mask=None):
        """
        """
        if mask is not None:
            J = self.J.T * mask
        else:
            J = self.J.T
            JJ = np.zeros((J.shape[0], J.shape[1] + Nsn ))
            for i in range(J.shape[0]):
                JJ[i][:J.shape[1]] = J[i]
                
        val = J.dot(p) - self.val

        if jac == False:
            return val

        return val, JJ




def generate_Lc(N, dx = 0.01, rng = [-70, 180], variance_sn = 0.05 ,plot=False, lab = 'dep'):
    """                                                                                                                                                                                                            
    """
    x,y,yerr = [], [], []
    ide = []
    for i in range(N):
        tmax = np.random.uniform(rng[0], rng[1])
        sig = np.random.uniform(1., 10.)
        norm = np.random.uniform(50., 1000.)

        npts = np.random.randint(10,20)
        
        xx = np.random.uniform(-3*sig, 3*sig, size=npts)
        #xx = np.linspace(-20, 20, npts)
        yy = norm * np.exp(-0.5 * (xx/sig)**2)
        xx += tmax
        yy_err = 10.
        if lab == 'cst' :
            yy += np.random.normal(scale=np.sqrt((variance_sn)**2) , size=len(yy))#np.random.normal(scale=yy_err, size=len(yy))
        else :
            yy += np.random.normal(scale=np.sqrt((variance_sn * yy)**2) , size=len(yy))
        x.append(xx)
        y.append(yy)
        ide.append(np.full(len(xx), i))
        yerr.append(np.full(len(xx), yy_err))

    x = np.hstack(x)

    # data set                                                                                                                                                                                                     
    data = NTuple(len(x),dtype=[('Date', float), ('Flux', float), ('FluxErr', float), ('ZP', float) , ('id',int)])
    data['Date'] = np.hstack(x)
    data['Flux'] = np.hstack(y)
    data['FluxErr'] = np.hstack(yerr)
    data['ZP'] = 0.01 
    data['id'] = np.hstack(ide)

    if plot :
        for i in np.unique(data['id']):
            idx = data['id'] == i
            tmax = data['Flux'][idx].max()
            phase = data['Date'][idx]
            pl.errorbar(phase, data['Flux'][idx], yerr=data['FluxErr'][idx], fmt='.')

    return data




def fit_sqp(data = None, N = 20, C = [1., 0., 1.], n_theta = 30, max_iter= 200, nomin = False, survey = 'csp', band = b'SWOPE::B', SNe = None, lab = 'dep', variance_sn = 0.05):
    if data is None :
        print(data)
        data = generate_Lc(N, plot = False, variance_sn = variance_sn, lab = lab)
        
    else :
        try:
            data = data[data['Filter'] == band]
        except:
            data = data
        #init_data, redu_data, SNe = data_cons(data = data, band = band, survey = survey, before = 7, after = 7 )
        
    #data = data[un]
    sig = data['FluxErr']
    
    #w = 1. / data['FluxErr']
    model = SModel(data, grid_size = n_theta)
    var_model = VModel(model.n_theta, data, lab = lab)
    
    p = model.pars.free
    g = var_model.pars.free
    
    #Initialilsation
    init = model(p, jac=0)
    fig = pl.figure()
    ax1 = pl.subplot(211)
    ax2 = pl.subplot(212, sharex = ax1)

    for i in np.unique(data['id']):
        d = data[data['id'] == i]
        date = np.linspace(d['Date'].min(), d['Date'].max())
        u = np.full(len(date), i).astype(int)
        z = np.full(len(date), d['ZP'][0]).astype(float)
        d = np.rec.fromarrays((date, z, u), names=['Date', 'ZP','id'])
        v = model(p, jac=0, xdata=d)
        ax1.plot(d['Date'], v, color=pl.cm.jet(i), ls='-')
       
        
    ax1.errorbar(data['Date'], data['Flux'], yerr=data['FluxErr'],color ='k', marker='.', ls='')
    ax1.set_title(survey + '  ' + band.decode('UTF-8') + '   INIT')
    ax1.set_ylabel('Flux') 

    ax2.errorbar(data['Date'], data['Flux']-init, yerr=data['FluxErr'], color ='k', marker='.', ls = '')
    ax2.plot(np.linspace(data['Date'].min(), data['Date'].max(), 1000), np.zeros(1000), ls = '--', color = 'red', linewidth = 0.5 ) 
    vmin = (data['Flux']-init).min() - 0.1
    vmax = (data['Flux']-init).max() + 0.1
    ax2.set_ylim(vmin, vmax)
    ax2.set_ylabel('Residuals')
    ax2.set_xlabel('Days')
    cons = IntegralConstraints(model.pars, model.spline_basis, vals=C, limits=(-32., 32.))

    p, g, B, M = sqp_cholm(model, var_model, data['Flux'], cons, p, g, n_iter=max_iter, sigma = sig)
   
    fig = pl.figure()
    ax1 = pl.subplot(211)
    ax2 = pl.subplot(212, sharex = ax1)

    phase = data['Date']
    #p = model.pars.free
    chi2 = []
    #snw = []
    #sn = sn_csp()
    pl.figure()
    ax1.errorbar(phase, data['Flux'], yerr = data['FluxErr'], marker='.', ls='', color='k')
    for i in np.unique(data['id']):
        d = data[data['id'] == i]
        date = np.linspace(d['Date'].min(), d['Date'].max())
        u = np.full(len(date), i).astype(int)
        z = np.full(len(date), d['ZP'][0]).astype(float)
        d_sn = np.rec.fromarrays((date, z, u), names=['Date','ZP','id'])
        v = model(p, jac=0, xdata=d_sn)
        ax1.plot(d_sn['Date'], v, color=pl.cm.jet(i), ls='-')
        ax1.plot(d_sn['Date'], v + 1*(np.sqrt((g[i] * v)**2)), color=pl.cm.jet(i), ls='--', linewidth = 0.5)
        ax1.plot(d_sn['Date'], v - 1*(np.sqrt((g[i] * v)**2)), color=pl.cm.jet(i), ls='--', linewidth = 0.5)

        col = np.random.randint(0,1000)/1000
        
        pl.plot((d['Date'] - p[len(np.unique(data['id']))+i])/ (1 + p[2*len(np.unique(data['id'])) + i]), d['Flux']/np.abs(p[i]), marker = '.', color = pl.cm.jet(col), ls= '' )

        val = model(p, jac=0, xdata=d)
        chi2.append(((d['Flux'] - val)**2/d['FluxErr']**2).sum()/len(d)) 
        #if chi2[len(chi2)-1] >= 10:
         #   ax1.plot(d_sn['Date'], v, color='r', ls='-')
          #  ax1.text(d_sn['Date'][int(len(d_sn['Date'])/2)], v[v == v.max()], SNe[i].decode('UTF-8'))

    pl.title(survey + '  ' + band.decode('UTF-8') + '  Light Curves corrected with fit parameters')
    pl.xlabel(r'$\frac{Days - DayMax_{SN}}{(1+s_{SN})(1+z)}$')
    pl.ylabel(r'$\frac{Flux_{SN}}{|Fitted Flux_{SN}|}$')
    ax1.set_title(survey + '  ' + band.decode('UTF-8') + '  FIT')
    ax1.set_ylabel('Flux')
    v = model(p, jac=0)
    
    ax2.errorbar(phase, data['Flux']-v, yerr = data['FluxErr'], color ='k', marker='.', ls = '')
    ax2.plot(np.linspace(data['Date'].min(), data['Date'].max(), 1000), np.zeros(1000), ls = '--', color = 'red', linewidth = 0.5 )
    ax2.set_ylim(vmin, vmax)
    ax2.set_ylabel('Residuals')
    ax2.set_xlabel('Days')

    """
    pl.figure()
    pl.title(survey + '  ' + band.decode('UTF-8') + '  Chi2 = f(sn)')
    pl.ylabel(r'$\chi^{2}}$/nb_pts')
    pl.xlabel('SN')
    pl.scatter(range(len(chi2)), chi2, marker = '.')
    #compt = 0
    for i in range(len(chi2)):
        if chi2[i] > 10.:
            cst = np.random.randint(0, 5)
            sn0 = SNe[i].decode('UTF-8')
            sn0 = sn0[:2] + ' ' + sn0[2:]
            result_table = customSimbad.query_object(sn0)
            pl.text(i-1, chi2[i] + 3, sn0)
            pl.text(i-1, chi2[i] ,result_table['SP_TYPE'][0].decode('UTF-8'))
            #compt += 1

    SNe_type = []
    for i in range(len(chi2)):
        sn0 = SNe[i].decode('UTF-8')

    
    idx = np.array(chi2).argsort()
    pl.figure()
    pl.xlabel(r'$\chi^{2}}$/nb_pts')
    pl.ylabel('SN')
    pl.title(survey + '  ' + band.decode('UTF-8') + '  SN = f(Chi2)')
    pl.plot(np.array(chi2)[idx], SNe[idx], 'k.')
    """

    #if B is not None:
        #fact = cholesky(B, mode='simplicial')
        #U = fact.inv().todense()

        #    U = np.linalg.inv(HH.todense())                                                                                                                                                                       
        #D = np.matrix(np.diag(U))
        #C = U / np.sqrt(D.T * D)
        #pl.matshow(C)
        #pl.colorbar()

    return p, g, model, var_model #s, data, model, cons, B, M#, snw

def control(real = 10, N = 10, sigma_err = 1., variance_sn = 0.05, lab = 'cst', dbin = 0.02, plot = False):
    
    """                                   
    Control plot : histogram of the variance parameters for found for all SNe.
    Input : - real = int, number of realisation of the fit.
            - N = int, number of SNe fitting in each "real" realisation.
            - sigma_err = float, measure error we want on the SNe light curves
     




       - variance_sn = float, variance we want to be modeled by the variance model.
            - lab = str 'cst' or 'dep', type of variance model we want to use.
            - nbins = int, number of bins for the histogram.
            - plot = bool, True if we want to see each Sne light curve plot with the foncion plot_cl.       Output : histogram
    """
    g = []
    for i in range(real):
        #data = generate_Lc(N = N, variance_sn = variance_sn)#, lab = lab)
        #data = generate_Lc(N, plot = False, variance_sn = variance_sn)
        p0, g0, model, var_model = fit_sqp(data = None)#, max_iter = 100, lab = lab)#, plot = plot)
        g.append(g0)

    g = np.array(g)
    pl.figure()

    xx, yy = np.histogram(g.ravel())
    rg = (yy.min(), yy.max())
    nbins = int((rg[1] - rg[0])/ dbin)

    xh, yh, hh = pl.hist(g.ravel(), bins=nbins)#, range = (,0.01))                                       

    med = np.median(g)
    moy = g.mean()
    pl.plot(variance_sn * np.ones(10), np.linspace(0,xh.max(),10), 'r--')
    pl.plot(moy * np.ones(10), np.linspace(0,xh.max(),10), 'k--')
    pl.plot(med * np.ones(10), np.linspace(0,xh.max(),10), 'b--')
    pl.title('%i real  de %i SN : v = %f ( => v_simu moy : %f med : %f)' % (real, N, variance_sn, moy, med))


def comparaison(N = 20, variance_sn = 0.05, lab = 'dep'):
    data = generate_Lc(N, plot = False, variance_sn = variance_sn, lab = lab)

    p, g, model, var_model = fit_sqp(data = data, lab = lab)
    
    data, model1, cons, B, M = nf.fit_sqp(data = data)

    phase = data['Date']
    p1 = model1.pars.free
    
    fig = pl.figure(figsize=(10, 10))
    outer = gridspec.GridSpec(2, 1, wspace=0.2, hspace=0.2)
    inner = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer[0], wspace=0.1, hspace=0.1)

    ax1 = pl.Subplot(fig, inner[0])
    ax2 = pl.Subplot(fig, inner[1], sharex = ax1)
    ax1.errorbar(phase, data['Flux'], yerr = data['FluxErr'], marker='.', ls='', color='k')
    for i in np.unique(data['id']):
        d = data[data['id'] == i]
        #idx_bads = bads[data['id'] == i]
        date = np.linspace(d['Date'].min(), d['Date'].max())
        u = np.full(len(date), i).astype(int)
        z = np.full(len(date), d['ZP'][0]).astype(float)
        d_sn = np.rec.fromarrays((date, z, u), names=['Date','ZP','id'])
        v = model(p, jac=0, xdata=d_sn)
        ax1.plot(d_sn['Date'], v, color=pl.cm.jet(i**2), ls='-')
        if lab == 'cst' :
            print('il entre ')
            ax1.plot(d_sn['Date'], v + 1*(np.sqrt((g[i])**2)), color=pl.cm.jet(i**2), ls='--', linewidth = 0.5)
            ax1.plot(d_sn['Date'], v - 1*(np.sqrt((g[i])**2)), color=pl.cm.jet(i**2), ls='--', linewidth = 0.5)
        else :
            ax1.plot(d_sn['Date'], v + 1*(np.sqrt((g[i] * v)**2)), color=pl.cm.jet(i**2), ls='--', linewidth = 0.5)
            ax1.plot(d_sn['Date'], v - 1*(np.sqrt((g[i] * v)**2)), color=pl.cm.jet(i**2), ls='--', linewidth = 0.5)
    ax1.set_ylabel('Flux')
    v = model(p, jac=0)
    ax2.errorbar(phase, data['Flux']-v, yerr = data['FluxErr'], color ='k', marker='.', ls = '')
    ax2.plot(np.linspace(data['Date'].min(), data['Date'].max(), 1000), np.zeros(1000), ls = '--', color = 'red', linewidth = 0.5 )
    #ax2.set_ylim(vmin, vmax)
    ax2.set_ylabel('Residuals')
    ax2.set_xlabel('Days')
    fig.add_subplot(ax1)
    fig.add_subplot(ax2)

    inner = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=outer[1], wspace=0.1, hspace=0.1)
    ax3 = pl.Subplot(fig, inner[0], sharex = ax1, sharey = ax1)
    ax4 = pl.Subplot(fig, inner[1], sharex = ax3, sharey = ax2)
    ax3.errorbar(phase, data['Flux'], yerr = data['FluxErr'], marker='.', ls='', color='k')
    for i in np.unique(data['id']):
        d = data[data['id'] == i]
        #idx_bads = bads[data['id'] == i]
        date = np.linspace(d['Date'].min(), d['Date'].max())
        u = np.full(len(date), i).astype(int)
        z = np.full(len(date), d['ZP'][0]).astype(float)
        d_sn = np.rec.fromarrays((date, z, u), names=['Date','ZP','id'])
        v = model1(p1, jac=0, xdata=d_sn)
        ax3.plot(d_sn['Date'], v, color=pl.cm.jet(i**2), ls='-')
    ax3.set_ylabel('Flux')
    v = model1(p1, jac=0)

    ax4.errorbar(phase, data['Flux']-v, yerr = data['FluxErr'], color ='k', marker='.', ls = '')
    ax4.plot(np.linspace(data['Date'].min(), data['Date'].max(), 1000), np.zeros(1000), ls = '--', color = 'red', linewidth = 0.5 )
    #ax4.set_ylim(vmin, vmax)
    ax4.set_ylabel('Residuals')
    ax4.set_xlabel('Days')
    fig.add_subplot(ax3)
    fig.add_subplot(ax4)



    
    
    
def data_cons(data = None, band = b'SWOPE::B', survey = 'csp', mjd_plus = 30, mjd_moins = 15):#,  n_pt = 7):
    if data is None:
        data = NTuple.fromfile('work/snls5/' + survey + '_lc.npy')
        
    data = data[data['Filter'] == band]
    mjd_max = np.zeros_like(data['Date'])
    
    for i in np.unique(data['id']):
        
        d = np.where(data['id'] == i)[0]
        #date = data[d]['Date']
        if len(d) < 6:
            #print('non', data[d]['id'])
            mjd_max[d] = 0
        else :
            #print('oui', data[d]['id'])
            dmax = data['Date'][d][np.where(data[d]['Flux'] == data[d]['Flux'].max() )[0]]
            mjd_max[d] = dmax.min()
            #print(data['Date'][d], dmax, mjd_max)
            #544(233)
        
    date_red = data['Date'] - mjd_max
    #234(23)
    #print(date_red)
    #for i_date in date-red:
        #if i_date > 0. :
            
    idx = (date_red < -mjd_moins) ^ (date_red > mjd_plus) 
    #3432(234)
    """if len(d) < 6:
            continue
        else:
            id_fmax = np.where(d['Flux'] == d['Flux'].max())[0][0]
            idx_sn = np.where(data['id']==d['id'][0])[0]
            
            if id_fmax != 0:
                if id_fmax >= n_pt:
                    for ii in idx_sn[id_fmax - n_pt : id_fmax + n_pt + 1]:
                        idx.append(ii)
                else:
                    for ii in idx_sn[: id_fmax + n_pt + 1]:
        idx.append(ii)
    """    
    data = data[~idx]

    len_data = np.zeros_like(data['Date'], dtype = bool)
    for i in np.unique(data['id']):
        d = np.where(data['id'] == i)[0]
        if len(d) < 6:
            len_data[d] = False
        else :
            len_data[d] = True

    data = data[len_data]

    
    #reduced data
    idin_sn = [] 
    for i in range(len(data)):
        if data['id'][i] in data['id']:
             idin_sn.append(i)
    un = np.unique(data['id'])                     
    for i in range(len(un)):
        idex0 = data['id'] == un[i]
        data['id'][idex0] = i    
    data['Flux'] *= 10**6 
    data['FluxErr'] *= 10**6    
    sn_sum = np.load('work/snls5/' + survey + '_lc_summary.npy')
    return data , sn_sum['SN'][un]#init_data, data[idin_sn], sn_sum['SN'][un]


def sn_csp():
    fi = open('work/snls5/studies/samples_selection/CSP/LC/DR3/tab1.dat')
    ligne = fi.readlines()

    keys = [('SN', '|S20'), ('ZHelio', float)]
    sn = np.zeros(len(ligne[1:-7]), dtype = keys)
    
    p = re.compile(r'\t+')
    dicti = dict()                                                       
    c =  0
    for i in ligne[1:-7]:
        v = p.split(i)
        sn[c] = v[0], v[5]
        c +=1
    return sn


def find_sn(survey = 'csp'):
    xdata = np.load('work/snls5/' + survey + '_lc.npy')
    filter = np.unique(xdata['Filter'])
    wi = np.zeros(len(filter), dtype = [('band', '|S20'), ('SNe', list)])
    c = 0                       
    for i in filter:
        print(i)
        data, sn,  un = data_cons(band = i)
        s, data, model, cons, B, M = fit_sqp(data = data, C = [1., 0., 10.], max_iter = 250, n_theta = 30, band=i)
        wi[c] = i, snw
        c += 1
    return wi
