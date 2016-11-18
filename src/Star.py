import numpy

class Star(sam.Config):

	def __init__(self,configs):

		#Stellar Mass
		self._mass = configs["mass"]

		#Stellar Radius
		self._radius = configs["radius"]

		#Stellar temperature
		self._temperature = configs["temperature"]

		#Stellar Luminosity
		self._luminosity = sam.luminosity()

		#Stellar Mass Fractions -- X:Hydrogen,Y:Helium,Z:Metals
		self._massFractions = configs["mass_fractions"]
		self._X = self._massFractions["X"]
		self._Y = self._massFractions["Y"]
		self._Z = self._massFractions["Z"]

		#Stellar Opacity as function of radius
		self._opacity = None
