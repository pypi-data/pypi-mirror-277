import numpy as np
import pylab as pl
from nacl.minimize import WeightedResiduals
import helpers

tds, model = helpers.generate_dataset(2, seed=42)


def check_wres_grad(wres, p, dx=1.E-5):
    v0, jacobian, _ = wres(p, jac=True)
    p0 = p.copy()

    df = []
    for i in range(len(p)):
        p0[i] += dx
        vp = wres(p0, jac=False)
        df.append((vp-v0) / dx)
        p0[i] -= dx
    return np.array(jacobian.todense()), np.vstack(df).T


def test_weighted_residual_derivatives():
    """
    """
    wres = WeightedResiduals(model)
    jac, num_der = check_wres_grad(wres, p=model.pars.free)

    return np.array(jac), num_der
