import numpy
import math    

# Destination depths
SAM_8U = numpy.uint8      # 8-bit unsigned int
SAM_8S = numpy.int8       # 8-bit signed int
SAM_16U = numpy.uint16    # 16-bit unsigned int
SAM_16S = numpy.int16     # 16-bit signed int
SAM_32S = numpy.int32     # 32-bit signed int
SAM_32F = numpy.float32   # 32-bit float (single precision)
SAM_64F = numpy.float64   # 64-bit float (double precision)

#### UNIVERSAL CONSTANTS ####

#pi
SAM_pi = math.pi #pi

#e
SAM_e = math.e

#Boltzman's constant
SAM_Boltzmann = 1.38064852e-23
SAM_k = SAM_Boltzmann

#planck's constant
SAM_Planck = 6.62607004e-34
SAM_h = SAM_Planck 
SAM_hbar = 1.054571800e-34

#planck Length
SAM_l = 1.616199e-35
SAM_PlanckLength = SAM_l

#Gravitational Constant (Newton's Constant)
SAM_G = 6.67408e-11
SAM_Newton = SAM_G

#Speed of Light
SAM_c = 2.99792458e8

#Stefan-Boltzman Constant
SAM_sigma = 5.670373e-8
SAM_StefanBoltzmann = SAM_sigma
SAM_proportionality = SAM_sigma
SAM_SB = SAM_sigma

#Bohr's radius
SAM_a0 = 5.2917721067e-11

#Proton Mass
SAM_protonMass = 1.672621898e-27
SAM_mp = SAM_protonMass

#Election Mass
SAM_electronMass = 9.10936356e-31
sam_me = SAM_electronMass

#Rydberg Constant
SAM_Rydberg = 1.0973731568508e7
SAM_R = SAM_Rydberg



