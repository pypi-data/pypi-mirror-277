import numpy as np
import pylab as pl
from nacl.models.salt import SALT2Like
from nacl import dataset
from nacl.simulations.fullsim import sngen

import helpers

tds, model = helpers.generate_dataset(2, seed=42)


def test_X0_definition():
    """
    Here, we check the normalization of the model.
    Our goal is to clarify the normalization of the model, while
    keeping the overall values of the X0's and the overall values
    of the M0,M1 surfaces not too far away from the original model.
    """
    gen = sngen.DVDzSNGenerator(z_range=(0.001, 0.6))
    sample = gen.generate_sample(nsn=10000)
    jla = dataset.read_hdf('jla.hd5')
    zz = np.linspace(0.001, 0.6, 500)

    # JLA versus d_L(z) values
    pl.figure()
    pl.semilogy(jla.sn_data.z, jla.sn_data.x0, 'k.',
                label="original JLA X0's")
    pl.semilogy(zz, 100. / gen.cosmo.luminosity_distance(zz)**2, 'r--',
                label='$100/d_L^2(z)$')
    pl.semilogy(zz,  80. / gen.cosmo.luminosity_distance(zz)**2, 'c--',
                label='$80/d_L^2(z)$')
    pl.legend(loc='best')
    pl.xlabel('redshift')
    pl.ylabel('X0')
    pl.title('Comparison between the JLA $X_0$ values and $d_L(z)$' )

    # generator versus d_L(z) values
    pl.figure()
    pl.semilogy(sample.z, sample.x0, 'k.',
                label='simulated sample')
    pl.semilogy(zz, 100. / gen.cosmo.luminosity_distance(zz)**2, 'r--',
                label='$100/d_L(z)^2$')
    pl.legend(loc='best')
    pl.xlabel('redshift')
    pl.ylabel('X0')
    pl.title('Comparison between the generator $X_0$ values and $d_L(z)$' )

    return gen, jla


