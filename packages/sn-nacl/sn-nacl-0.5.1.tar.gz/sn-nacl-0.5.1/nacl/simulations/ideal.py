import numpy as np
from ..dataset import TrainingDataset
from ..util import salt2

from math import *
import astropy.cosmology as cosmology



def perret_rate(z):
    """The SNLS SNIa rate according to (Perret et al, 201?)
    """
    rate = 0.17E-4
    expn = 2.11
    my_z = np.copy(z)
    my_z[my_z>1.] = 1.
    return rate * np.power(1+my_z, expn)


class Generator(object):
    r"""
    Data generator.
    Generate ideal simulation.

    * Parameters of SNe
    For a fixed number of supernovae, we uniformly draw redshifts between :math:`z = 0.001` and :math:`z = 0.8`
    by default.
    The training batches are truncated in redshift with respect to the cosmological batches
    in order to have a complete training batch, without selection bias.

    Once the redshifts are obtained, we compute the luminosity distance defined as :

    .. math::
        d_L(z) =  c\int^{z}_{0} \frac{d\tilde{z}}{H(\tilde{z})} (1+z)

    where :

    .. math::
        H^{2}(z) = H_0^2 \left[ \Omega_{m} (1+z)^3 + \Omega_{r} (1+z)^4 +  \Omega_{k} (1+z)^2 +
        \Omega_{DE} (1+z)^{3(1+w)} \right]

    Our fiduciary cosmology is the following Flat$-\Lambda$CDM cosmology~:
    with :

    .. math::
         \bullet \, & H_0 = 70, \mathrm{km.s^{-1}.Mpc^{-1}} \\
         \bullet \, & \Omega_m = 0.25 \\
         \bullet \, & w = -1 \\
         \bullet \, & \Omega_DE = 0.75 \\
         \bullet \, & \Omega_k = 0. \\
         \bullet \, & \Omega_\gamma = 5*10^{-5} \\

    Once the distances are known, we can simulate the eigen-parameters of the SNe.
    We first generate the values of :math:`X_1` and :math:`c` according to the two following normal laws~:

    .. math::
        X_1 \sim \mathcal{N}(0, 1.) \quad \quad \quad c \sim \mathcal{N}(0, 0.1)

    then we calculate :math:`X_0` according to the following formula:

    .. math::
        X_0 = \frac{10^{-4}}{d_L(z)^2} 10^{-0.4 (\tilde{M}_{B^\star} - \alpha X_1 + \beta c)}

    The factor :math:`10^{-4}` corresponds to the passage of the square of the luminosity
    distance from :math:`kpc^2 \,  to \, pc^2`.
    For the standardization parameters, we take those determined by the JLA~ analysis:

    .. math::
         \bullet \, & M_{B^\star} = -19.0906 \\
         \bullet \, & \alpha = 0.13 \\
         \bullet \, & \beta = 3 \\

    If LSST survey is simulated filters are : :math:`u, g,r,i,z`
    If not, observing band depend on the z.
    If :math:`z` < 0.05, bands are u, B, V and r from the SWOPE instrument.
    If 0.05 < :math:`z` < 0.2, they are griz from SDSS's instrument.
    and if 0.2 < :math:`z`, bands are griz of Megacam.


    Attributes
    ----------
    n_sn : int
        Number of SNe generated
    n_sp_sn : int
        Number of Spectra per sn, common to all sne.
    n_lc_sn : int
        Number of light curve POINT per sne, common to all light curves.
    n_band : int
        Number of different filter use (only not LSST)
    lc : numpy.rec.array
        Light curves data with data_type as type.
    sp : numpy.rec.array
        Spectral data, with data_type as type.
    z : numpy.array
        Redshift of each data point (photometric then spectroscopic)
    cosmo : astropy.cosmology.FlatLambdaCDM
        Cosmology
    Mb : float
        SN Ia absolute magnitude
    alpha : float
        Parameter of brighter-slower relation
    beta : float
        Parameter of brighter-bluer relation
    flux_at_10pc : float
        Flux of SN observed at 10 pc.
    X0_norm : float
       Model overall X0 normalisation.
    snInfo : numpy.rec.array
        Array of SNe information (:math:`z`, :math:`tmax`, :math:`x1`, :math:`x0`, :math:`c`)
    n_filter : int
        Number of different filter use (only not LSST)
    bands : list
        Bands used in the survey.
    remove_band : list
        if band should be removed.
    lsst_simu : bool
        if sample generated using LSST filter.
    seed : int
        Seed for cadence.
    z_range : list
        Redshift range for the training sample
    data_type : list
        NaCl data type.
    snInfo_type : list
        Type of information of SNe.
    sigma_lc : float
        Dispersion of photometric data (only not LSST)
    sigma_sp : float
        Dispersion of spectral data.
    trainingDataset: nacl.dataset.TrainingDataset
        Data set of photometric and spectroscopic observations.
    """

    def __init__(self, n_sn, n_sp_sn=1, n_lc_sn=20, n_band=4,
                 z_range=[0.01, 0.85], remove_band=[],
                 lsst_simu=True, seed=0, sigma_lc=0.05, sigma_sp=0.02,
                 date_evenly_sparse=False):
        """
        Constructor - computes the arguments

        Parameters
        ----------
        n_sn : int
            Number of SNe generated
        n_sp_sn : int
            Number of Spectra per sn, common to all sne.
        n_lc_sn : int
            Number of light curve POINT per sne, common to all light curves.
        n_band : int
            Number of different filter use (only not LSST)
        z_range : list
            redshift range for the training sample
        remove_band : list
            if band should be removed.
        lsst_simu : bool
            if sample generated using LSST filter.
        seed : int
            Seed for cadence.
        sigma_lc : float
            Dispersion of photometric data (only not LSST)
        sigma_sp : float
            Dispersion of spectral data.
        date_evenly_sparse :
            If observation date are uniformly distributed.
        """
        self.nb_sn = n_sn
        self.n_filter = n_band
        
        self.n_sp_sn = n_sp_sn
        self.n_lc_sn = n_lc_sn

        self.lc, self.sp, self.z = None, None, None
        self.cosmo = None
        self.Mb, self.alpha, self.beta = None, None, None
        self.flux_at_10pc, self.X0_norm = None, None
        self.snInfo, self.n_filter, self.bands = None, None, None

        # for LSST
        self.lsst_simu = lsst_simu
        self.remove_band = remove_band
        self.bands_survey()
        
        self.seed = seed
        np.random.seed(self.seed)
        
        self.z_range = z_range
        self.data_type = [('Date', '<f8'), ('Flux', '<f8'), ('FluxErr', '<f8'),
                          ('Filter', '|S20'), ('Wavelength', '<f8'), ('MagSys', '|S20'),
                          ('ZHelio', '<f8'), ('sn_id', '<i4'), ('spec_id', '<i4')]
        self.snInfo_type = [('z', '<f8'), ('tmax', '<f8'), ('x1', '<f8'),
                            ('x0', '<f8'), ('c', '<f8')]

        self.init_info()
        # print("0", self.snInfo['x1'].sum())
        self.init_photometric_data()
        # print("1", self.snInfo['x1'].sum())
        self.init_spectral_data(date_evenly_sparse)
        # print("2", self.snInfo['x1'].sum())
                
        self.sigma_sp = sigma_sp
        self.sigma_lc = sigma_lc
        self.indexing()
        self.trainingDataset = TrainingDataset(self.lc, self.sp, self.snInfo)

    def indexing(self):
        """
        Reindex spectral ('spec_id', 'sn_id') and photometric data ('band_id', 'lc_id', 'sn_id'),
        when data have been removed.
        """
        n_lc, n_sp = len(self.lc), len(self.sp)
        # band indexation
        dict_bd = {}
        _, idx_bd = np.unique(self.lc['Filter'], return_index=True)
        for i_bd, bd in enumerate(self.lc['Filter'][np.sort(idx_bd)]):
            dict_bd[bd] = i_bd
        id_bd = np.array([dict_bd[bd] for bd in self.lc['Filter']])

        # light curve indexation
        c = 0
        id_lc = np.ones(len(self.lc['Flux']))
        
        for i in range(self.lc['sn_id'][-1]+1):
            idx_sn = self.lc['sn_id'] == i
            lcs = self.lc[idx_sn]
            _, idx = np.unique(lcs["Filter"], return_index=True)
            for bd_sn in lcs['Filter'][np.sort(idx)]:
                id_lc[(self.lc['sn_id'] == i) & (self.lc['Filter'] == bd_sn)] = c
                c += 1
        
        id_lc = np.hstack(np.array(id_lc))
        self.lc = np.lib.recfunctions.rec_append_fields(self.lc, names=['lc_id', 'band_id', 'i'],
                                                        data=[id_lc.astype(int), id_bd, np.arange(n_lc)])
        i_sp = n_lc + np.arange(n_sp)
        sp_ones = np.ones_like(i_sp)
        self.sp = np.lib.recfunctions.rec_append_fields(self.sp, names=['lc_id', 'band_id', 'i'],
                                                        data=[-1*sp_ones, -1 * sp_ones, n_lc+np.arange(n_sp)])

    def init_info(self, tmax_dist=[15., 30.], x1_dist=[0, 1], c_dist=[0, .1]):
        r"""
        SN parameters initialisation:
        :math:`X_1` : follow a centred and reduced normal distribution,
        :math:`c` : follow a centred normal distribution of std = 0.1,
        :math:`t_{max}` : follow in uniform distribution between 15 and 30 MJD,
        :math:`z` : follow also a uniform distribution.

        :math:`X_0`, is defined, using the other parameters, as follow :
                
        .. math:
            X_0 = 10^{-0.4(M_b-\alpha x1 + \Beta c )} \frac{(10pc)^2}{d_L^2(z)}

        dL is calculated following a flat :math:`\Lambda CDM` and
        :math:`M_b`, :math:`\alpha`, :math:`\beta` are taken from JLA.
        """
        n_sn = self.nb_sn
        np.random.seed(self.seed)
        z = np.random.uniform(self.z_range[0], self.z_range[1], size=floor(n_sn))
        
        #        self.cosmo.comoving_volume()
        

        color = np.random.normal(c_dist[0], c_dist[1], size=n_sn)
        sig = np.random.normal(x1_dist[0], x1_dist[1], size=n_sn)
        sig /= sig.std()
        print('X1 removing mean and correct from standard deviation; \n c removing mean')
        sig -= sig.mean()
        color -= color.mean()
 
        np.random.seed(self.seed)
        tmax = np.random.uniform(tmax_dist[0], tmax_dist[1], size=n_sn)
        self.cosmo = cosmology.FlatLambdaCDM(H0=70, Om0=0.25)
        dl = np.array(self.cosmo.luminosity_distance(z)) * 1.E3 # from Mpc to kpc
        self.Mb = -19.0906
        self.alpha = 0.13
        self.beta = 3.0

        self.flux_at_10pc = np.power(10., -0.4 * self.Mb)
        self.X0_norm = self.flux_at_10pc * 1.E-4  # from kpc^2 to (10pc)^2
        norm = self.X0_norm / dl**2
        norm *= np.power(10., 0.4*(self.alpha*sig - self.beta*color))

        self.snInfo = np.rec.fromarrays((z, tmax, sig, norm.ravel(), color),
                                        names=['z', 'tmax', 'x1', 'x0', 'c'])
        self.z = z
        print(f"color m : {np.mean(self.snInfo['c'])}, s : {np.std(self.snInfo['c'])}")
        print(f"x1 m : {np.mean(self.snInfo['x1'])}, s : {np.std(self.snInfo['x1'])}")

    def init_spectral_data(self, date_evenly_sparse,
                           range_spectra=[2000, 11000]):
        r"""
        Observation initialisation, each spectra range is drawn 
        from an int between 2000 and 5000, 
        finish between 6000 and 9000 math:`\AA`.
        Observation date follow a centred normal distribution of std = 10 days.

        The resolution is constant and equal to 10 math:`\AA`.
        Each spectrum is transform in observer frame, by multiplying
        the wavelength by a factor math:`1+z` and adding to the observation date, math:`t_{max}` and 
        times math:`1+z`

        Parameters
        ----------
        date_evenly_sparse : bool
             If observation spectral date should be uniformly distributed.
             Else follow gumbel distribution.
        range_spectra : list,
             range of generated spectra
        """
        n_sn = self.nb_sn
        np.random.seed(self.seed)
        
        nsp = np.random.randint(self.n_sp_sn, self.n_sp_sn + 1, size=n_sn)
        sn_sp = np.array([[i]*nsp[i] for i in range(n_sn)]).ravel()

        date_sp, wave_sp, zhelio_sp, obs_id_sp, sn_id_sp = [],  [], [], [], []
        dates = np.linspace(-20, 45, nsp.sum())  # 50
        np.random.shuffle(dates)
            
        for i in range(len(sn_sp)):
            r0 = np.random.randint(range_spectra[0], 3000)  # 5000
            r1 = np.random.randint(8000, range_spectra[1])  # 6000
            n_pts_wl = ceil((r1-r0)/10) 

            wave_sp.append(np.linspace(r0, r1, n_pts_wl))
            # if date_evenly_sparse:
            #     date_sp.append([dates[i]] * n_pts_wl)
            # else:
            ddate = np.random.gumbel(-2, 8., 1)
            if (ddate > 35) ^ (ddate < -15):  # 35
                # print(ddate[0])
                # print('\n removing spectra bigger than 35 smaller than -15 !!! \n')
                # np.random.seed(self.seed)
                ddate = np.random.normal(0, 5, 1)
                # print(ddate[0])                    
            date_sp.append([ddate[0]] * n_pts_wl)  # np.random.normal(3, 15, 1)[0]] * n_pts_wl)
                
            obs_id_sp.append([i] * n_pts_wl)
            sn_id_sp.append([sn_sp[i]] * n_pts_wl)
            
        sn_id_sp = np.hstack(sn_id_sp)
        zhelio_sp = self.z[sn_id_sp]
        # date_sp = (np.hstack(date_sp) + self.snInfo['tmax'][sn_id_sp]) * (1 + zhelio_sp)
        date_sp = (np.hstack(date_sp)) * (1 + zhelio_sp) + self.snInfo['tmax'][sn_id_sp]
        wave_sp = np.hstack(wave_sp) * (1 + zhelio_sp)
        obs_id_sp = np.hstack(obs_id_sp)
        
        sp_none = np.array([b''] * len(date_sp))       
        flux_sp = np.zeros_like(date_sp)
        
        self.sp = np.rec.fromarrays((date_sp, flux_sp, flux_sp,  sp_none, wave_sp,
                                     sp_none, zhelio_sp, sn_id_sp, obs_id_sp),
                                    dtype=self.data_type)

    def init_photometric_data(self):
        r"""
        Initiate photometric cadence. For each SN n_band band of observation, depending on the redshift
        or common and equal to LSST bands.

        Date of observation are evenly sample between -15 and 30 days, with a gaussian noise. 
        """
        n_sn = self.nb_sn
        self.n_filter = self.n_filter
        
        nlc = np.random.randint(self.n_lc_sn, self.n_lc_sn + 1, size=n_sn)
        sn_lc = np.array([[i] * nlc[i] * self.n_filter for i in range(len(nlc))]).ravel()
        zhelio_lc = self.z[sn_lc]
        # date_lc = (np.array([[ii for ii  in np.linspace(-15,30,nlc[i]) + np.random.normal(0, 0.5, 1)]*
        # self.n_filter for i in range(len(nlc))]).ravel() + self.snInfo['tmax'][sn_lc]) * (1 + zhelio_lc)
        date_lc = (np.array([[ii for ii in np.linspace(-15, 35, nlc[i]) + np.random.normal(0, 0.5, 1)] *
                             self.n_filter for i in range(len(nlc))]).ravel()) * \
                  (1 + zhelio_lc) + self.snInfo['tmax'][sn_lc]

        band_lc = self.make_band(nlc)
        # self.make_band(nlc)
        # band_lc = self.bands_lc_obs
        flux_lc = np.zeros_like(date_lc)
        lc_none = np.array([b''] * len(date_lc))
        lc_ones = np.ones_like(sn_lc)
        lc_mean_wavelength = np.zeros_like(flux_lc)
        bands = [i.decode('UTF-8') for i in np.unique(band_lc)]
        filterset = salt2.load_filters(bands)
        for bd in bands:
            idxmw = band_lc == bd.encode('UTF-8')
            lc_mean_wavelength[idxmw] = filterset.mean_wavelength([bd])
        
        self.lc = np.rec.fromarrays((date_lc, flux_lc, flux_lc,  band_lc,
                                     lc_mean_wavelength, lc_none, zhelio_lc, sn_lc,
                                     -1 * lc_ones),  # obs_id_lc),
                                    dtype=self.data_type)

    def bands_survey(self):
        r"""
        Attribute band to the light curves, if LSST all SNe are observed through griz.
        If not depending on z, they are observed through CSP, SDSS and SNLS bands.
        """
        if self.lsst_simu:
            self.bands = ['LSST::u', 'LSST::g', 'LSST::r', 'LSST::i', 'LSST::z']
            if self.remove_band != 0:
                for bd in self.remove_band:
                    self.bands.remove(bd)
            self.n_filter = len(self.bands)
        else:
            self.bands = ['SWOPE::u', 'SWOPE::V', 'SWOPE::B', 'SWOPE::r',
                          'SDSS::g', 'SDSS::r', 'SDSS::i', 'SDSS::z',
                          'MEGACAMPSF::g', 'MEGACAMPSF::i', 'MEGACAMPSF::r', 'MEGACAMPSF::z']

    def make_band(self, nlc):
        r"""
        Create the band array of each photometric observation.
        If observations are made through LSST cadence, all sne are observe by math:`u,g,r,i,z` bands.
        If not, observing band depend on the z.
        If z < 0.05, bands are u, B, V and r from the SWOPE instrument.
        If 0.05 < z < 0.2, they are griz from SDSS's instrument.
        and if 0.2 < z, bands are griz of Megacam.

        Parameters
        ----------
        nlc : array
            Number of observation per Lcs.

        Returns
        -------
        band_lc : array
            Band corresponding to each observation
        """
        band_lc = []
        if self.lsst_simu:
            for iz in range(len(self.z)):
                band_lc0 = np.array(np.repeat(self.bands, nlc[iz]), dtype='|S16')
                band_lc.append(band_lc0)
            band_lc = np.hstack(band_lc)
        else:
            for iz in range(len(self.z)):
                zz = self.z[iz]
                if zz < 0.05:
                    i_band = 0
                elif (zz >= 0.05) & (zz < 0.2):
                    i_band = 1
                else:
                    i_band = 2
                band_lc0 = np.array(np.repeat(self.bands[i_band * self.n_filter:(i_band + 1) * self.n_filter],
                                              nlc[iz]), dtype='|S16')
                band_lc.append(band_lc0)
            band_lc = np.hstack(band_lc)
        return band_lc
