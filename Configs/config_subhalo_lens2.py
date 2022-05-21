# Includes a PEMD deflector with external shear, and Sersic sources. Includes 
# a simple observational effect model that roughly matches HST effects for
# Wide Field Camera 3 (WFC3) IR channel with the F160W filter.

import numpy as np
import pandas as pd
from scipy.stats import norm, truncnorm, uniform, lognorm
from paltas.MainDeflector.simple_deflectors import PEMDShear
from paltas.Sources.sersic_amp import SingleSersicSource
from paltas.Substructure.los_dg19 import LOSDG19
from paltas.Substructure.subhalos_dg19_single import SubhalosDG19
from paltas.Sources.cosmos import COSMOSExcludeCatalog
from paltas.Sources.real_image import RealImage



# Define the numerics kwargs.
kwargs_numerics = {'supersampling_factor':1}

# This is always the number of pixels for the CCD. If drizzle is used, the
# final image will be larger.
numpix = 128
no_noise = False

# Define some general image kwargs for the dataset
# mask_radius = 0.5
# mag_cut = 2.0

# Define arguments that will be used multiple times
output_ab_zeropoint = 25.127


config_dict = {
	'subhalo':{
		'class': SubhalosDG19,
		'parameters':{
			'sigma_sub':norm(loc=2e-3,scale=0e-3).rvs,
			'shmf_plaw_index':uniform(loc=-1.92,scale=0.).rvs,
			'm_pivot': 1e10,'m_min': 1e9,'m_max': 2e9,
			'c_0':uniform(loc=16,scale=0).rvs,
			'conc_zeta':uniform(loc=-0.3,scale=0.).rvs,
			'conc_beta':uniform(loc=0.55,scale=0.).rvs,
			'conc_m_ref': 1e8,
			'dex_scatter': uniform(loc=0.1,scale=0.0).rvs,
			'k1':0.0, 'k2':0.0
		}
	},
	'main_deflector':{
		'class': PEMDShear,
		'parameters':{
			'M200': 1e13,
			'z_lens': 2.0,
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
	'lens_light':{
		'class': SingleSersicSource,
		'parameters':{
			'z_source':2.0,
			'amp':lambda: np.exp(norm(loc=np.log(30),scale=0.2).rvs()),
			'output_ab_zeropoint':output_ab_zeropoint,
			'R_sersic':truncnorm(-2,2,loc=0.35,scale=0.05).rvs,
			'n_sersic':truncnorm(-6.,np.inf,loc=3.,scale=0.5).rvs,
			'e1':norm(loc=0.0,scale=0.1).rvs,
			'e2':norm(loc=0.0,scale=0.1).rvs,
			'center_x':norm(loc=0.0,scale=0.).rvs,
			'center_y':norm(loc=0.0,scale=0.).rvs}
	},
	'source':{
		'class': SingleSersicSource,
		'parameters':{
			'z_source':6.0,
			'amp':lambda: np.exp(norm(loc=np.log(150),scale=0.9).rvs()),
			'output_ab_zeropoint':output_ab_zeropoint,
			'R_sersic':truncnorm(-2,2,loc=0.35,scale=0.05).rvs,
			'n_sersic':truncnorm(-6.,np.inf,loc=3.,scale=0.5).rvs,
			'e1':norm(loc=0.0,scale=0.1).rvs,
			'e2':norm(loc=0.0,scale=0.1).rvs,
			'center_x':norm(loc=0.0,scale=0.).rvs,
			'center_y':norm(loc=0.0,scale=0.).rvs}
	},


	'cosmology':{
		'parameters':{
			'cosmology_name': 'planck18'
		}
	},
	'psf':{
		'parameters':{
			'psf_type':'GAUSSIAN',
			'fwhm': 0.02
		}
	},
	'detector':{
		'parameters':{
			'pixel_scale':0.040,'ccd_gain':1.58,'read_noise':3.0,
			'magnitude_zero_point':output_ab_zeropoint,
			'exposure_time':3600,'sky_brightness':21.83,
			'num_exposures':4,'background_noise':None
		}
	}
}
