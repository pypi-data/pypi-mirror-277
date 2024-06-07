import numpy as np
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
from astroquery.simbad import Simbad
import scipy 


# first model :                                                                                                                                                                          
# $$ y_{sn,t_{mjd}} = f_{sn} \times S\left(\frac{t_{mjd} - t_{max}}{1+s_{sn}}; \theta_{splines} \right) $$                                                                               

theta_range = [-35, 35]

customSimbad = Simbad()
customSimbad.remove_votable_fields('coordinates')
customSimbad.add_votable_fields('sptype')


class SModel(object):
    """
    Model of Type Ia supernova light curve :
    $$ y_{sn,t_{mjd}} = f_{sn} \times S\left(\frac{t_{mjd} - t_{max}}{1+s_{sn}}; \theta_{splines} \right) $$
    """
    def __init__(self, xdata, rng_spline = theta_range, grid_size = 10):
        self.nb_sn = len(np.unique(xdata['id']))
        self.spline_basis = CardinalBSplineC(grid_size, rng_spline)
        self.xdata = xdata
        self.n_theta = grid_size
        self.pars = self.init_pars(xdata) #self.para_init(xdata)

    def init_pars(self, xdata):
        p = [("flux", self.nb_sn), ("tmax", self.nb_sn), ("s", self.nb_sn), ("theta", len(self.spline_basis))]
        p = FitParameters(p)
        p['flux'].full[:] = [100.] * self.nb_sn
        p['s'].full[:] = [0.] * self.nb_sn
        #p['flux'].fix(0, val=100.) 
        p['s'].fix(0, val=0.)
        
        for i in range(self.nb_sn):
            idx = xdata['id'] == i
            tmax = (xdata[idx]['Date'] * xdata[idx]['Flux']).sum() / xdata[idx]['Flux'].sum()
            tmax = xdata[idx]['Date'].sum() / idx.sum()
            p['tmax'].full[i] = tmax 
            p['flux'].full[i] = xdata[idx]['Flux'][np.where(xdata[idx]['Flux'] == xdata[idx]['Flux'].max())]#
            if i ==0:
                p['tmax'].fix(0)
                p['flux'].fix(0)
        
        p['theta'].full[:] = self.theta_init(xdata)
        return p
    
    def theta_init(self, xdata, plot = False):
        #dat = generate_Lc(1)
        data = xdata[xdata['id'] == 0]
        #phase = dat['Date'] - dat['Date'][dat['Flux'] == np.unique(dat['Flux']).max()]
        phase = data['Date'] - data['Date'][data['Flux'] == np.unique(data['Flux']).max()]
        y = data['Flux']/max(data['Flux'])
        jacobian = self.spline_basis.eval(phase)
        H = jacobian.T * jacobian + 0.01 * diags(np.ones(jacobian.shape[1]))
        factor = cholesky(H.tocsc())
        if plot:
            pl.figure()
            pl.plot(data['Date'], y, 'b.')
            pl.plot(data['Date'], jacobian*factor(jacobian.T * y), 'k.')
            pl.show()
        return factor(jacobian.T * y)
        
        
    def __call__(self, p, jac=False, xdata=None):
        if xdata is None:
            xdata = self.xdata
        
        self.pars.free = p
        ide = xdata['id']
        sp1 = (1. + self.pars['s'].full[ide])
        phases = (xdata['Date'] - self.pars['tmax'].full[ide]) / sp1 #(sp1* (1 + xdata['ZP']))

        flx = self.pars['flux'].full[ide]
        jacobian = self.spline_basis.eval(phases)
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
            val_t = self.pars['flux'].full[ide] * (-1/sp1) * (dB * self.pars['theta'].full) #(-1/(sp1 * (1 + xdata['ZP']))) * (dB * self.pars['theta'].full)

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
            Jac = coo_matrix((val_jac[idx_fix], (i[idx_fix],j[idx_fix])), shape = (N, len(self.pars.free)))
                                                                                                                                                                                         
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
        """
        Initialisation of the parameters of the model.
        the parameter v represent the standard deviation : sigma = np.sqrt(variance), one per Supernova

        Input :  

        Output : FitParameters, class of parameter
        """
        fp = [("v", self.nb_sn)]
        fp = FitParameters(fp)
        fp['v'] = 0.1 #* 50**2 #* np.arange(self.nb_sn) + np.arange(self.nb_sn)**2
        return fp

    def __call__(self, value, p, J=None):
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
        if J == None:
            if self.lab == 'cst':
                return np.diag(p[ide]**2) #np.diag(p[ide]) 
            else :
                return np.diag((p[ide]*(value))**2) #np.diag(p[ide]*(value)**2)
        else :
            N = self.nb_theta + 4 * self.nb_sn
            n = len(value)
            isn = np.arange(n)

            # derive parametre de J:
            ii_J = J.col
            jj_J = J.row
            if self.lab == 'cst':
                val_J = np.zeros((len(J.data))) #2 * value[ide[J.row]] * J.data * p[ide[J.row]]
            else :
                val_J = 2 * value[ide[J.row]] * J.data * p[ide[J.row]]**2

            # derive V_{n}:
            ii_v = J.shape[1] + ide
            jj_v = isn
            if self.lab == 'cst':
                val_v = np.ones(len(value)) #value**2
            else :
                val_v = 2 * p[ide] * value**2
                
            i = np.hstack((ii_J, ii_v))
            j = np.hstack((jj_J, jj_v))
            val_jac = np.hstack((val_J, val_v))

            dV = coo_matrix((val_jac, (i,j)), shape = (N, n))
            if self.lab	== 'cst':
                return np.diag(p[ide]**2), dV #*(value)**2), dV
            else :
                return np.diag((p[ide]*(value))**2), dV


