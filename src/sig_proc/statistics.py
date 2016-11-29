import numpy as np
import math


def rms(array):
	rms = np.sqrt(np.mean(np.square(array)))	
	return rms

def rms2(array1,array2):
	"""calculates root mean squared of two sets"""
	N = array1.size
	diffSquared = (array1 - array2)**2
	rms = math.sqrt( np.sum(diffSquared) / N ) 
	return rms

def noise_rms(array):
	rms = np.sqrt(np.mean( np.square(array - np.mean(array)) ) )
	return rms

# def average_samples(array,avgSize):
# 	if (array.size / avgSize).is_integer():
# 		 avgs = np.reshape(-1,avgSize).mean(axis=1)
# 	else:
		
def snr(array):
	rms = noise_rms(array)
	snr = np.mean(array) / rms
	return snr


if __name__ == "__main__":
	data = np.genfromtxt("2data.csv",delimiter=",",names=True)
	noiseRmsA = noise_rms(data["Sa2"])
	rmsB = noise_rms(data["Sb2"])
	print(noiseRmsA, rmsB )
	print(snr(data["Sa2"]),snr(data["Sb2"]) )
