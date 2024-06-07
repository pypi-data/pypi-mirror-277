import os
import os.path as op
import numpy as np

from nacl.models.salt import SALT2Like
from nacl.models import variancemodels
import nacl.models as models
from nacl.simulations.fullsim import cadences, sngen, snsurvey
from nacl.simulations import etc
# from nacl.simulations.flux_simulator import FluxSimulator
from nacl.simulations import FluxSimulator, SpecUncertainties


def locate_test_datafile(fn, dirname='expected', check=False):
    """
    """
    ret = op.join(op.dirname(__file__), dirname, fn)
    if check and not op.isfile(ret):
        raise(FileNotFoundError(ret))
    return ret


def generate_dataset(nsn=10, seed=42, string_ids=True,
                     calib_variance=0., compress=False):
    """generate a model and a training dataset
    """
    # first, we instantiate s SN generator
    # it generates the SN distribution, according to the chosen cosmology
    gen = sngen.DVDzSNGenerator(string_ids=string_ids,
                                alpha=-0.13, beta=3., sigma_int=0.1)

    # using this generator, we generate a supernova sample
    sample = gen.generate_sample(nsn=nsn)

    # then, we need to observe these supernovae,
    # to generate follow-up data. We generate the
    # main survey cadence...
    cad = cadences.MetronomicCadenceFactory(cadences.lsst_ddf_ideal,
                                            n_fields=1)
    obslog = cad()

    # then, we instantiate the survey class.
    # i.e. something that,
    survey = snsurvey.FieldBasedSNSurvey(sample, obslog,
        visits=[snsurvey.StandardSpectroscopicObservations()])

    # and generate the training dataset
    # at this stage, we have not generated the fluxes yet.
    training_dataset = survey.observe()
    
    # mag sky values are a little too optimistic
    # TODO: move this hack somewhere else
    training_dataset.lc_data.nt['mag_sky'] -= 1.5
    training_dataset.lc_data.nt['seeing'] = 1.

    # now, instantiate a model
    # model = SALT2Like(training_dataset,
    #                   init_from_salt2_file='salt2.npz',
    #                   normalization_band_name='SWOPE::B',
    #                   error_snake_model_type=variancemodels.SimpleErrorSnake)
    #                   # calib_variance=calib_variance)
    model = models.get_model(training_dataset)
    model.init_pars()
    model.init_from_training_dataset()
    
    # generate an instance of the training dataset
    fs = FluxSimulator(model)
    fs.model.pars['sigma_snake'].full[:] = 0.05
    fs.update(p=model.pars.free, 
              phot_etc=etc.find('LSST'),
              spec_etc=SpecUncertainties(),
              phot_uncertainty_pedestal=None) # was 0.01
    tds = fs()

    # and instantiate a model around it
    tds_model = SALT2Like(tds,
                          init_from_salt2_file='salt2.npz',
                          normalization_band_name='SWOPE::B',
                          error_snake_model_type=variancemodels.SimpleErrorSnake)
    tds_model.init_from_training_dataset()
    tds_model.pars['sigma_snake'].full[:] = 0.05

    # and simulate the fluxes
    # fs = FluxSimulator(model, seed=seed, salt2_filename='salt2.npz',
    #                    instrument_model=etc.find('LSST'),
    #                    calib_scatter=model.calib_scatter,
    #                    color_scatter=model.color_scatter,
    #                    error_snake=model.error_snake)
    # fs.load_truth_from_tds()
    # fs.update_fluxes()
    # fs.update_photometric_uncertainties()
    # fs.update_spectroscopic_uncertainties()
    # fs.add_measurement_noise()

    # remove failed measurements ?
    if compress:
        training_dataset.compress()
        model = SALT2Like(training_dataset,
                          init_from_salt2_file='salt2.npz',
                          normalization_band_name='SWOPE::B',
                          error_snake_model_type=variancemodels.SimpleErrorSnake)
        model.init_pars()

    return tds, tds_model


def check_grad(model, p):
    """
    """
    v,jacobian = model(p, jac=True)
    dx = 1.E-7
    p0 = p.copy()
    df = []
    for i in range(len(p)):
        p[i] += dx
        vp = model(p, jac=False)
        df.append((vp-v)/dx)
        p[i] -= dx
    return np.array(jacobian.todense()), np.vstack(df).T


def check_deriv(pen, p):
    """
    """
    v, grad, hess = pen(p=p, deriv=True)
    dx = 1.E-5
    p0 = p.copy()

    df =[]
    for i in range(len(p0)):
        p0[i] += dx
        # vp = pen(p0, deriv=False)-
        p0[i] -= (2*dx)
        vm = pen(p0, deriv=False)
        df.append((vp-vm)/(2*dx))
        d2f.append((vp - 2*v + vm)/dx**2)
        p0[i] += dx
    return np.array(grad), np.vstack(df).T


def check_grad_var(func, p, g):
    """
    """
    h = 1.e-7
    val0, J0 = func.model(p, jac = True)
    v0, V0 = func.VarianceModel(g, p, jacobian = J0)#val0,

    df = []
    dmod = []
    for i in range(len(p)+len(g)):
        #print(i)
        if i < len(p):
            p[i] += h
        else :
            g[i-len(p)] += h

        val1 = func.model(p)
        v1 = func.VarianceModel(g, p)#val1,
        #print(i)
        dv = (v1-v0)/h
        #print(V0.tocsr()[i].toarray().squeeze(), dv)
        #np.testing.assert_allclose(V0.tocsr()[i].toarray().squeeze(), dv, rtol=1.E-2)
        df.append(dv)
        if i < len(p):
            dmod.append((val1-val0)/h)
        if i < len(p):
            p[i] -= h
        else :
            g[i-len(p)] -= h

    return V0.todense(), np.vstack(df).T, J0.todense(), np.vstack(dmod).T