def generate_Lc(N, sigma_err, variance_sn, rng = [-70, 180], plot=False, lab = 'cst'):
    """
    Creation of SN light curves as gaussian. Here each tmax, stetch and maximum of the flux are the same for all SNe, but variation can be uncomment.

    Input : - N = int, is the number of SN light curves wanted.
            - sigma_err = float, is the measure error wanted on each point (can be change with a standard deviation if needed).
            - variance_sn = float, is the variance wanted on each SN, that we want to model with the Variance model.
            - rng = list , is the range of time, expressed in days
            - plot = bool, to plot the light curves
            - lab = str, to have a 'cst' (constant) variance for all SN, or a variance dependent of the flux. 

    Output : - Data = NTuple, is the new light curves.
    """
    x,y,yerr = [], [], []
    ide = []
    for i in range(N):
        tmax = 0. #np.random.uniform(theta_range[0]+15, theta_range[1]-15) #rng[0], rng[1]) #0.
        sig = 5. #np.random.uniform(1., 10.) #5.
        norm = 100. #np.random.uniform(50., 1000.) #100.

        npts = np.random.randint(5,8)*2+1
        
        xx = np.linspace(-20, 20, npts) #np.random.uniform(-3*sig, 3*sig, size=npts)
        yy = norm * np.exp(-0.5 * (xx/sig)**2)
        xx += tmax
        yy_err = sigma_err #np.random.normal(scale= sigma_err, size=len(yy))
        if lab == 'cst':
            yy += variance_sn #np.random.normal(scale=np.sqrt(0.1), size=len(yy)) #* yy**2) , size=len(yy)) 
        else :
            yy += np.random.normal(scale=np.sqrt((0.1 * yy)**2) , size=len(yy)) 
        x.append(xx)
        y.append(yy)
        ide.append(np.full(len(xx), i))
        yerr.append(np.full(len(xx), yy_err))

    x = np.hstack(x)

    data = NTuple(len(x),dtype=[('Date', float), ('Flux', float), ('FluxErr', float),('id',int)])
    data['Date'] = np.hstack(x)
    data['Flux'] = np.hstack(y)
    data['FluxErr'] = np.hstack(yerr)
    data['id'] = np.hstack(ide)
    
    if plot :
        for i in np.unique(data['id']):
            idx = data['id'] == i
            tmax = data['Flux'][idx].max()
            phase = data['Date'][idx]
            pl.errorbar(phase, data['Flux'][idx], yerr=data['FluxErr'][idx], fmt='.')

    return data



