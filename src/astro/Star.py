import numpy as np
import scipy.integrate as integ
import sam

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


	def assign_base_attributes(self):
		try:
			#mass
			self._mass = self._configs["mass"]
			
			#radius
			self._totalRadius = self._configs["radius"]["total"]
			self._radiusStep = self._configs["radius"]["dr"]
			
			#mass fractions
			self._X = self._configs["mass_fractions"]["X"]
			self._Y = self._configs["mass_fractions"]["Y"]
			self._Z = self._configs["mass_fractions"]["Z"]
			
			#opacity
			# self._opacity = self._radii.copy() #TEMPORARY UNTIL YOU GET REAL OPACITY DATA
			# opacityFilename = self._configs["opacity"]["filename"]
			# self._opacity = sam.retreive_data(opacityFilename,structured=False)
		except Exception as e:
			sam.debug(e)


	def calculate_attributes(self):
		#pressure
		try:
			if self._configs["calculate_pressure"] == True:
				vol = 4.0/3.0 * sam.CONSTANT_pi * self._totalRadius**3
				self._pressure = self._mass / vol
			else:	
				self._pressure = self._configs["average_pressure"]

			#Calculating Specific Energy
			epsilonPP = sam.astro.specific_energy_pp(self._X,self._pressure,5777)
			epsilonCNO = sam.astro.specific_energy_cno(self._X,1,1,1)
			self._specificEnergy = epsilonPP + epsilonCNO
			
			#calculating stellar radii ( stellar structure function bounds )
			self._radii = np.arange( 0.0, self._totalRadius, self._radiusStep,dtype=sam.TYPE_32F )
		except Exception as e:
			sam.debug(e)
	def calculate_structure(self):
		try:
			r = self._radii.copy()
			rho = self._pressure
			
			#mass gradient
			self._massGradient = sam.astro.mass_gradient(r,rho)
			
			#pressure gradient
			Mr = integ.cumtrapz(self._massGradient,r)
			self._pressureGradient = sam.astro.pressure_gradient(r,rho,Mr)
			
			#luminosity gradient
			self._luminosityGradient = sam.astro.luminosity_gradient(r,rho,self._specificEnergy)
			
			#temperature gradient
			# internalLuminosity = integ.cu
			# radTempGradient = 
			mu = (self._X * 1) + (self._Y * 4) 
			self._adiabaticTempGradient = sam.astro.adiabatic_temperature_gradient(r,Mr,mu)
		except Exception as e:
			sam.debug(e)


