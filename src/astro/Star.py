import numpy as np
import scipy.integrate as integ
import sam

class Star(object):
	"""
	Creates a 'Star' object which builds all stellar structure 
	attributes based on the initial values in the config parameter

	"""


	def __init__(self,configs):
		#user loaded config files
		self._configs = configs

		self.load_config_attributes()
		self.calculate_attributes()
		self.calculate_boundaries()
		self.calculate_structure()


	def load_config_attributes(self):
		try: #wrapped in try-catch for debugging and traceback ease

			#mass
			self._Ms = self._configs["Ms"]
			#radius
			self._Rs = self._configs["radius"]["Rs"]
			self._dr = self._configs["radius"]["dr"]
			
			#mass fractions
			self._X = self._configs["mass_fractions"]["X"]
			self._Y = self._configs["mass_fractions"]["Y"]
			self._Z = self._configs["mass_fractions"]["Z"]

			#gamma
			self._gamma = self._configs["gamma"]
			
			#effective temperature
			self._Teff = self._configs["Teff"]

			#opacity object to calculate opacity value for given rho and T
			opacityFilename = self._configs["opacity"]["filename"]
			self._OPAC = sam.sig_proc.Opacity(opacityFilename) 

			#Stopping criteria
			self._stoppingCritera = self._configs["stopping_critera"]


		except Exception as e:
			sam.debug(e)


	def calculate_attributes(self):
		"""
		calculates attributes not given in config

		"""

		try: #wrapped in try-catch for debugging and traceback ease

			#calculated attributes -- ie values not given in the config file
			
			#gamma ratio, generally (gamma - 1) / gamma in class but inverse here
			self._gammaRatio = self._gamma / (self._gamma - 1)

			# mean molecular weight
			self._mu = sam.astro.mean_molecular_weight(self._X,self._Y,self._Z)
			
			#calculating Stellar Luminosity based off of Stefan Boltzman
			self._Ls = sam.astro.luminosity(self._Rs,self._Teff)

			#calculating specific stopping criteria
			self._minM = self._stoppingCritera["M_min"] * self._Ms
			self._minL = self._stoppingCritera["L_min"] * self._Ls 
			self._minR = self._stoppingCritera["R_min"] * self._Rs

			#compiling all attributes into dictionary for easy access later
			self._attributes = {"Ms":self._Ms,
								"Rs":self._Rs,
								"dr":self._dr,
								"X" :self._X,
								"Y" :self._Y,
								"Z" :self._Z,
								"gamma":self._gamma,
								"gammaRatio":self._gammaRatio,
								"OPAC":self._OPAC,
								"mu":self._mu,
								"Ls":self._Ls,
								"minM":self._minM,
								"minL":self._minL,
								"minR":self._minR	}

		except Exception as e:
			sam.debug(e)


	def calculate_boundaries(self):
		try: #wrapped in try-catch for debugging and traceback ease

			#calculating initial values as stated in appendix L of BOB
			self._bounds = sam.astro.boundaries(self._attributes)

		except Exception as e:
			sam.debug(e)


	def calculate_structure(self):
		"""
		calculates stellar structure using the 4 1D stellar structure equations

		"""

		try: #wrapped in try-catch for debugging and traceback ease

			# preparing arrays to load values into
			# should convert to setting values in numpy array and referencing later --> much faster
			self._radii = []
			self._MrArray = []
			self._LrArray = []
			self._PrArray = []
			self._TrArray = []

			self._rhoArray = []

			self._mGrad = []
			self._lGrad = []
			self._pGrad = []
			self._tGrad = []
			self._tGradSwitch = 1e4 #index where self._tGrad switches from adibatic to radiation

			#assigning initial values to self._bounds
			lastM = self._Ms
			lastL = self._Ls
			lastT = self._bounds["T"]
			lastP = self._bounds["P"]
			rho = self._bounds["rho"]
			kappa = self._bounds["kappa"]
			epsilon = self._bounds["epsilon"]
			self._radii.append(self._bounds["r"])
			r = self._bounds["r"] - self._dr

			print(self._bounds)

			#Continues loop until program determines it has reached the core
			atCore = False
			i = 0
			while atCore != True:
				# stepping radius

				i = i + 1
				# print(i)
				#calculating stellar structure
				#mass gradient
				if i < 2:
					print(rho)
				self._mGrad.append(  sam.astro.mass_gradient( r,rho )  )
				# print(self._mGrad[-1])
				Mr = lastM - (self._mGrad[-1] * self._dr)
				# print( sam.astro.mass_gradient( r,rho ) )
				self._MrArray.append(  Mr  )

				#pressure gradient
				self._pGrad.append(  sam.astro.pressure_gradient( r,rho,lastM )  )
				Pr = lastP + (self._pGrad[-1] * self._dr)
				self._PrArray.append(  Pr  )
				
				#luminsosity gradient
				self._lGrad.append(  self._mGrad[-1] * epsilon )
				Lr = lastL - (self._lGrad[-1] * self._dr)
				self._LrArray.append(  Lr  )
				
				#temperature gradient

				adiabatic = True
				#MUST FIGURE OUT WAY TO DETERMINE THIS
				if adiabatic:
					self._tGrad.append(  sam.astro.temperature_gradient_adiabatic(r,self._gamma,self._mu,Mr)  ) #should this be internal mass?
					Tr = lastT - (self._tGrad[-1] * self._dr)
					self._TrArray.append(  Tr  )
				else:
					self._tGrad.append(  sam.astro.temperature_gradient_radiation(r,rho,kappa,lastT,lastL)  )
					Tr = lastT - (self._tGrad[-1] * self._dr)
					self._TrArray.append
				#setting values for next round of computation
				# print(lastM - Mr)
				# print(lastM - Mr)
				rho = sam.astro.rho(lastT,lastP,self._mu)
				self._rhoArray.append(rho)

				lastM = self._MrArray[-1]
				lastL = self._LrArray[-1]
				lastT = self._TrArray[-1]
				lastP = self._PrArray[-1]
				# print(lastT)
				kappa = self._OPAC.value( rho,lastT )
				epsilon = sam.astro.specific_energy(self._X,rho,lastT)

				print("RHO=",rho)
				print("lastL ",lastL)
				print("lastM ",lastM)
				print("lastT ",lastT)
				print("lastP ",lastP)

				#checking if stopping criteria has been met
				if (self._minR > r) or (self._minL > lastL) or (self._minM > lastM):
					pass
					# print("atCore triggering")
					break

				self._radii.append(r)
				r = r - self._dr

			self._radii = np.asarray(self._radii)
			self._MrArray = np.asarray(self._MrArray)
			self._LrArray = np.asarray(self._LrArray)
			self._PrArray = np.asarray(self._PrArray)
			self._TrArray = np.asarray(self._TrArray)
			
			self._rhoArray = np.asarray(self._rhoArray)


			self._mGrad = np.asarray(self._mGrad)
			self._lGrad = np.asarray(self._lGrad)
			self._pGrad = np.asarray(self._pGrad)
			self._tGrad = np.asarray(self._tGrad)

		except Exception as e:
			sam.debug(e)
