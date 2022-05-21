# -*- coding: utf-8 -*-
"""
Provides classes for specifying a sersic light distribution.

This module contains the class required to provide a sersic light distribution
as the source for paltas.
"""
from .source_base import SourceBase
from lenstronomy.LightModel.light_model import LightModel
from lenstronomy.Util.data_util import magnitude2cps
import numpy as np


class RealImage(SourceBase):
	"""Class to generate single Sersic profile light models

	Args:
		cosmology_parameters (str,dict, or colossus.cosmology.Cosmology):
			Either a name of colossus cosmology, a dict with 'cosmology name':
			name of colossus cosmology, an instance of colussus cosmology, or a
			dict with H0 and Om0 ( other parameters will be set to defaults).
		source_parameters: dictionary with source-specific parameters.

	Notes:

	Required Parameters

	- magnitude - AB absolute magnitude of the source
	- output_ab_zeropoint - AB magnitude zeropoint of the detector
	- R_sersic - Sersic radius in units of arcseconds
	- n_sersic - Sersic index
	- e1 - x-direction ellipticity eccentricity
	- e2 - xy-direction ellipticity eccentricity
	- center_x - x-coordinate lens center in units of arcseconds
	- center_y - y-coordinate lens center in units of arcseconds
	- z_source - source redshift
	"""

	required_parameters = ('file', 'output_ab_zeropoint', 
		'center_x', 'center_y', 'z_source', 'scale', 'amp')

	def draw_source(self):
		"""Return lenstronomy LightModel kwargs

		Returns:
			(list,list) A list containing the model names(s), and
			a list containing the model kwargs dictionaries.
		"""
		# Just extract each of the sersic parameters.
		params ={
			k: v
			for k, v in self.source_parameters.items()
			if k in self.required_parameters}
		params.pop('z_source')
		params.pop('output_ab_zeropoint')

		# mag to amp conversion
		params['image']=np.load(self.source_parameters['file'])
		params.pop('file')
		return (
			['INTERPOL'],
			[params])
