import numpy as np
from math import sqrt
import sam

def blackbody_fit(wavelengths,emissivity,tempRange=(100,6500),step=5,rtype="dict",autoDebug=True):
	#Error Checking
	if autoDebug == True:
		sam.type_check(wavelengths,np.ndarray,'wavelengths')
		sam.type_check(emissivity,np.ndarray,'emissivity')
		sam.value_check(emissivity.shape,(wavelengths.shape,),'discrete','emissivity')
		sam.type_check(tempRange, (tuple,list,np.ndarray),'tempRange')
		sam.value_check( len(tempRange), (1), 'f', "tempRange")
		sam.type_check(step, (float,int), 'step')
		if len(tempRange) <= 2:
			sam.value_check(step,(tempRange[-1]-tempRange[0])/2,'g',"tempRange")
		sam.type_check(rtype,str,'rtype')
		sam.value_check(rtype, [0,"tuple","t","list",1,"dict","dictionary","d"], "d", "rtype")


	try:
		#Checking for normalization
		if np.max(emissivity) > 1.0:
			emissivity = emissivity / np.max(emissivity)
		if len(tempRange) == 2:
			tempRange = range(tempRange[0],tempRange[1],step)

		RMS = np.zeros(len(tempRange))
		for index,temp in enumerate(tempRange):
			bb = sam.blackbody(T=temp, ranges=wavelengths, normalize=True)
			rms = sam.rms2(bb,emissivity)
			RMS[index] = rms

		bestFitTemp= tempRange[ np.argmin(RMS) ]
		bestBlackbody = sam.blackbody(T=bestFitTemp,ranges=wavelengths)


		if rtype in [0,"tuple","t","list"]:
			return wavelengths, emissivity, bestBlackbody, np.asarray(RMS), bestFitTemp
		if rtype in [1,"dict","dictionary","d"]:
			return {"wavelengths":wavelengths,"emissivity":emissivity,"bestBlackbody":bestBlackbody, "rms":np.asarray(RMS),"bestFitTemp":bestFitTemp}


	except Exception as e:
		sam.debug(e)


if __name__ == "__main__":
	import time	
	startTime = time.time()	
	dataFiles = ["data/Dark_spectrum.txt","data/Known_spectrum.txt","data/Tungsten_spectrum.txt"]
	saveNames = ["output/Blackbody/Dark_plot.pdf","output/Blackbody/Known_plot.pdf","output/Blackbody/Tungsten_plot.pdf"]

	for fileIndex,file in enumerate(dataFiles):
		source = sam.retrieve_structured_data(filename=file)
		source["wavelengths"] = source["wavelengths"] * 1e-3 #converting to microns
		wavelengths, emissivity, bestBlackbody, RMS, bestFitTemp = blackbody_fit(source["wavelengths"],source["emissivity"],rtype="tuple")
		peakLambda = sam.wiens_peak(bestFitTemp)
		plot = sam.quickplot(filename=saveNames[fileIndex],
							values=( (wavelengths,emissivity),(wavelengths,bestBlackbody) ), 
							colors=('r','g'), 
							labels=("blackbody approximation at {0}".format(bestFitTemp),file),
							yLimits=(0,1.2),
							xLimits=(.3,1.05),
							verticalMarkers=(peakLambda,),
							save=True,
							display=False,
							clearFig = True )
