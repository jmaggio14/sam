import numpy as np
import math    

# Destination depths
SAM_8U = np.uint8      # 8-bit unsigned int
SAM_8S = np.int8       # 8-bit signed int
SAM_16U = np.uint16    # 16-bit unsigned int
SAM_16S = np.int16     # 16-bit signed int
SAM_32S = np.int32     # 32-bit signed int
SAM_32F = np.float32   # 32-bit float (single precision)
SAM_64F = np.float64   # 64-bit float (double precision)

#Standard type tables (for error checking)
SAM_TYPES_math = (np.ndarray,int,float)
SAM_TYPES_lists = (np.ndarray,list,tuple)
SAM_TYPES_numbers = (int,float)


####======= UNIVERSAL CONSTANTS ========####

#pi
SAM_pi = math.pi #pi

#e
SAM_e = math.e

#Boltzman's constant
SAM_boltzmann = 1.38064852e-23
SAM_k = SAM_boltzmann

#planck's constant
SAM_planck = 6.62607004e-34
SAM_h = SAM_planck 
SAM_hbar = 1.054571800e-34

#planck Length
SAM_l = 1.616199e-35
SAM_planckLength = SAM_l

#Gravitational Constant (Newton's Constant)
SAM_G = 6.67408e-11
SAM_newton = SAM_G

#Speed of Light
SAM_c = 2.99792458e8
SAM_speedOfLight = SAM_c

#Stefan-Boltzman Constant
SAM_stefanBoltzmann = 5.670373e-8
SAM_SB = SAM_stefanBoltzmann

#Bohr's radius
SAM_a0 = 5.2917721067e-11

#electron scattering cross section
SAM_electronCrossSection = 6.65e-29

#Proton Mass
SAM_protonMass = 1.672621898e-27
SAM_mp = SAM_protonMass

#Election Mass
SAM_electronMass = 9.10936356e-31
sam_me = SAM_electronMass

#Rydberg Constant
SAM_rydberg = 1.0973731568508e7
SAM_R = SAM_rydberg