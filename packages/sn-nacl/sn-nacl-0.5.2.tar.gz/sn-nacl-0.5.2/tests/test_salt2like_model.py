import numpy as np
import pylab as pl
from nacl.models.salt import SALT2Like
from nacl import dataset
from nacl.simulations.fullsim import sngen

import helpers

tds, model = helpers.generate_dataset(2, seed=42)


def test_model_normalization():
    """
    check the model normalization, i.e. check that
      - with the definition of X0 as (10Mpc)^2/d_L^2(z)
      - with the definition of the model normalization
    we can reproduce, at 0th order, the JLA light curves
    """
    # gen = sngen.DVDzSNGenerator(z_range=(0.001, 0.6))
    # sample = gen.generate_sample(nsn=10000)
    jla = dataset.read_hdf('jla.hd5')
    # zz = np.linspace(0.001, 0.6, 500)
    model = SALT2Like(jla,
                      init_from_salt2_file='salt2.npz',
                      init_from_training_dataset=True)

    return model

def test_salt2like_derivatives(block_name=None):
    """
    """
    if block_name is None:
        model.pars.release()
    else:
        model.pars.fix()
        model.pars.release(block_name)

    v, J = model(model.pars.free, jac=True)

    jac, num_der = helpers.check_grad(model, model.pars.free)

    return np.array(jac), num_der
