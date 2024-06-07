import nacl.simulations.ideal as ideal
from nacl.models.salt import SALT2Like
from nacl.simulations.flux_simulator import Simulator
from nacl.models.variancemodels import SimpleVarianceModel, ColorScatter
from nacl.minimizers import Minimizer
from nacl.fit import FitModel2D
import numpy as np 


N_SN = 500
MU_REG = 10

####################################### SIMULATION ###################################
# Seed                                                                
SEED_SAMPLING, SEED_NOISE, SEED_INIT = 0, 0, 0

# Create the cadence 
DS = ideal.Generator(n_sn=N_SN, lsst_simu=True)

# Simulate the flux and the measurements error
INIT_FROM_SALT2_FILE = "../data/salt2.npz"
# Color Scatter initialisation
SIGMA_KAPPA_INIT = np.array([0.015, -0.02, 0.05])
CS_FUNC = ColorScatter
# Error Snake value used in simulation
# Error snake initiate at 5%
GAMMA_INIT = 0.05
# Covariance calibration matrix 
COV_CALIB = 1e-6

FS = Simulator(DS,                                        # DataSet
               SALT2Like,                                 # Model function used to simulated
               variance_model_func=SimpleVarianceModel,   # Error Snake used in sim
               gamma_init=GAMMA_INIT,                     # Value of the error snake
               seed=SEED_NOISE,                           # Seed for noise generation                
               sigma_kappa_init=SIGMA_KAPPA_INIT,         # Value of Color scatter used in sim
               eta_covmatrix=COV_CALIB,                   # Value of Calibration Covariance Matrix
               color_scatter_func=CS_FUNC,                # Color scatter mmodel func
               init_from_salt2_file=INIT_FROM_SALT2_FILE) # Model values for sim

####################################### FIT #########################################
## Instantiate Fit
# Create Constraints and Regularization
# as function of free parameters.
fit = FitModel2D(FS.trainingDataset,                            # TrainingDataset
                 model_func=SALT2Like,                          # Model used
                 normalization_band_name='SWOPE::B',            # Model normalization
                 init_from_salt2_file=INIT_FROM_SALT2_FILE,     # Files to initiate the model
                 pars_fix=[],                                   # Parameters that should be fixed
                 color_scatter_func=CS_FUNC,                    # Color Scatter fun
                 mu_reg=MU_REG,                                 # Regularization hyperparameter
                 minimizer=Minimizer)                           # Minimizer function

# degrade SN parameters (multiply by N(1, 0.05))
# degrade error snake  (multiply by N(1, 1))

# select SN parameters
pars_fix = ['M0', 'CL', 'M1', 'SpectrumRecalibration', 'eta_calib', 'kappa_color']
# Fix model parameters
fit.pars_fix = pars_fix
fit.pars_release()

# set kappa and eta to zero
fit.model.pars['eta_calib'].full[:] = 0
fit.model.pars['kappa_color'].full[:] = 0

fit.parameter_degradation(model_coef_init=0.05,
                          var_coef_init=0.1,
                          seed=SEED_INIT)
sigma_kappa = SIGMA_KAPPA_INIT.copy()/2.5 

fit.beta = 1e-10
#####################################################################################
################################################### 1st fit model without Error Snake 
fit(pars_fix=['gamma'],
    sigma_kappa=sigma_kappa,
    g=None,
    eta_covmatrix=COV_CALIB,
    sigma_kappa_fit=True)
sigma_kappa = fit.color_scatter.pars.full[:].copy()

################################################### 2nd Fit only error snake
# Release Error Snake parameter
fit.variance_model.pars.release()
fit(pars_fix=fit.all_pars, g=fit.variance_model.pars.free)

################################################### 3rd Fit : All
# Release model parameters
fit.model.pars.release()
fit(pars_fix=[],
    g=fit.variance_model.pars.free, 
    sigma_kappa=sigma_kappa,
    eta_covmatrix=COV_CALIB,
    sigma_kappa_fit=True)
