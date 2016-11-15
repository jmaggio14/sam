import sys
import os
import logging
import yaml
import os
import glob

class Config(object):

	def __init__(self):
		self._path = None
		self._verified = False
		self._configs = self.parse_input()           
    
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

if __name__ == "__main__":
	configs = Config()._configs
	print(configs)
