import sam
import numpy as np

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

def pressure_gradient(r,rho,Mr,autoDebug=True):
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


def luminosity_gradient(r,rho,epsilon,autoDebug=True):
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
			sam.type_check(epsilon,[int,float],'epsilon')
		#-------------END ERROR CHECKING------------------

		luminosityGradient = epsilon * rho * 4.0 * sam.SAM_pi * r**2
		return luminosityGradient

	except Exception as e:
		sam.debug(e)


def radiation_temperature_gradient(r,kappa,rho,Lr,T,autoDebug=True):
    pass
#	try:
		#-------------BEGIN ERROR CHECKING----------------
		# if autoDebug:
		# 	sam.type_check(r,[np.ndarray,int,float],'r')
		# 	sam.type_check(conductivity,[np.ndarray,int,float],'conductivity')
		# 	sam.type_check(Lr,[np.ndarray,int,float],'Lr')
		#-------------END ERROR CHECKING------------------
		
		#temperatureGradient = (-3.0/4.0) ##UNFINISHED




###NON TRADITIONAL STELLAR STRUCTURE EQUATIONS
def internal_mass(r,rho,autoDebug=True):
	"""
	calculates internal mass of star

	Volume of circle * density 

	currently only works with 
	"""
	mass = 4.0/3.0 * sam.SAM_pi * r**3 * rho
	return mass


def specific_energy_pp(X,rho,T,fpp=1.0,psi=1.0,cpp=1.0):
	"""
	calculates specific energy for the proton-proton chain

	:inputs:
		X [float]
			'--> the mass fraction of hydrogen
		rho [float,int]
			'--> pressure of star (generally average pressure)
		T [float,int]
			'--> temperature of reasction (generally an average)
			'--> NOT T_6 (not T/1e6 as is usually used hand written equations)
		fpp [float,int]
			'--> PP chain screening factor (generally 1)
		psi [float,int]
			'--> PP correction factor (generally 1)
		cpp [float,int]
			'--> higher order correction term (generally 1)
	"""
	#separates these for sake of computational efficiency
	## ie don't bother multiplying by 1 when you don't have to
	if (fpp == 1.0) and (psi == 1.0) and (cpp == 1.0):
		epsilon = sam.SAM_ppConstant * rho * X**2 * (T/1e6)**4

	else:	
		epsilon = sam.SAM_ppConstant * rho * X**2 * fpp * psi * cpp * (T/1e6)**4

	return epsilon


def specific_energy_cno():


