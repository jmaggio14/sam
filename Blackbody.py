import numpy as np
import sam
def blackbody(T=5800, ranges=(0.35,2.5), step=.005, normalize=True,
									verbose=False, filename='planckian_bb.pdf'):
	"""
	:TITLE:
		generate_blackbody 

	:PURPOSE:
		generates a planckian blackbody curve

	:INPUTS:
		ranges [tuple,list,np.ndarray] 
			'--> wavelength boundries in microns
		step [int,float]
			'--> value of discrete iteration
		temp [int,float]
			'--> temperature to be used in calculation in kelvin
		verbose [bool]
			'--> whether or not to display figure
		filename [string]
			'--> name of 

	:RETURN:
		#IF VERBOSE
			radiances [np.ndarray]
				'--> array of radiance values for planckian blackbody
		#ELSE
			radiances [np.ndarray] | plotObject [matplotlib.pyplot]
				'--> array of radiance values and plotting object
	"""
	#ERROR CHECKING INPUTS
	blackbody_errorcheck(T=T,ranges=ranges,step=step,verbose=verbose,filename=filename)

	if len(ranges) > 2:
		wavelengths = ranges
	else:
		wavelengths = np.arange(ranges[0],ranges[1],step)

	h = sam.SAM_h
	c = sam.SAM_c
	k = sam.SAM_k
	e = sam.SAM_e
	calcWavelengths = wavelengths * 1e-6
	radiances = (2*h*c**2) / ( ((calcWavelengths)**5) * (e**((h*c) / ( (calcWavelengths)*k*T)) ))

	if normalize == True:
		radiances = radiances / np.max(radiances)

	if verbose == True:
		import matplotlib.pyplot as plt
		yLabel = "relative radiance" if normalize == True else "radiance [W m^-2 sr^-1]"
		peak = sam.wiens_peak(T)
		plt.title(filename)
		plt.plot(wavelengths,radiances, color='r', label="planckian blackbody")
		plt.xlabel("wavelength [um]")
		plt.ylabel(yLabel)
		plt.axvline(peak, color='g',label = "bb peak at {0}".format(peak))
		plt.savefig(filename)
		plt.legend()
		return radiances,plt
	else:
		return radiances



def wiens_peak(T):
	peak = (2897.7729) / T 
	return peak

def wiens_temp(peak):
	temp = (2897.7729) / peak
	return temp



def blackbody_errorcheck(T, ranges, step, verbose, filename):
		#--------- BEGIN ERROR CHECKING -----------#
	if isinstance(ranges,(tuple,list,np.ndarray)) == False:
		print("input 'ranges' must be array-like type \
					| currently {0}".format(type(ranges)))
		raise TypeError

	# if len(ranges) != 2:
	# 	print("input 'ranges' must only contain 2 points\
	# 				| currently contains {0}".format(len(ranges)))
	# 	raise ValueError

	if isinstance(ranges[0],(int,float,np.float32)) == False:
		print("starting point in 'ranges' must be either float or int \
					| currently type {0}".format(type(ranges[0])))
		raise ValueError

	if isinstance(ranges[1],(int,float,np.float32)) == False:
		print("ending point in 'ranges' must be either float or int \
					| currently type {0}".format(type(ranges[1])))
		raise ValueError

	if isinstance(step,(int,float)) == False:
		print("input 'step' must be int or float type \
					| currently {0}".format(type(step)))
		raise TypeError

	if isinstance(T,(float,int)) == False:
		print("input 'T' must be int or float type \
					| currently {0}".format(type(step)))
		raise TypeError

	if isinstance(verbose,bool) == False:
		print("input 'verbose' must be boolean [int] \
					| currently {0}".format(type(verbose)))
		raise TypeError

	if isinstance(filename,str) == False:
		print("input 'filename must be a string\
					| currently {0}".format(type(filename)))
		raise TypeError
	#---------- END ERROR CHECKING ------------#


if __name__ == "__main__":
	plot = blackbody(T=3660,verbose = True)[1]
	peak = wiens_peak(3660)
	temp = wiens_temp(peak)
	plot.show()






