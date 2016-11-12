import numpy as np
from math import sqrt
import sam

def blackbody_fit(wavelengths,emissivity,tempRange=(100,6500),step=5,rtype="dict",units="nm"):
	#Checking for normalization
	try:
		if np.max(emissivity) > 1.0:
			emissivity = emissivity / np.max(emissivity)
		if len(tempRange) == 2:
			tempRange = range(tempRange[0],tempRange[1],step)

		RMS = np.zeros(len(tempRange))
		N = wavelengths.size

		for index,temp in enumerate(tempRange):
			bb = sam.blackbody(T=temp, ranges=wavelengths, normalize=True)
			rms = sqrt( np.sum( (bb - emissivity)**2 ) / N )
			RMS[index] = rms

		bestFitTemp= tempRange[ np.argmin(RMS) ]
		bestBlackbody = sam.blackbody(T=bestFitTemp,ranges=wavelengths,normalize=True)


		if rtype in [0,"tuple","t","list"]:
			return wavelengths, emissivity, bestBlackbody, np.asarray(RMS), bestFitTemp
		if rtype in [1,"dict","dictionary","d"]:
			return {"wavelengths":wavelengths,"emissivity":emissivity,"bestBlackbody":bestBlackbody, "rms":np.asarray(RMS),"bestFitTemp":bestFitTemp}


	except Exception as e:
		sam.debug(e)


if __name__ == "__main__":
	import time

	for file in ["data/Dark_spectrum.txt","data/Known_spectrum.txt","data/Tungsten_spectrum.txt"]:
		startTime = time.time()	
		source = sam.retrieve_structured_data(filename=file)
		source["wavelengths"] = source["wavelengths"] / 1e3 #converting to microns
		wavelengths, emissivity, bestBlackbody, RMS, bestFitTemp = blackbody_fit(source["wavelengths"],source["emissivity"],rtype="tuple")
		peakLambda = sam.wiens_peak(bestFitTemp)
		plot = sam.quickplot(values=( (wavelengths,emissivity),(wavelengths,bestBlackbody) ), 
							colors=('r','g'), 
							labels=("blackbody approximation at {0}".format(bestFitTemp),file),
							yLimits=(0,1.2),
							xLimits=(.3,1.05) )

		# plot = sam.quickplot(values=( (wavelengths,emissivity), ), 
		# 					colors=('r',), 
		# 					labels=("blackbody approximation at {0}".format(bestFitTemp),),
		# 					yLimits=(0,1.2) )
		plot.show()
