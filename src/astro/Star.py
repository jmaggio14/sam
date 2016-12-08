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
		self.load_config_attributes()
		self.calculate_attributes()
		self.calculate_structure()


	def load_config_attributes(self):
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
			opacityFilename = self._configs["opacity"]["filename"]
			self._OPAC = sam.sig_proc.Opacity(opacityFilename) 
			
		except Exception as e:
			sam.debug(e)


	def calculate_attributes(self):
		#pressure
		try:
			#calculating stellar radii ( stellar structure function bounds )
			self._radii = np.flipud( np.arange( 0.0,self._totalRadius, self._radiusStep,dtype=sam.TYPE_64F) )
			#calculating mean molecular weight
			self._mu = sam.astro.mean_molecular_weight(self._X,self._Y,self._Z)

			#calculating inital approximations for purposes of numerical integration
			Rs = self._radii[0]
			Ri = self._radii[1]
			
			#HARDCODED TO TEST -- FOR GOD SAKES CHANGE THIS
			A = .4 
			#all equations determined from appendix L in BOB
			self._initialTemperature = sam.astro.boundary_temperature(Ri,Rs,self._mu,self._mass)
			self._initialLuminosity = sam.astro.luminosity(Rs,self._initialTemperature)
			self._initialPressure = sam.astro.boundary_pressure(self._mass,self._initialLuminosity,self._mu,self._initialTemperature,self._initialEpsilon)
			self._initialDensity = sam.astro.rho(self._initialTemperature,self._initialPressure,self._mu)
			self._initialEpsilon = sam.astro.specific_energy(self._X,self._initialPressure,self._initialTemperature)

		except Exception as e:
			sam.debug(e)

	def calculate_structure(self):
		try:	
			radii = self._radii.copy() #just good practice to perform deep copy

			#preparing stellar structure arrays to plop data into
			self._massGradient = np.zeros( radii.size + 1 )
			self._pressureGradient = np.zeros( radii.size + 1 )
			self._luminosityGradient = np.zeros( radii.size + 1 )

			self._adiabaticTemperatureGradient = np.zeros( radii.size + 1 )
			self._radiationTemperatureGradient = np.zeros( radii.size + 1 )
			self._temperatureGradient = np.zeros( radii.size + 1 )
			
			# non Stellar Structure data
			self._rho = np.zeros( radii.size + 1 )
			self._internalTemperature = np.zeros( radii.size + 1 )
			self._internalMass = np.zeros( radii.size + 1 )
			self._internalLuminosity = np.zeros( radii.size + 1 )
			self._internalEpsilon = np.zeros( radii.size + 1 )
			self._internalOpacity = np.zeros( radii.size + 1 )
			self._internalPressure = np.zeros( radii.size + 1 )


			#setting intial values
			self._rho[0] = self._initialDensity
			self._internalMass[0] = self._mass
			self._internalEpsilon[0] = self._initialEpsilon
			self._internalLuminosity[0] = self._initialLuminosity
			self._internalTemperature[0] = self._initialTemperature
			self._internalPressure[0] = self._initialPressure
			self._internalOpacity[0] = self._OPAC.value(self._rho[0],self._internalTemperature[0])
			T1 = self._initialTemperature
			for index,r in enumerate(radii):
				nextIndex = index+1
				
				# equations of stellar structure
				self._massGradient[index] = sam.astro.mass_gradient(r,self._rho[index])
				self._pressureGradient[index] = sam.astro.pressure_gradient(r,self._rho[index],self._internalMass[index])
				self._luminosityGradient[index] = sam.astro.luminosity_gradient(r,self._rho[index],self._internalEpsilon[index])
				self._adiabaticTemperatureGradient[index] = sam.astro.temperature_gradient_adiabatic(r,self._internalMass[index],self._mu)
				self._radiationTemperatureGradient[index] = sam.astro.temperature_gradient_radiation(r,self._rho[index],
															self._internalOpacity[index],self._mu,self._internalTemperature[index],self._internalLuminosity[index])
				self._temperatureGradient[index] = self._radiationTemperatureGradient[index] + self._adiabaticTemperatureGradient[index]

				#dependencies and other values
				self._rho[nextIndex] = sam.astro.rho(self._internalTemperature[index],self._internalPressure[index],self._mu)
				self._internalMass[nextIndex] = sam.astro.internal_mass(r,self._rho[index])
				self._internalEpsilon[nextIndex] = sam.astro.specific_energy(self._X,self._rho[index],self._internalTemperature[index])
				print("TEMPERATURE IS",self._internalTemperature[index])
				self._internalLuminosity[nextIndex] = sam.astro.luminosity(r,self._internalTemperature[index])
				self._internalTemperature[nextIndex] = sam.astro.temperature_from_gradient(self._temperatureGradient[index],T1,self._radiusStep)
				T1 = self._temperatureGradient[index]
				self._internalPressure[nextIndex] = sam.astro.pressure(self._rho[index],self._internalTemperature[index],self._mu)
				self._internalOpacity[0] = self._OPAC.value(self._rho[0],self._internalTemperature[0])

		except Exception as e:
			sam.debug(e)
