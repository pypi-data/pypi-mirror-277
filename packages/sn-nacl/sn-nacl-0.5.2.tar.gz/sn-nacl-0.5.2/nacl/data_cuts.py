import numpy as np 
import pandas as pd
from nacl.models.salt import SALT2Like
import matplotlib.pyplot as plt
from nacl.dataset import TrainingDataset

def cut(data_generator, model_func,init_from_salt2_file="../data/salt2.npz", degree=3, normalization_band_name='SWOPE::B',phase_range=(-20., 50.), wl_range=(2000., 9000.),plot=False):
	r"""
	Function to find the light curve and spectra index outside our model

	Attributes
	----------
	data_generator : nacl.jla.generator or nacl.ideal.generator or nacl.k21.generator
	Cadence and SNe information.
	model_func : nacl.models.salt.SALT2Like
	Model to generated data.
	degree : int
	Degree of the spectral recalibration polynomial function.
	normalization_band_name : str
	Band name for normalization of the model.
	init_from_salt2_file : str
	File salt2, created by script 'nacl.simulation.make_salt2_npz.py'.
	plot : False or True; plot spec/lc with data cut 
	"""

	model = model_func(data_generator.trainingDataset,init_from_salt2_file=init_from_salt2_file, spectrum_recal_degree=degree,normalization_band_name=normalization_band_name,phase_range=phase_range, wl_range=wl_range)


	blue_cutoff, red_cutoff = model.wl_range
	early_cutoff, late_cutoff = model.phase_range

	# for JLA and K21 need cutoff to be less than model def;
	# in order to degrade tmax and fit
	early_cutoff += 5
	late_cutoff -= 5

	lc = data_generator.trainingDataset.lc_data
	sp = data_generator.trainingDataset.spec_data
	snInfo = data_generator.trainingDataset.sn_data

	# lc
	bands = np.unique(lc.nt['band'])
	lambda_range = np.linspace(1500, 11000, int(1e5))
	min_lambda = np.zeros(len(lc.nt['band']))
	max_lambda = np.zeros(len(lc.nt['band']))
	for bd in bands:
		idx = lc.nt['band'] == bd
		ff = model.filter_db.transmission_db[bd].func(lambda_range)
		idxx = np.where(ff > ff.max()*0.01)
		mmin, mmax = lambda_range[idxx[0][0]], lambda_range[idxx[0][-1]]
		min_lambda[idx] = mmin/(1+snInfo.nt.z[np.array([np.where(snInfo.nt.sn==yy)[0][0] for yy in lc.nt[idx].sn])])
		max_lambda[idx] = mmax/(1+snInfo.nt.z[np.array([np.where(snInfo.nt.sn==yy)[0][0] for yy in lc.nt[idx].sn])])
	date_lc = (lc.nt['mjd'] - snInfo.nt.tmax[np.array([np.where(snInfo.nt.sn==yy)[0][0] for yy in lc.nt.sn])]) / (1. + snInfo.nt.z[np.array([np.where(snInfo.nt.sn==yy)[0][0] for yy in lc.nt.sn])])	

	idx_ph_lc = (date_lc > early_cutoff) & (date_lc < late_cutoff)
	idx_wl_lc = (min_lambda > blue_cutoff) & (max_lambda < red_cutoff)
	idx_lc = idx_ph_lc & idx_wl_lc
	
	if plot==True:
		fig, ax1 = plt.subplots(figsize=(8,6), facecolor='w', edgecolor='k')
		
		#ax1.vlines(x=date_lc,ymin=min_lambda,ymax=max_lambda, color='red', zorder=2,ls='--')
		ax1.plot(date_lc,min_lambda,'ro')
		ax1.plot(date_lc,max_lambda,'ro')						
		
		ax1.axvline(x=early_cutoff,color='k',ls='--')	
		ax1.axvline(x=late_cutoff,color='k',ls='--')	
		ax1.axhline(y=blue_cutoff,color='k',ls='--')	
		ax1.axhline(y=red_cutoff,color='k',ls='--')			
		ax1.set_ylabel('Wavelength min max filter [Angs]',fontsize=14,fontweight='bold')						
		ax1.set_xlabel('Phase since max [days]',fontsize=14,fontweight='bold')								
		plt.show()
	# sp
	zspec=pd.merge(pd.DataFrame(sp.nt),pd.DataFrame(snInfo.nt).set_index('index'),how='inner', on=['sn'])['z']
	tspec=pd.merge(pd.DataFrame(sp.nt),pd.DataFrame(snInfo.nt).set_index('index'),how='inner', on=['sn'])['tmax']
	wl_sp = sp.nt['wavelength'] / (1. + zspec)
	idx_wl_sp = (wl_sp > blue_cutoff) & (wl_sp < red_cutoff)
	date_sp = (sp.nt['mjd'] - tspec) / (1. + zspec)
	idx_ph_sp = (date_sp > early_cutoff) & (date_sp < late_cutoff)

	idx_sp = idx_ph_sp & idx_wl_sp
	idx_sp=idx_sp.values

	if plot==True:
		fig, ax1 = plt.subplots(figsize=(8,6), facecolor='w', edgecolor='k')
		
		ax1.plot(date_sp,wl_sp,'ro')		
		ax1.axvline(x=early_cutoff,color='k',ls='--')	
		ax1.axvline(x=late_cutoff,color='k',ls='--')	
		ax1.axhline(y=blue_cutoff,color='k',ls='--')	
		ax1.axhline(y=red_cutoff,color='k',ls='--')			
		ax1.set_ylabel('Wavelength min max filter [Angs]',fontsize=14,fontweight='bold')						
		ax1.set_xlabel('Phase since max [days]',fontsize=14,fontweight='bold')								
		plt.show()	
	
	data_generator.trainingDataset.lc_data.valid=idx_lc.astype(int)
	data_generator.trainingDataset.spec_data.valid=idx_sp.astype(int)
		
	data_generator.trainingDataset.compress()	
	
	return data_generator
	
	
	
	
