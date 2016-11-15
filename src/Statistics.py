import numpy as np
import math


def rms(array):
	N = array.size
	arraySquared = array**2
	rms = math.sqrt( np.sum(arraySquared) / N )	
	return rms

def rms2(array1,array2):
	"""calculates root mean squared of two sets"""
	N = array1.size
	diffSquared = (array1 - array2)**2
	rms = math.sqrt( np.sum(diffSquared) / N ) 
	return rms
