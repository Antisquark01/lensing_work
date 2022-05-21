# Includes a PEMD deflector with external shear, and Sersic sources. Includes 
# a simple observational effect model that roughly matches HST effects for
# Wide Field Camera 3 (WFC3) IR channel with the F160W filter.

import numpy as np
import pandas as pd
from scipy.stats import norm, truncnorm, uniform
from paltas.MainDeflector.simple_deflectors import PEMDShear
from paltas.Sources.sersic import SingleSersicSource
from paltas.Substructure.los_dg19 import LOSDG19
from paltas.Substructure.subhalos_dg19_single import SubhalosDG19
from paltas.Sources.cosmos import COSMOSExcludeCatalog


# Define the numerics kwargs.
kwargs_numerics = {'supersampling_factor':1}

# This is always the number of pixels for the CCD. If drizzle is used, the
# final image will be larger.
numpix = 128

# Define some general image kwargs for the dataset
mask_radius = 0.0
mag_cut = None

# Define arguments that will be used multiple times
output_ab_zeropoint = 25.127
cosmos_folder ='../datasets/cosmos/COSMOS_23.5_training_sample/'


config_dict = {
	'subhalo':{
		'class': SubhalosDG19,
		'parameters':{
			'sigma_sub':norm(loc=2e-3,scale=1.1e-3).rvs,
			'shmf_plaw_index':uniform(loc=-1.92,scale=0.1).rvs,
			'm_pivot': 1e10,'m_min': 1e9,'m_max': 2e9,
			'c_0':uniform(loc=16,scale=2).rvs,
			'conc_zeta':uniform(loc=-0.3,scale=0.1).rvs,
			'conc_beta':uniform(loc=0.55,scale=0.3).rvs,
			'conc_m_ref': 1e8,
			'dex_scatter': uniform(loc=0.1,scale=0.06).rvs,
			'k1':0.0, 'k2':0.0
		}
	},
	'main_deflector':{
		'class': PEMDShear,
		'parameters':{
			'M200': 1e13,
			'z_lens': 0.5,
			'gamma': truncnorm(-20,np.inf,loc=2.0,scale=0.1).rvs,
			'theta_E': truncnorm(-1.1/0.15,np.inf,loc=1.1,scale=0.).rvs,
			'e1': norm(loc=0.0,scale=0.1).rvs,
			'e2': norm(loc=0.0,scale=0.1).rvs,
			'center_x': norm(loc=0.0,scale=0.16).rvs,
			'center_y': norm(loc=0.0,scale=0.16).rvs,
			'gamma1': norm(loc=0.0,scale=0.05).rvs,
			'gamma2': norm(loc=0.0,scale=0.05).rvs,
			'ra_0':0.0, 'dec_0':0.0
		}
	},
	# 'source':{
	# 	'class': SingleSersicSource,
	# 	'parameters':{
	# 		'z_source':(lambda: truncnorm(-5,np.inf,loc=3.,scale=0.0).rvs()),
	# 		'magnitude':uniform(loc=20,scale=0).rvs,
	# 		'output_ab_zeropoint':output_ab_zeropoint,
	# 		'R_sersic':truncnorm(-2,2,loc=0.35,scale=0.0).rvs,
	# 		'n_sersic':truncnorm(-6.,np.inf,loc=3.,scale=0.).rvs,
	# 		'e1':norm(loc=0.0,scale=0.).rvs,
	# 		'e2':norm(loc=0.0,scale=0.).rvs,
	# 		'center_x':norm(loc=0.0,scale=0.0).rvs,
	# 		'center_y':norm(loc=0.0,scale=0.0).rvs}
	# },
	'source':{
		'class': COSMOSExcludeCatalog,
		'parameters':{
			'z_source':3,'cosmos_folder':cosmos_folder,
			'max_z':1.0,'minimum_size_in_pixels':64,'faintest_apparent_mag':20,
			'smoothing_sigma':0.00,'random_rotation':False,
			'output_ab_zeropoint':output_ab_zeropoint,
			'center_x':norm(loc=0.0,scale=0.0).rvs,
			'center_y':norm(loc=0.0,scale=0.0).rvs,
			'min_flux_radius':10.0,'source_exclusion_list':np.append(
				pd.read_csv(
					'Sources/bad_galaxies.csv',
					names=['catalog_i'])['catalog_i'].to_numpy(),
				pd.read_csv(
					'Sources/val_galaxies.csv',
					names=['catalog_i'])['catalog_i'].to_numpy())}
	},
	'cosmology':{
		'parameters':{
			'cosmology_name': 'planck18'
		}
	},
	'psf':{
		'parameters':{
			'psf_type':'GAUSSIAN',
			'fwhm': 0.03
		}
	},
	'detector':{
		'parameters':{
			'pixel_scale':0.040,'ccd_gain':1.58,'read_noise':3.0,
			'magnitude_zero_point':output_ab_zeropoint,
			'exposure_time':1380,'sky_brightness':21.83,
			'num_exposures':4,'background_noise':None
		}
	}
}
