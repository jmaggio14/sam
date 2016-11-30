import numpy as np
import sam

def jeans_mass(u,T,rho):
	"""
	calculates the jean's mass of an ISM cloud
	Mj = ( (5kT) / (G*µ*mH) )^(3/2) * (3 / (4*pi*rho) )

	where k is Boltzmann, T is temperature, G is Newton's constant
	µ is the number of nucleons (?), mH is mass of hydrogen
	rho is the density of the cloud

	WIP -- needs auto-error checking
	"""
	firstTerm = ( (5 * sam.CONSTANT_k * T) / (sam.CONSTANT_G * u * sam.CONSTANT_mh) )**1.5
	secondTerm =  (3 / (4 * sam.CONSTANT_pi * rho) )**.5 
	Mj = firstTerm * secondTerm
	return Mj

def jeans_mass2(u,T,n):
	pass
	"""
	calculates the jean's mass of an ISM cloud, uses 
	Mj = ( (375 k^3) / (4 * pi * (µ*mH)^4 * G^3) )

	WIP -- needs auto-error checking
	"""
