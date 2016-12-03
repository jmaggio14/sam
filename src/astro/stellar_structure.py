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
			sam.type_check(r,sam.TYPES_math,'r')
			sam.type_check(rho,sam.TYPES_math,'rho')
		#-------------END ERROR CHECKING------------------
		#flipping the radii array if necessary
		if r[-1] - r[-2] < 0:
			r = np.flipud(r)
		#setting defaults
		rho = 0
		integrationDistance = abs( r[-1] - r[-2] )

		#setting up output arrays
		grad = np.zeros(r.shape)
		shellVol = np.zeros(r.shape)
		shellMass = np.zeros(r.shape)

		#creating lambdas for equations --> less efficient but cleaner
		gradFunc = lambda radius, rho : 4.0 * sam.CONSTANT_pi * radius**2.0 * rho
		volFunc = lambda r2,r1 : 1.3333333 * sam.CONSTANT_pi * (r2**3 - r1**3) 
		shellMassFunc = lambda grad, delta : grad * delta

		prevRadius = r[0]
		for index,radius in enumerate(r):
			grad[index] = gradFunc(radius,rho)
			shellVol = volFunc(radius,r[index-1])
			shellMass[index] = shellMassFunc(grad,integrationDistance)

			prevRadius = radius

		mass = np.flipud( np.cumsum(shellMass) )
		volume = np.flipud( np.cumsum(shellVol) )

		return grad,mass,volume

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
			sam.type_check(r,sam.TYPES_math,'r')
			sam.type_check(rho,sam.TYPES_math,'rho')
			sam.type_check(Mr,sam.TYPES_math,'Mr')
		#-------------END ERROR CHECKING------------------

		"""NEED TO CHECK SIGNS HERE!"""
		presureGradient = (-1.0 * sam.CONSTANT_G * Mr * rho) / (r[:-1]**2)
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
			sam.type_check(r,sam.TYPES_math,'r')
			sam.type_check(rho,sam.TYPES_math,'rho')
			sam.type_check(epsilon,sam.TYPES_numbers,'epsilon')
		#-------------END ERROR CHECKING------------------

		luminosityGradient = epsilon * rho * 4.0 * sam.CONSTANT_pi * r**2
		return luminosityGradient

	except Exception as e:
		sam.debug(e)


def radiation_temperature_gradient(r,kappa,rho,Lr,T=0,autoDebug=True):
	try:
		#-------------BEGIN ERROR CHECKING----------------
		# if autoDebug:
		# 	sam.type_check(r,sam.TYPES_math,'r')
		# 	sam.type_check(conductivity,sam.TYPES_math,'conductivity')
		# 	sam.type_check(Lr,sam.TYPES_math,'Lr')
		#-------------END ERROR CHECKING------------------
		
		a = sam.CONSTANT_a
		c = sam.CONSTANT_c
		temperatureGradient = np.zeros( r.shape )

		for index,radius in enumerate(r):
			temperatureGradient = (-3.0 * kappa * rho * Lr[index])  / (4 * a * c * T**3)

	except Exception as e:
		sam.debug(e)

def adiabatic_temperature_gradient(r,Mr,mu,autoDebug=True):
	try:
		#-------------BEGIN ERROR CHECKING----------------
		if autoDebug:
			sam.type_check(r,sam.TYPES_math,'r')
			sam.type_check(Mr,sam.TYPES_math,'Mr')
			sam.type_check(mu,sam.TYPES_numbers,'mu')
			sam.value_check(mu,0.,">","mu")
		#-------------END ERROR CHECKING------------------

		g = (sam.CONSTANT_G * Mr) / r[:-1]**2
		nR = ( sam.CONSTANT_k / (mu * sam.CONSTANT_mh) )
		Cv = 1.5 * nR
		Cp = Cv + nR

		tempGrad = -g / Cp
		return tempGrad
	
	except Exception as e:
		sam.debug(e)

###NON TRADITIONAL STELLAR STRUCTURE EQUATIONS
def internal_mass(r,rho,autoDebug=True):
	"""
	calculates internal mass of star

	Volume of circle * density 
	"""
	mass = (4.0 / 3.0) * sam.CONSTANT_pi * r**3.0 * rho
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

	if (fpp == 1.0) and (psi == 1.0) and (cpp == 1.0):
	# separates these for sake of computational efficiency
	## ie don't bother multiplying by 1 when you don't have to
		epsilon = sam.CONSTANT_ppConstant * rho * X**2 * (T/1.0e6)**4
	else:	
		epsilon = sam.CONSTANT_ppConstant * rho * X**2 * fpp * psi * cpp * (T/1.0e6)**4

	return epsilon


def specific_energy_cno(X,Xcno,rho,T):
	"""
	calculates specific energy for the proton-proton chain

	:inputs:
		X [float]
			'--> the mass fraction of hydrogen
		Xcno [float,int]
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
	epsilon = sam.CONSTANT_cnoConstant * rho * X * Xcno * (T / 1.0e6)**19.9
	return epsilon


if __name__ == "__main__":
	dr = 1.0e+5
	rBound = 7e+8
	r = np.arange(0,rBound,dr)
	rho = 1410.0
	massGrad = mass_gradient(r,rho,autoDebug=False)

	internalMassTest = sam.sig_proc.integrate(massGrad,dx=1.0e5)
	internalMass = internal_mass(r[:-2],rho)

	# both = np.concatenate( (internalMassTest, internalMass ), axis=1 )
	# sub = internalMassTest - internalMass

	# np.savetxt("sub.txt",sub)
	np.savetxt("sig.txt",internalMassTest)
	np.savetxt("ast.txt",internalMass)
