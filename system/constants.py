import numpy as np
"""
add:
	light year <--> meter conversion
	imperial <--> metric  conversions

"""

###=========== TYPES ==============##

# Destination depths
TYPE_8U = np.uint8      # 8-bit unsigned int
TYPE_8S = np.int8       # 8-bit signed int
TYPE_16U = np.uint16    # 16-bit unsigned int
TYPE_16S = np.int16     # 16-bit signed int
TYPE_32S = np.int32     # 32-bit signed int
TYPE_32F = np.float32   # 32-bit float (single precision)
TYPE_64F = np.float64   # 64-bit float (double precision)
TYPE_64C = np.complex64 # 64-bit complex float
TYPE_128C = np.complex128 # 128-bit complex float

#Standard type tables (for error checking)
TYPES_math = (np.ndarray,int,float)
TYPES_lists = (np.ndarray,list,tuple)
TYPES_numbers = (int,float)
TYPES_pythonLists = (list,tuple)
TYPES_depths =( TYPE_8U,
				TYPE_8S, 
				TYPE_16U,
				TYPE_16S,
				TYPE_32S,
				TYPE_32F,
				TYPE_64F,
				TYPE_64C,
				TYPE_128C )

TYPES_intDepths = ( TYPE_8U,
					TYPE_8S, 
					TYPE_16U,
					TYPE_16S,
					TYPE_32S )

TYPES_floatDepths = ( TYPE_32F, TYPE_64F )
TYPES_complexDepths = ( TYPE_64C,TYPE_128C )
 

### DATA PATH (ONLY WORKS ON CIS SERVERS)
PATH_data = "~/src/python/data/examples"

######======= SOLAR ATTRIBUTES ======####

#solar mass
SOLAR_solarMass = 1.9891e30
SOLAR_Ms = SOLAR_solarMass

#solar luminosity
SOLAR_solarLuminosity = 3.839e26
SOLAR_Ls = SOLAR_solarLuminosity

#solar radius
SOLAR_solarRadius = 6.955e8
SOLAR_Rs = SOLAR_solarRadius

#solar effective surface temperature
SOLAR_solarTemperature = 5777
SOLAR_Ts = SOLAR_solarTemperature



######============= CONVERSIONS =======####

#distances
CONVERT_pc_to_m = 3.0856776e16
CONVERT_m_to_pc = 1.0 / CONVERT_pc_to_m

CONVERT_pc_to_ly = 0.306601
CONVERT_ly_to_pc = 1.0 / CONVERT_pc_to_ly

CONVERT_m_to_ly = 1.057e-16
CONVERT_ly_to_m = 1.0 / CONVERT_m_to_ly

CONVERT_m_to_au = 6.68459e-12
CONVERT_au_to_m = 1.0 / CONVERT_m_to_au

CONVERT_nm_to_m = 1e-9
CONVERT_nm_to_m = 1.0 / CONVERT_nm_to_m

CONVERT_um_to_m = 1e-6
CONVERT_um_to_m = 1.0 / CONVERT_um_to_m

CONVERT_cm_to_m = 1e-2
CONVERT_m_to_cm = 1.0 / CONVERT_cm_to_m

CONVERT_A_to_m = 1e-10
CONVERT_A_to_m = 1.0 / CONVERT_A_to_m

#energy
CONVERT_j_to_ev = 6.242e+18
CONVERT_ev_to_j = 1.0 / CONVERT_j_to_ev


####======= UNIVERSAL CONSTANTS ========####

#fractions
CONSTANT_half    = 1.0 / 2.0
CONSTANT_third   = 1.0 / 3.0
CONSTANT_fourth  = 1.0 / 4.0
CONSTANT_fifth   = 1.0 / 5.0
CONSTANT_sixth   = 1.0 / 6.0
CONSTANT_seventh = 1.0 / 7.0
CONSTANT_eighth  = 1.0 / 8.0
CONSTANT_ninth   = 1.0 / 7.0
CONSTANT_tenth   = 1.0 / 10.0

#pi
CONSTANT_pi = np.pi #pi
CONSTANT_2pi = 2.0 * CONSTANT_pi
CONSTANT_4pi = 4.0 * CONSTANT_pi
CONSTANT_16pi = 16.0 * CONSTANT_pi


#e
CONSTANT_e = np.e

#Boltzman's constant
CONSTANT_boltzmann = 1.38064852e-23
CONSTANT_k = CONSTANT_boltzmann

#planck's constant
CONSTANT_planck = 6.62607004e-34
CONSTANT_h = CONSTANT_planck 
CONSTANT_hbar = 1.054571800e-34

#planck Length
CONSTANT_planckLength = 1.616199e-35
CONSTANT_l = CONSTANT_planckLength

#Gravitational Constant (Newton's Constant)
CONSTANT_G = 6.67408e-11
CONSTANT_newton = CONSTANT_G

#Speed of Light
CONSTANT_c = 2.99792458e8
CONSTANT_speedOfLight = CONSTANT_c

#Stefan-Boltzman Constant
CONSTANT_stefanBoltzmann = 5.670373e-8
CONSTANT_SB = CONSTANT_stefanBoltzmann

#Bohr's radius
CONSTANT_a0 = 5.2917721067e-11

#electron scattering cross section
CONSTANT_electronCrossSection = 6.65e-29

#Proton Mass
CONSTANT_protonMass = 1.672621898e-27
CONSTANT_mp = CONSTANT_protonMass

#Hydrogren mass
CONSTANT_hydrogrenMass = 1.673532499e-27
CONSTANT_mh = CONSTANT_hydrogrenMass

#Election Mass
CONSTANT_electronMass = 9.10936356e-31
CONSTANT_me = CONSTANT_electronMass

#Rydberg Constant
CONSTANT_rydberg = 1.0973731568508e7
CONSTANT_R = CONSTANT_rydberg

#Radiation Constant
CONSTANT_radationConstant = 4.0 * CONSTANT_stefanBoltzmann / CONSTANT_c
CONSTANT_a = CONSTANT_radationConstant

#specific energies for CNO cycle and PP chain {J/kg}
CONSTANT_ppConstant = 1.08e-12
CONSTANT_cnoConstant = 8.24e-31

#Univeral gas constant {J * mol^-2 K^-1}
CONSTANT_gasConstant = 8.214472
CONSTANT_Rg = CONSTANT_gasConstant

#Bound Free opacity constant
CONSTANT_Abf = 4.34e21
CONSTANT_boundFreeConstant = CONSTANT_Abf 

#Free Free opacity constant
CONSTANT_Aff = 3.68e18
CONSTANT_freeFreeConstant = CONSTANT_Aff 

#Free-free gaunt factor
CONSTANT_gff = 1.0
CONSTANT_gauntFactor = 1.0

# Xcno constant
CONSTANT_Xcno = 0.0141
