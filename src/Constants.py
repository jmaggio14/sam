import numpy as np
"""
add:
	light year <--> meter conversion
	imperial <--> metric  conversions

"""


###=========== TYPES ==============##

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



######======= SOLAR ATTRIBUTES ======####

#solar mass
SAM_solarMass = 1.9891e30
SAM_Ms = SAM_solarMass

#solar luminosity
SAM_solarLuminosity = 3.839e26
SAM_Ls = SAM_solarLuminosity

#solar radius
SAM_solarRadius = 6.955e8
SAM_Rs = SAM_solarRadius

#solar effective surface temperature
SAM_solarTemperature = 5777
SAM_Ts = SAM_solarTemperature



######============= CONVERSIONS =======####
SAM_pc_to_m = 3.0856776e16
SAM_m_to_pc = (1.0 / SAM_pc_to_m)



####======= UNIVERSAL CONSTANTS ========####

#pi
SAM_pi = np.pi #pi

#e
SAM_e = np.e

#Boltzman's constant
SAM_boltzmann = 1.38064852e-23
SAM_k = SAM_boltzmann

#planck's constant
SAM_planck = 6.62607004e-34
SAM_h = SAM_planck 
SAM_hbar = 1.054571800e-34

#planck Length
SAM_planckLength = 1.616199e-35
SAM_l = SAM_planckLength

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

#Hydrogren mass
SAM_hydrogrenMass = 1.673532499e-27
SAM_mh = SAM_hydrogrenMass

#Election Mass
SAM_electronMass = 9.10936356e-31
SAM_me = SAM_electronMass

#Rydberg Constant
SAM_rydberg = 1.0973731568508e7
SAM_R = SAM_rydberg

#Radiation Constant
SAM_radationConstant = 4.0 * SAM_stefanBoltzmann / SAM_c
SAM_a = SAM_radationConstant

#specific energies for CNO cycle and PP chain
SAM_ppConstant = 1.08e-12
SAM_cnoConstant = 8.24e-31



