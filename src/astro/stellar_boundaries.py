import numpy as np
import sam

def boundaries(attributes):
	a = attributes
	bounds = {}
	prevR = a["Rs"]
	bounds["r"] = a["Rs"] - a["dr"]
	#initial temperature calculated using radiation equations by necessesity
	guillotine = .01 #same assumption as made in StatStar


	# startingT = 5777
	startingT = surface_temp_convective(a["Ms"],a["gammaRatio"],a["mu"],bounds["r"],a["Rs"]) 
	A = extinction(a["X"],a["Z"],guillotine)
	startingP = surface_pressure(a["Ms"],a["Ls"],A,a["mu"],startingT)


	bounds["T"] = startingT
	bounds["P"] = startingP
	# bounds[""] = 86.8
	bounds["rho"] = rho( bounds["T"],bounds["P"],a["mu"] )
	bounds["kappa"] = a["OPAC"].value( bounds["rho"],bounds["T"] )
	bounds["epsilon"] = specific_energy( bounds["T"],bounds["rho"],a["X"],a["Z"] )

	return bounds

	#---------------------------------------------------------

	# initKappa = a["OPAC"].value(initRho,initT)
	# initT = radiation_temperature(bounds["r"],prevR,a["Ms"],a["mu"])
	# initP = radiation_pressure(a["Ms"],a["Ls"],a["mu"],initT,initA)
	# initRho = rho(initT,initP,a["mu"])

	#calculating more resonable values using adiabatic approx
	# bounds["T"] = adiabatic_temperature(bounds["r"],prevR,a["Ms"],a["gammaRatio"],a["mu"])
	# bounds["P"] = adiabatic_pressure(bounds["r"],prevR,initP,bounds["T"],initT,a["gammaRatio"]) 	


def surface_pressure(Ms,Ls,A,mu,T):
	"""
	calculates approximation of pressure for the purposes 
	of numerical integration

	uses eq. L.1 in BOB
	"""
	G = sam.CONSTANT_G
	mh = sam.CONSTANT_mh
	c = sam.CONSTANT_c
	k = sam.CONSTANT_k
	a = sam.CONSTANT_a
	pi = sam.CONSTANT_pi

	numerator = 16 * pi * G * Ms * a * c * k
	denominator = 4.25 * 3 * Ls * A * mu * mh 

	pressure = (numerator / denominator)**.5 * T**4.25
	return pressure



def surface_temp_convective(Ms,gammaRatio,mu,r,Rs):
	G = sam.CONSTANT_G
	k = sam.CONSTANT_k
	mh = sam.CONSTANT_mh

	T = G * Ms * (1 / gammaRatio) * (mu * mh)/k * (1/r - 1/Rs)
	return T


def adiabatic_temperature(r,r2,Ms,gammaRatio,mu):
	#setting constants to shorter vars for aesthetics
	G = sam.CONSTANT_G
	mh = sam.CONSTANT_mh
	k = sam.CONSTANT_k

	T = sam.CONSTANT_G * Ms * ( (mu * mh) / (k * gammaRatio) ) * (1/r - 1/r2)
	return T

def adiabatic_pressure(r,r2,P,T,T2,gammaRatio):
	#setting Constants
	K = P / (T2**gammaRatio)
	P = K * T**gammaRatio
	return P 

# def initial_temperature(r,r2,Ms,gammaRatio):
# 	G = sam.CONSTANT_G
# 	mh = sam.CONSTANT_mh
# 	k = sam.CONSTANT_k

# 	T = G * Ms * 

# def surface_dPdr(Ms,Ls,kappa):
# 	"""
# 	calculates approximation of pressure for the purposes 
# 	of numerical integration

# 	uses eq. L.1 in BOB
# 	"""
# 	G = sam.CONSTANT_G
# 	mh = sam.CONSTANT_mh
# 	c = sam.CONSTANT_c
# 	k = sam.CONSTANT_k
# 	a = sam.CONSTANT_a
# 	pi = sam.CONSTANT_pi

# 	numerator = 16 * pi * G * Ms * a *c * k
# 	denominator = 4.25 * 3 * Ls * A * mu * mh 

# 	pressure = (numerator / denominator)**.5 * T**4.25
# 	return pressure





def extinction(X,Z,t,g = 1.0):
	Abf = sam.CONSTANT_Abf
	Aff = sam.CONSTANT_Aff
	A = (Abf / t) * Z * (1 + X) + Aff * (1 - Z) * (1 + X)
	return A

def radiation_temperature(r,r2,Ms,mu): #r2 is lastR
	G = sam.CONSTANT_G
	mh = sam.CONSTANT_mh
	k = sam.CONSTANT_k

	T = G * Ms * ( (mu*mh) / (4.25*k) ) * (1/r - 1/r2)
	return T




def radiation_pressure(Ms,Ls,mu,T,A):
	"""
	calculates approximation of pressure for the purposes 
	of numerical integration

	uses eq. L.1 in BOB
	"""
	G = sam.CONSTANT_G
	mh = sam.CONSTANT_mh
	c = sam.CONSTANT_c
	k = sam.CONSTANT_k
	a = sam.CONSTANT_a
	pi = sam.CONSTANT_pi

	numerator = 16 * pi * G * Ms * a *c * k
	denominator = 4.25 * 3 * Ls * A * mu * mh 

	pressure = (numerator / denominator)**.5 * T**4.25
	return pressure



def rho(T,P,mu,autoDebug=True):
	if autoDebug:
		sam.type_check(T,sam.TYPES_numbers,'T')
		sam.type_check(P,sam.TYPES_numbers,'P')
		sam.type_check(mu,sam.TYPES_numbers,'mu')

	Pg = gas_pressure2(T,P)
	rho = (Pg * mu * sam.CONSTANT_mh) / (sam.CONSTANT_k * T)
	return rho

def density(T,P,mu,autoDebug=True):
	return rho(T,P,mu,autoDebug)

def gas_pressure2(T,P,autoDebug=True):
	"""
	calculcates gas pressure by subtracting radiation pressure from
	total pressure in star 
	"""
	if autoDebug:
		sam.type_check(T,sam.TYPES_numbers,'T')
		sam.type_check(P,sam.TYPES_numbers,'P')

	Pg = P - (sam.CONSTANT_third * sam.CONSTANT_a * T**4)
	return Pg

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


def specific_energy_cno(X,rho,T):
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
	Xcno = sam.CONSTANT_Xcno
	epsilon = sam.CONSTANT_cnoConstant * rho * X * Xcno * (T / 1.0e6)**19.9
	return epsilon




def specific_energy(X,rho,T,autoDebug=True):
	epsilonPP = specific_energy_pp(X,rho,T)
	epsilonCNO = specific_energy_pp(X,rho,T)
	epsilon = epsilonPP + epsilonCNO 
	return epsilon


class BoundaryInvalid( Exception ):
	pass


