import numpy as np
import pylab as pl
from nacl.models.regularizations import NaClSplineRegularization
from nacl import minimize
import helpers

tds, model = helpers.generate_dataset(2, seed=42)


def test_regularization_minimization(to_regularize=['M0']):
    """
    """
    model.pars.fix()
    for block_name in to_regularize:
        model.pars[block_name].release()

    reg =NaClSplineRegularization(model, to_regularize=['M0'])
    minz = minimize.Minimizer(reg)
    minz(model.pars.free)
    return reg, minz



