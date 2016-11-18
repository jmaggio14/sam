import sam
import numpy as np

def luminosity(r,T,autoDebug=True):
	"""
	calculates the luminosity based off of the
	Stefan-Boltzmann law

	:inputs:
		r [np.ndarray,int,float] -- radius or radii of stars
		T [np.ndarray,int,float] -- effective temperature or effective temperatures
	:returns:
		L [np.ndarray,float] -- effective luminosity or luminosities 
	"""
	#-----------BEGIN ERROR CHECKING----------
	if autoDebug:
		sam.type_check(r, sam.SAM_TYPES_math, "r")
		sam.type_check(T, SAM_TYPES_math, "T")
		sam.value_check(r,.0,">","r")
		sam.value_check(T,.0.,">","T")
	#-----------END ERROR CHECKING----------

	L = 4 * sam.SAM_pi * r**2 * sam.SAM_k * T**4
	return L

