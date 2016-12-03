import sys
import os
import logging
import yaml
import os
import glob
import sam


class Config(object):

	def __init__(self):
		self._path = None
		self._verified = False
		self._configs = self.parse_input()
		self.validate_configs()        
    
	def load_config(self):
		if self._verified:
			configFile = open(self._path)
			configs = yaml.safe_load(configFile)
			configFile.close()
			return configs
		else:
			print("config file not verified, run parse_input()")

	def check_config_path(self):
		if self._path == None:
			self._path = ""

		if (".yaml" in self._path) and os.path.exists(self._path):
			#only create config var if valid YAML file
			self._verified = True
		else:
			print("\r\ncould not find specified config file\r\n")
			discoveredYamlFiles = glob.glob("*.yaml")
			
			if len(discoveredYamlFiles) > 0:
				userResponse = input("use {0} instead: Y/n?\r\n".format(discoveredYamlFiles[0]))
				if userResponse in ["yes","Y",'y',"YES",'']:
					self._path = discoveredYamlFiles[0]
					self._verified = True
				else:
					print("exiting...")
					sys.exit()

	def parse_input(self):
		args = sys.argv
		#initializing Sys Variables
		configs = None
		loggingLevel = logging.INFO
		logLevelDict = {"d":logging.DEBUG,"debug":logging.DEBUG,
						"i":logging.INFO,"info":logging.INFO,
						"w":logging.WARNING,"warning":logging.WARNING,
						"e":logging.ERROR, "error":logging.ERROR,
						"c":logging.CRITICAL,"critical":logging.CRITICAL}
		if len(args) == 1:
			self.check_config_path()
			configs = self.load_config()

		if len(args) == 2:
			self._path = args[1]
			self.check_config_path()
			configs = self.load_config()

		if len(args) > 2:
			self._path = args[1]
			loggingInput = args[2].replace('-','').lower()

			self.check_config_path()
			configs = self.load_config()
			
			if loggingInput in logLevelDict:
				loggingLevel = logLevelDict[loggingInput]
			elif loggingInput.isdigit():
				if int(loggingInput) in range(0,logging.CRITICAL):
					loggingLevel = loggingInput
			else:
				print("logging input not interpretable")

		return configs


	def validate_configs(self):
		"""
		thoroughly hardcoded method used to validate the config inputs
		"""

		#mass
		mass = self._configs["mass"]
		sam.type_check(mass,sam.TYPES_numbers,'mass')
		sam.value_check(mass,.0,'>','mass')
		
		#mass-fractions
		mF = self._configs["mass_fractions"]
		X = mF["X"]
		sam.type_check(X,float,'Config: X')
		sam.value_check(X,.0,'>','Config: X')
		Y = mF["Y"]
		sam.type_check(Y,float,'Config: Y')
		sam.value_check(Y,.0,'>','Config: Y')
		Z = mF["Z"]
		sam.type_check(Z,float,'Config: Z')
		sam.value_check(Z,.0,'>','Config: Z')

		#effective_temperature
		# temp = self._configs["effective_temperature"]
		# sam.type_check(temp,sam.TYPES_numbers,'Config: effective_temperature')
		# sam.value_check(temp,.0,'>','Config: effective_temperature')

		#radii filename
		# rFilename = self._configs["radii_filename"]
		# sam.type_check(rFilename,str,'Config: radii_filename')
		# sam.path_check(rFilename)

		#average pressure
		# rho = self._configs["average_pressure"]
		# sam.type_check(rho,sam.TYPES_numbers,'Config: average_pressure')
		# sam.value_check(rho,.0,'>','Config: average_pressure')



if __name__ == "__main__":
	configs = Config()._configs
	print(configs)
