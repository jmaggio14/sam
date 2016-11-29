"""
WORK IN PROGRESS!
	necessary to add some manner of error correction 
	to detect whether or not data is structured
"""
import numpy as np

def retrieve_data(filename,skipHeaders=0,structured=True,delimiter=','):
	if structured == True:
		data = retrieve_structured_data(filename=filename,skipHeaders=skipHeaders,delimiter=delimiter)
	else:
		data = retrieve_non_structured_data(filename=filename,skipHeaders=skipHeaders,delimiter=delimiter)
	return data

def retrieve_structured_data(filename,skipHeaders=0,delimiter=','):
	data = np.genfromtxt(fname=filename,skip_header=skipHeaders,delimiter=delimiter,names=True)
	return data

def retrieve_non_structured_data(filename,skipHeaders=0,delimiter=','):
	data = np.genfromtxt(fname=filename,skip_header=skipHeaders,delimiter=delimiter)
	return data