import numpy as np
import sam
import sam.astro as sat

class Star(object):
	"""
	Creating the star
	 itself, based of configs and data files

	:inherits:
		Config: class that retreives and validates configuration file
	"""


	def __init__(self,configs):
		#Raw Configuration Values
		self._configs = configs
		self.assign_base_attributes()
		self.calculate_attributes()
		self.calculate_structure()



	def assign_base_values(self):
		#mass
		self._mass = self.configs["mass"]
		#radius
		self._totalRadius = self._configs["radius"]["total"]
		#effective bb temperature
		self._effectiveTemperature = self._configs["effective_temperature"]
		#mass fractions
		self._X = self._configs["massFractions"]["X"]
		self._Y = self._configs["massFractions"]["Y"]
		self._Z = self._configs["massFractions"]["Z"]

	def calculate_attributes(self):
		#luminosity
		self._luminosity = sat.luminosity(self._totalRadius,self._effectiveTemperature)
		#pressure
		if self._configs["calculate_pressure"] == True:
			vol = 4.0/3.0 * sam.CONSTANT_pi * self._totalRadius**3
			self._pressure = self._mass / vol
		else:	
			self._pressure = self._configs["average_pressure"]
		#internal mass
		specificEnergyPP = sat.specific_energy_pp(self._X,self._pressure)
		specificEnergyCNO = sat.specific_energy_cno(self.)
		self._specificEnergy = specificEnergyPP + specificEnergyCNO
		
		#######---------  ADD SPECIFIC ENERGY CNO  ----------
		self._radiusStep = self._configs["radius"]["step"]
		self._radii = np.arange( 0.0, self._totalRadius, integrationDistance )

	def calculate_structure(self):
		r = self._radii
		rho = self._pressure
		#mass gradient
		self._massGradient = sat.mass_gradient(r,rho)
		#pressure gradient
		self._internalMass = np.cumsum(self._massGradient * self._radiusStep)
		self._pressureGradient = sat.pressure_gradient(r,rho,self._internalMass)
		#luminosity gradient
		self._luminosityGradient = sat.luminosity_gradient(r,rho,self._specificEnergy)
		#temperature gradient
		internalLuminosity = 
		radTempGradient = 
		adiabaticTempGradient = 
		