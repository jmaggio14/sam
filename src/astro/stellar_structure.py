import sam
import numpy as np


def mass_gradient(r,rho,autoDebug=True):
	if autoDebug:
		sam.type_check(r,sam.TYPES_numbers,'r')
		sam.type_check(rho,sam.TYPES_numbers,'rho')

	dMdr = sam.CONSTANT_4pi * r**2 * rho
	return dMdr

def pressure_gradient(r,rho,Mr,autoDebug=True):
	if autoDebug:
		sam.type_check(r,sam.TYPES_numbers,'r')
		sam.type_check(rho,sam.TYPES_numbers,'rho')
		sam.type_check(Mr,sam.TYPES_numbers,'Mr')

	dPdr = (-sam.CONSTANT_G * Mr * rho) / (r**2)
	return dPdr

def luminosity_gradient(r,rho,epsilon,autoDebug=True):
	if autoDebug:
		sam.type_check(r,sam.TYPES_numbers,'r')
		sam.type_check(rho,sam.TYPES_numbers,'rho')
		sam.type_check(epsilon,sam.TYPES_numbers,'epsilon')

	dLdr = sam.CONSTANT_4pi * r**2 * rho * epsilon
	return dLdr

def temperature_gradient_radiation(r,rho,kappa,T,Lr,autoDebug=True):
	# if autoDebug:
	# 	sam.type_check(r,sam.TYPES_numbers,'gamma')
	# 	sam.type_check(kappa,sam.TYPES_numbers,'kappas')
	# 	sam.type_check(Mr,sam.TYPES_numbers,'Mr')
	
	numerator = -3 * kappa * rho * Lr
	denominator = 4 * sam.CONSTANT_a * sam.CONSTANT_c * T**3 * sam.CONSTANT_4pi * r**2
	
	radiationGrad = (numerator / denominator)
	return radiationGrad


def temperature_gradient_adiabatic(r,Mr,mu,autoDebug=True):
	if autoDebug:
		sam.type_check(r,sam.TYPES_numbers,'gamma')
		sam.type_check(mu,sam.TYPES_numbers,'mu')
		sam.type_check(Mr,sam.TYPES_numbers,'Mr')

	g = (sam.CONSTANT_G * Mr) / r**2
	nR = ( sam.CONSTANT_k / (mu * sam.CONSTANT_mh) )
	Cv = 1.5 * nR
	Cp = Cv + nR
	adiabaticGrad = -g / Cp

	return adiabaticGrad


# def mass_gradient(radii,autoDebug=True):
# 	"""
# 	dMr/dr = rho(r) * 4 * pi * r^2
# 	the mass gradient within the given radius/radii
# 	:inputs:
# 		r [numpy.ndarray,float,int]
# 			'--> radius, or set of radii to calculate
# 		rho [numpy.ndarray,float,int] 
# 			'--> density, either an array of density by radius or an average
# 	"""
# 	try:	

# 		#-------------BEGIN ERROR CHECKING----------------
# 		if autoDebug:
# 			sam.type_check(r,sam.TYPES_math,'r')
# 		#-------------END ERROR CHECKING------------------

# 		#flipping the radii array if necessary
# 		if radii[-1] > radii[-2]:
# 			radii = np.flipud(radii)
		
# 		#setting up output arrays
# 		# shellVol = volFunc( r, np.roll(r,-1) )  
	
# 		for index,r in enumerate(radii):


# 		return grad

# 	except Exception as e:
# 		sam.debug(e)


# 		# grad = np.zeros(r.shape)
# 		# shellVol = np.zeros(r.shape)
# 		# shellMass = np.zeros(r.shape)

# 		# #creating lambdas for equations --> less efficient but cleaner
# 		# gradFunc = lambda radius, rho : 4.0 * sam.CONSTANT_pi * radius**2.0 * rho
# 		# volFunc = lambda r2,r1 : 1.3333333 * sam.CONSTANT_pi * (r2**3 - r1**3) 
# 		# shellMassFunc = lambda grad, r2, r1 : grad * (r2 - r1)

