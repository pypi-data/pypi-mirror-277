import numpy as np
import pylab as pl
from nacl.models.constraints import SALT2LikeConstraints
from nacl import minimize
import helpers

tds, model = helpers.generate_dataset(10, seed=42)


def test_constraint_instantiation():
    """
    """
    cons = SALT2LikeConstraints(model, active={'M0': 1.}, mu=1.E10)
    v, grad, H = cons(model.pars.free, deriv=1)


def test_constraint_minimization(active={'M0': 1.}):
    """
    """
    model.pars.fix()
    for block_name in active:
        model.pars[block_name].release()

    cons = SALT2LikeConstraints(model, active=active, mu=1.E10)
    minz = minimize.Minimizer(cons)
    res = minz(model.pars.free)

    return res, minz
