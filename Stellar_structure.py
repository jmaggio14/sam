import numpy as np
import sam

def mass_gradient(r,rho,autoDebug=True):
	"""
	dMr/dr = rho(r) * 4 * pi * r^2
	the mass gradient within the given radius/radii
	:inputs:
		r [numpy.ndarray,float,int]
			'--> radius, or set of radii to calculate
		rho [numpy.ndarray,float,int] 
			'--> density, either an array of density by radius or an average
	"""
	try:	

		#-------------BEGIN ERROR CHECKING----------------
		if autoDebug:
			sam.type_check(r,[np.ndarray,int,float],'r')
			sam.type_check(rho,[np.ndarray,int,float],'rho')
		#-------------END ERROR CHECKING------------------

		massGradient = 4.0 * sam.SAM_pi * r**2 * rho
		return massGradient

	except Exception as e:
		sam.debug(e)

def pressure_gradient(r,rho,Mr):
	"""
	dPr/dr = (-G * Mr * rho(r) ) / (r^2)
	the pressure gradient at the given radius/radii
	:inputs:
		r [numpy.ndarray,float,int]
			'--> radius, or set of radii to calculate
		rho [numpy.ndarray,float,int] 
			'--> density, either an array of density by radius or an average
		Mr [numpy.ndarray,float,int]
			'--> the mass at the mass at the radius
	"""
	try:
		#-------------BEGIN ERROR CHECKING----------------
		if autoDebug:
			sam.type_check(r,[np.ndarray,int,float],'r')
			sam.type_check(rho,[np.ndarray,int,float],'rho')
			sam.type_check(Mr,[np.ndarray,int,float],'Mr')
		#-------------END ERROR CHECKING------------------

		"""NEED TO CHECK SIGNS HERE!"""
		presureGradient = (-1.0 * sam.SAM_G * Mr * rho) / (r**2)
		return presureGradient

	except Exception as e:
		sam.debug(e)


def luminosity_gradient(r,rho,epsilon):
	"""
	dLr/dr = epsilon * rho(r) * 4 * pi * r^2
	the luminosity gradient at the given radius/radii
	:inputs:
		r [numpy.ndarray,float,int]
			'--> radius, or set of radii to calculate
		rho [numpy.ndarray,float,int] 
			'--> density, either an array of density by radius or an average
		epsilson [float,int]
			'--> the specific energy [J/kg] of the star
	"""	
	try:
		#-------------BEGIN ERROR CHECKING----------------
		if autoDebug:
			sam.type_check(r,[np.ndarray,int,float],'r')
			sam.type_check(rho,[np.ndarray,int,float],'rho')
			sam.type_check(epsilon,[int,float],'Mr')
		#-------------END ERROR CHECKING------------------

		luminosityGradient = epsilon * rho * 4.0 * sam.SAM_pi * r**2
		return luminosityGradient

	except Exception as e:
		sam.debug(e)