# def pressure_gradient(r,rho,Mr,autoDebug=True):
# 	"""
# 	dPr/dr = (-G * Mr * rho(r) ) / (r^2)
# 	the pressure gradient at the given radius/radii
# 	:inputs:
# 		r [numpy.ndarray,float,int]
# 			'--> radius, or set of radii to calculate
# 		rho [numpy.ndarray,float,int] 
# 			'--> density, either an array of density by radius or an average
# 		Mr [numpy.ndarray,float,int]
# 			'--> the mass at the mass at the radius
# 	"""
# 	try:
# 		#-------------BEGIN ERROR CHECKING----------------
# 		if autoDebug:
# 			sam.type_check(r,sam.TYPES_math,'r')
# 			sam.type_check(rho,sam.TYPES_math,'rho')
# 			sam.type_check(Mr,sam.TYPES_math,'Mr')
# 		#-------------END ERROR CHECKING------------------

# 		"""NEED TO CHECK SIGNS HERE!"""
# 		presureGradient = (-1.0 * sam.CONSTANT_G * Mr * rho) / (r[:-1]**2)
# 		return presureGradient

# 	except Exception as e:
# 		sam.debug(e)


# def luminosity_gradient(r,rho,epsilon,autoDebug=True):
# 	"""
# 	dLr/dr = epsilon * rho(r) * 4 * pi * r^2
# 	the luminosity gradient at the given radius/radii
# 	:inputs:
# 		r [numpy.ndarray,float,int]
# 			'--> radius, or set of radii to calculate
# 		rho [numpy.ndarray,float,int] 
# 			'--> density, either an array of density by radius or an average
# 		epsilson [float,int]
# 			'--> the specific energy [J/kg] of the star
# 	"""	
# 	try:
# 		#-------------BEGIN ERROR CHECKING----------------
# 		if autoDebug:
# 			sam.type_check(r,sam.TYPES_math,'r')
# 			sam.type_check(rho,sam.TYPES_math,'rho')
# 			sam.type_check(epsilon,sam.TYPES_numbers,'epsilon')
# 		#-------------END ERROR CHECKING------------------

# 		luminosityGradient = epsilon * rho * 4.0 * sam.CONSTANT_pi * r**2
# 		return luminosityGradient

# 	except Exception as e:
# 		sam.debug(e)


# def radiation_temperature_gradient(r,kappa,rho,Lr,T=0,autoDebug=True):
# 	try:
# 		#-------------BEGIN ERROR CHECKING----------------
# 		# if autoDebug:
# 		# 	sam.type_check(r,sam.TYPES_math,'r')
# 		# 	sam.type_check(conductivity,sam.TYPES_math,'conductivity')
# 		# 	sam.type_check(Lr,sam.TYPES_math,'Lr')
# 		#-------------END ERROR CHECKING------------------
		
# 		a = sam.CONSTANT_a
# 		c = sam.CONSTANT_c
# 		temperatureGradient = np.zeros( r.shape )

# 		for index,radius in enumerate(r):
# 			temperatureGradient = (-3.0 * kappa * rho * Lr[index])  / (4 * a * c * T**3)

# 	except Exception as e:
# 		sam.debug(e)

# def adiabatic_temperature_gradient(r,Mr,mu,autoDebug=True):
# 	try:
# 		#-------------BEGIN ERROR CHECKING----------------
# 		if autoDebug:
# 			sam.type_check(r,sam.TYPES_math,'r')
# 			sam.type_check(Mr,sam.TYPES_math,'Mr')
# 			sam.type_check(mu,sam.TYPES_numbers,'mu')
# 			sam.value_check(mu,0.,">","mu")
# 		#-------------END ERROR CHECKING------------------

# 		g = (sam.CONSTANT_G * Mr) / r[:-1]**2
# 		nR = ( sam.CONSTANT_k / (mu * sam.CONSTANT_mh) )
# 		Cv = 1.5 * nR
# 		Cp = Cv + nR

# 		tempGrad = -g / Cp
# 		return tempGrad
	
# 	except Exception as e:
# 		sam.debug(e)



# if __name__ == "__main__":
# 	dr = 1.0e+5
# 	rBound = 7e+8
# 	r = np.arange(0,rBound,dr)
# 	rho = 1410.0
# 	massGrad = mass_gradient(r,rho,autoDebug=False)

# 	internalMassTest = sam.sig_proc.integrate(massGrad,dx=1.0e5)
# 	internalMass = internal_mass(r[:-2],rho)

# 	# both = np.concatenate( (internalMassTest, internalMass ), axis=1 )
# 	# sub = internalMassTest - internalMass

# 	# np.savetxt("sub.txt",sub)
# 	np.savetxt("sig.txt",internalMassTest)
# 	np.savetxt("ast.txt",internalMass)
