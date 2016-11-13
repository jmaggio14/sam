import sys
import os
import System #File in this directory -- not downloadable module
import logging


#loading in command line arguments
args = sys.argv

#Creating system wide logger object


#initializing Sys Variables
configPath = None
configs = None
debugMode = False

if len(args) == 1:
	arg1 = sys.argv[0]
	if ".yaml" in arg1:
		#only create config var if it exists
		if os.path.exists(arg1):
			configPath = arg1
		else
			logging


