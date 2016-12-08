import sam
import numpy as np


def mean_molecular_weight(X,Y,Z):
    """
	calcualtes mean molecular weight based off of X, Y & Z
    """
    mu = (1/(2*X + 3*Y/4 + Z/2))
    return mu


def boundary_temperature(r,Rs,mu,Ms):
	"""
	calculates approximation to start numerical integration

	uses equation L.2 in B.O.B.
	"""
	G = sam.CONSTANT_G
	k = sam.CONSTANT_k
	mh = sam.CONSTANT_mh

	T = G * Ms * (mu * mh) / (4.25 * k) * (1.0/r - 1.0/Rs )
	return T

def boundary_pressure(Ms,Ls,mu,T,A,rho):
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

def temperature_from_gradient(dT1,dT2,dr):
	temp = np.mean([dT2,dT1]) * dr
	return temp

	
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

def gas_pressure1(rho,T,mu,autoDebug=True):
	Pg = (rho * sam.CONSTANT_k * T ) / (mu * sam.CONSTANT_mh)
	return Pg

def radiation_pressure(T):
	Pr = sam.CONSTANT_third * sam.CONSTANT_a * T**4
	return Pr

def pressure(rho,T,mu):
	Ps = gas_pressure1(rho,T,mu) + radiation_pressure(T)
	return Ps

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
	

def boundry_extinction(X,Z,t=None,g=1):
	"""
	where t is guillotine factor
	"""	
	if t == None:
		t = 2.82 * ( rho*(1 + X) )**.2

	bf = (sa.CONSTANT_Abf / t) * Z * (1 + X)
	ff = sam.CONSTANT_Aff * g * (1-Z) * (1+X)
	A = bf + ff
	return A