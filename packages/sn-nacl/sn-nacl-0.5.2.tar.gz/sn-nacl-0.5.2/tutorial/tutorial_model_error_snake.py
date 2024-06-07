import nacl.simulations.ideal as ideal
from nacl.models.salt import SALT2Like
from nacl.simulations.flux_simulator import Simulator
from nacl.models.variancemodels import SimpleVarianceModel
from nacl.minimizers import Minimizer
from nacl.fit import FitModel2D
import numpy as np 

N_SN = 500
MU_REG = 10

####################################### SIMULATION #############################
# Create the cadence 
DS = ideal.Generator(n_sn=N_SN, lsst_simu=True)

# Simulate the flux and the measurements error
INIT_FROM_SALT2_FILE = "../data/salt2.npz"

# Error snake initiate at 5%
GAMMA_INIT = 0.05  
FS = Simulator(DS,                                        # DataSet
               SALT2Like,                                 # Model function used to simulated
               variance_model_func=SimpleVarianceModel,   # Error Snake used in sim
               gamma_init=GAMMA_INIT,                     # Value of the error snake
               init_from_salt2_file=INIT_FROM_SALT2_FILE) # Model values for sim

####################################### FIT ####################################
## Instantiate Fit
# Create Constraints and Regularization
# as function of free parameters.
fit = FitModel2D(FS.trainingDataset,                            # TrainingDataset
                 model_func=SALT2Like,                          # Model used
                 normalization_band_name='SWOPE::B',            # Model normalization
                 init_from_salt2_file=INIT_FROM_SALT2_FILE,     # Files to initiate the model
                 pars_fix=[],                                   # Parameters that should be fixed
                 mu_reg=MU_REG,                                 # Regularization hyperparameter
                 minimizer=Minimizer)                           # Minimizer function

# degrade SN parameters (multiply by N(1, 0.05))
# degrade error snake  (multiply by N(1, 1))
fit.parameter_degradation(model_coef_init=0.05,
                          var_coef_init=0.1)

################################################### 1st fit model without Error Snake 
fit(pars_fix=['eta_calib', 'kappa_color', 'gamma'])

################################################### 2nd Fit
# Release Error Snake parameter
fit.variance_model.pars.release()
fit(pars_fix=fit.all_pars, g=fit.variance_model.pars.free)

################################################### 3rd Fit
# Release model parameters
fit.model.pars.release()
fit(pars_fix=['eta_calib', 'kappa_color'], g=fit.variance_model.pars.free)
