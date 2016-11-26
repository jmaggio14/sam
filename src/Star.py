import numpy as np
import os

class Star(object):
	"""
	Creating the star
	 itself, based of configs and data files

	:inherits:
		Config: class that retreives and validates configuration file
	"""


	def __init__(self,configs):
		#Retrieving values from files [arrays]
		self._radii = sam.retrieve_non_structured_data(self._configs.radii_filename)
		self._totalRadius = self._radii[-1]

		#Raw Configuration Values
		self._configs = configs
		## All single values
		self._mass = self.configs["mass"]
		self._effectiveTemperature = self.configs["effective_temperature"]
		###ADD L(r) and separate totalLuminosity variable
		self._luminosity = sam.luminosity(self._totalRadius,self._effectiveTemperature)

		self._X = self._configs["massFractions"]["X"]
		self._Y = self._configs["massFractions"]["Y"]
		self._Z = self._configs["massFractions"]["Z"]
		self._averagePressure = self._configs["average_pressure"]


		# preparing to calculate stellar structure
		self._internalMass = sam.internal_mass(self._radii,self._averagePressure)
		self._specificEnergyPP = sam.specific_energy_pp(self._X,self._averagePressure)


		#Calculating Stellar Structure
		self._massGradient = sam.mass_gradient(self._radii,self._averagePressure)