def hessian(x, w, p, g, J, dV, reml):
    """
    Create Hessian matrix needed to minimized the chi2, in order to fit models of light curves and variances on data, using Newton-Raphson's method.
    Appearing on the left hand side of the equation.
 
    Input : - x = Array, is the 'Date' of the given light curve measurements.
            - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(x) * len(x)).
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
    
    def hess_reml(n, m, x = x, dV = dV.toarray(), w = w):
        """
        calculate the reml additional term the appears in the minimization of the chi2.
        NOT use for now.
        """
        X = np.diag(x+1)
        kl = np.linalg.inv(np.linalg.multi_dot((X.T, w.toarray(), X)))
        inte = np.linalg.multi_dot((np.diag(dV[n]), w.toarray(), X, kl, X.T, w.toarray(), np.diag(dV[m]))) + np.linalg.multi_dot((np.diag(dV[n]), w.toarray(), np.diag(dV[m]))) + np.linalg.multi_dot((np.diag(dV[m]), w.toarray(), np.diag(dV[n])))
        hess = np.linalg.multi_dot((kl, X.T, w.toarray(), inte, w.toarray(), X))
        return hess.trace()
    
    def trace(i, j, w = w, dV = dV, reml = reml):
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
        dVi = coo_matrix(np.diag(dV[i]))
        dVj = coo_matrix(np.diag(dV[j]))
        aj = 0
        if reml :
            aj = hess_reml(i, j)
        return (w * dVi * w * dVj).toarray().trace() + aj

    npar = p.shape[0] + g.shape[0]
    Tr = np.array([trace(i,j) for i in range(npar) for j in range(i, npar)])
    ii = [i for i in range(npar) for j in range(i, npar)]
    jj = [j for i in range(npar) for j in range(i, npar)]
    
    H_l = coo_matrix((np.hstack((Tr,Tr)), (np.hstack((ii,jj)), np.hstack((jj, ii)))), shape = ( npar, npar))
    H_l = coo_matrix((np.hstack((H_l.data, -np.diag(H_l.toarray())/2.)), (np.hstack((H_l.row, range(H_l.toarray().shape[0]))), np.hstack((H_l.col, range(H_l.toarray().shape[0]))))), shape = (npar,npar))
    H = coo_matrix((H00, (i00, j00)), shape = ( npar, npar))
    return H + H_l

def grad(res, x, w, J, dV, p, g, reml):
    """
    Create gradient vector needed to minimized the chi2, in order to fit models of light curves and variances on data, using Newton-Raphson's method.
    Appearing on the right hand side of the equation.  
    
    Input : - res = Array, is the residual of the measurement substracted by the model.
            - x = Array, is the 'Date' of the given light curve measurements.
            - w = Array, is the matrix in which each diagonal element is the inverse variance of the measurement ( size : len(x) * len(x)).
            - J = coo_matrix, is the Jacobian of the Light curev model.
            - dV = coo_matrix, is the Jacobian of the variance model.
            - p = Array, is the parameter of the LIGTH CURVE model.
            - g = Array, is the parameter of the VARIANCE model.
            - reml = bool, if the reml technic is needed.

    Output : - (-1) * resul = Array, the needed gradient vector. 
    """
    def grad_reml(n, x = x, dV = dV.toarray(), w = w):
        """
        Calculate the reml additional term the appears in the minimization of the chi2.
        NOT use for now.
        """
        X = np.diag(x+1)
        kl = np.linalg.inv(np.linalg.multi_dot((X.T, w.toarray(), X)))
        grad = np.linalg.multi_dot((kl, X.T, w.toarray(), np.diag(dV[n]), w.toarray(), X)).trace()
        return - grad

    def grad_theta(i, J = J, res = res, dV = dV, w = w):
        """
        Calculate the term i of the gradient vector.
        
        Input : - i = int, represent the i-th parameter term of the gradient.
  
        Output : - Float, the ith term 
        """
        aj = 0
        if reml :
            aj = grad_reml(i)
        grad = (w.toarray().dot(np.diag(dV.toarray()[i]))).trace() - np.linalg.multi_dot([res.T, w.toarray(), np.diag(dV.toarray()[i]), w.toarray(), res])
        if i < p.shape[0]:
            grad += - 2 * np.linalg.multi_dot([J.toarray().T[i], w.toarray(), res])
        return grad + aj
    resul = np.array([grad_theta(i) for i in range(p.shape[0] + g.shape[0])])
    return -resul

def plot_cl(data, model, p, g, chi2= 'before', lab = 'cst'):
    """
    Plot the light curves data points and the fitted models (of the light curves and the variance).
    
    Input : - data = NTuple, light cruve data.
            - model = SModel, Light curve model.
            - p = Array, light curve model parameters.
            - g = Array, variance model parameters.
            - chi2 = str, 'before' of 'after' the minimization because plots are differents.
            - lab = str, 'cst' or 'dep' labeled the variance dependence on the flux.
    
    Output : the plot of SN light curves (data point and the fit)  with variances (real dependence and the fit one). 
    
    """
    if chi2 =='before':
        fig = pl.figure()
        ax1 = pl.subplot(211)
        ax2 = pl.subplot(212, sharex = ax1)
        phase = data['Date']
        ax1.errorbar(phase, data['Flux'], yerr = data['FluxErr'], marker='.', ls='', color='k')
        for i in np.unique(data['id']):
            d = data[data['id'] == i]
            date = np.linspace(d['Date'].min(), d['Date'].max())
            u = np.full(len(date), i).astype(int)
            d_sn = np.rec.fromarrays((date, u), names=['Date','id'])
            v = model(p, jac=0, xdata=d_sn)
            ax1.plot(d_sn['Date'], v, color=pl.cm.jet(i), ls='-')
        v = model(p, jac=0)
        ax2.plot(phase, data['Flux']-v,'k.')

    
    elif chi2 == 'after':
        fig = pl.figure()
        ax1 = pl.subplot(211)
        ax2 = pl.subplot(212, sharex = ax1)
        phase = data['Date']
        #ax1.errorbar(phase, data['Flux'], yerr = data['FluxErr'], marker='.', ls='', color='k')                                                                                                                       
        for i in np.unique(data['id']):
            d = data[data['id'] == i]
            date = np.linspace(d['Date'].min(), d['Date'].max())
            u = np.full(len(date), i).astype(int)
            err = np.full(len(date), d['FluxErr'][0]).astype(float)
            d_sn = np.rec.fromarrays((date,err,u), names=['Date', 'FluxErr','id'])
            v = model(p, jac=0, xdata=d_sn)
            ax1.errorbar(d['Date'], d['Flux'], yerr = d['FluxErr'], marker='.', ls='', color=pl.cm.jet(i**2 + 10 *i))
            ax1.plot(d_sn['Date'], v, color=pl.cm.jet(i**2 + 10 *i), ls='-', label = str(i), linewidth = 0.5)
            if lab == 'cst':
                ax1.plot(d_sn['Date'], v + 3*(np.sqrt(g[i]**2 + err)), color=pl.cm.jet(i**2 + 10 *i), ls='--', linewidth = 0.5)
                ax1.plot(d_sn['Date'], v - 3*(np.sqrt(g[i]**2 + err)), color=pl.cm.jet(i**2 + 10 *i), ls='--', linewidth = 0.5)
            else : 
                ax1.plot(d_sn['Date'], v + 3*(np.sqrt((g[i] * v)**2 + err)), color=pl.cm.jet(i**2 + 10 *i), ls='--', linewidth = 0.5)
                ax1.plot(d_sn['Date'], v - 3*(np.sqrt((g[i] * v)**2 + err)), color=pl.cm.jet(i**2 + 10 *i), ls='--', linewidth = 0.5)
        ax1.legend()
        v = model(p, jac=0)
        ax2.plot(phase, data['Flux']-v,'k.')
    

#data = generate_Lc(N = 100, sigma_err = 2, npts = 11, lab = lab)
#def fit_sqp_lin(N, sigma_err, max_iter = 100, ll = 0.1, dchi2_min = 0.1, reml = False, lab = 'cst'):
def fit_sqp_lin(data, max_iter = 10, ll = 0.1, dchi2_min = 0.1, reml = False, lab = 'cst', plot = True):
    """
    Minimization of the chi2.
    
    Input : - data = NTuple(['Date', 'Flux', 'FluxErr']), light curves data (if generated with the function above generate_LC, the format is ok).
            - max_iter = int, is the maximum number of iteration wanted.
            - ll = float, help to inverse the hessian matrix, by adding somthing one its diagonal.
            - dchi2_min = float, variation of chi2 desired to reach.
            - reml = bool, to consider the reml technic, NOT use here !
            - lab = str, 'cst' or 'dep' labbeled the variance model dependance on the light curve flux.
            - plot = bool, True will plot SN light curves given by the fonction plot_cl.
    
    Output : - p = Array, the final parameter of the light curve model.
             - g  = Array, the final parameter of the variance model.
    """
    #data = generate_Lc(N = N, sigma_err = sigma_err, npts = 11, lab = lab)
    model = SModel(data)
    var_model = VModel(model.n_theta, data, lab = lab)
    y = data['Flux']
    x = data['Date']
    sig = data['FluxErr']
    
    p = model.pars.free
    g = var_model.pars.free
    dp = np.zeros(p.shape)
    dg = np.zeros(g.shape)

    v, J = model(p, jac = True)
    V, dV = var_model(v, g, J=J)

    variance = np.diag(V) + sig**2
    w = np.diag(1/variance)

    res = y - v
    chi2 = (np.linalg.multi_dot([res.T,w,res]) + len(res) * np.log(np.pi) + np.log(np.diag(w)).sum())/ (len(data) - (p.shape[0] + g.shape[0]))
    Dchi = 0.
    niter = 0

    #plot_cl(data = data, model = model, p = p, g = g, chi2= 'before', lab = lab)
    
    while niter < max_iter:
        v, J = model(p, jac = True)
        V, dV = var_model(v, g, J=J)

        variance = np.diag(V) + sig**2
        w = coo_matrix(np.diag(1/variance))
        
        res = y - v
        H = hessian(x = x, w = w, p = p, g = g, J = J, dV = dV, reml = reml) + ll * diags(np.ones(p.shape[0]+ g.shape[0]))
        resul = grad(res = res, x = x, w = w, J = J, dV = dV, p = p, g = g, reml = reml)

        var = np.linalg.inv(H.toarray()).dot(resul)
        dp = var[:p.shape[0]]
        dg = var[p.shape[0]:]
            
        variance = np.diag(V) + sig**2
        w = np.diag(1/variance)

        # here are the two ways of implementing the line search : the first one, only on the light cures parameters & the second on both models parameters.
        # One can comment or decomment the wanted fonction phi and crit.
        
        """
        def phi(p):
            return ((w * ( y - model(p, jac = False)))**2).sum()

        def crit(t):
            return phi(p + t * dp) 
        """
        vect = np.hstack((p,g))

        def phi(vect, n = len(p)):
            p = vect[:n]
            g = vect[n:]
            val = model(p)
            V = var_model(val, g)
            variance = np.diag(V) + sig**2
            w = coo_matrix(np.diag(1/variance))
            return ((w * ( y - val))**2).sum()

        def crit(t):
            return phi(vect + t * var)
        
        
        t, fval, ni, funcalls = scipy.optimize.brent(crit, brack=(0,1), full_output=True)
        
        p = p + t * dp
        g = g + t * dg

        # if the first line search is choosen, there are the corresponding parameter variations. 
        #p = p + dp                                                                                                                                                                                            
        #g = g + dg

        print('p', p, '\n', 'dp', dp, '\n', 't', t, '\n', 'g', g, '\n', 'dg', dg,'\n')    
        v = model(p, jac=False)                                                                                                                                                                                  
        V = var_model(v, g)                                                                                                                       
        res = y - v

        variance = np.diag(V) + sig**2
        w = np.diag(1/variance)

        new_chi2 = (np.linalg.multi_dot([res.T,w,res]) + len(res) * np.log(np.pi) + np.log(np.diag(w)).sum())/ (len(data) - (p.shape[0] + g.shape[0]))
        dchi2 = new_chi2 - chi2
        logging.info('iter %f : chi2: %f -> %f [dchi2=%f]' % (niter, chi2, new_chi2, dchi2))
    
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
    if plot :
        plot_cl(data = data, model = model, p = p, g = g, chi2= 'after', lab = lab)
    return p, g
    
def control(real = 10, N = 10, sigma_err = 2., variance_sn = 0.01, lab = 'cst', nbins = 25, plot = False):
    """
    Control plot : histogram of the variance parameters for found for all SNe.

    Input : - real = int, number of realisation of the fit.
            - N = int, number of SNe fitting in each "real" realisation.
            - sigma_err = float, measure error we want on the SNe light curves
            - variance_sn = float, variance we want to be modeled by the variance model.
            - lab = str 'cst' or 'dep', type of variance model we want to use.
            - nbins = int, number of bins for the histogram.
            - plot = bool, True if we want to see each Sne light curve plot with the foncion plot_cl.
    
    Output : histogram
    """
    g = []
    for i in range(real):
        data = generate_Lc(N = N, sigma_err = sigma_err, variance_sn = variance_sn, lab = lab)
        p0, g0 = fit_sqp_lin(data, max_iter = 20, lab = lab, plot = plot)
        g.append(g0)

    g = np.array(g)
    pl.figure()
    xh, yh, hh = pl.hist(np.abs(g.ravel()), bins=nbins)#, range = (,0.01))

    med = np.median(g)
    moy = g.mean()

    pl.plot(variance_sn * np.ones(10), np.linspace(0,xh.max(),10), 'r--')
    pl.plot(moy * np.ones(10), np.linspace(0,xh.max(),10), 'k--')
    pl.plot(med * np.ones(10), np.linspace(0,xh.max(),10), 'b--')

    pl.title('%i real  de %i SN : v = %f ( => v_simu moy : %f med : %f)' % (real, N, variance_sn, moy, med))


def plot_regimes(var = [0.001, 0.01, 0.1, 1., 10,], lab = 'dep', real = 10, N = 10):
    """
    plot histogram for the var differents value of the variance_sn of the control function.

    Input : - var, list of float, the variance wanted for the variance_sn of the function control.
            - lab = 'cst' or 'dep', the variance model depnedance on the flux
            - real = int, number of realisation of the fit.
            - N = int, number of SNe fitting in each "real" realisation.
    """
    for i in var :
        control(variance_sn = i, lab = lab, real = real, N = N)
        
    
