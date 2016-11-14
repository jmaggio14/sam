import sys
import os
import logging
import yaml
import os
import glob

def load_config(configPath):
	configFile = open(configPath)
	configs = yaml.safe_load(configFile)
	return configs

def get_config_path(path):
	if (".yaml" in path) and os.path.exists(path):
		#only create config var if valid YAML file
		configPath = path
	else:
		print("\r\ncould not find specified config file\r\n")
		discoveredYamlFiles = glob.glob("./*.yaml")
		if len(discoveredYamlFiles) > 0:
			userResponse = input("use {0} instead: Y/n?\r\n".format(discoveredYamlFiles[0]))
			if userResponse in ["yes","Y",'y',"YES",'']:
				configPath = discoveredYamlFiles[0]
			else:
				print("exiting...")
				sys.exit()
	return configPath


def parse_input():
	args = sys.argv
	#initializing Sys Variables
	configPath = None
	configs = None
	loggingLevel = logging.INFO
	logLevelDict = {"d":logging.DEBUG,"debug":logging.DEBUG,
					"i":logging.INFO,"info":logging.INFO,
					"w":logging.WARNING,"warning":logging.WARNING,
					"e":logging.ERROR, "error":logging.ERROR,
					"c":logging.CRITICAL,"critical":logging.CRITICAL}
	if len(args) == 1:
		configPath = get_config_path("")
		configs = load_config(configPath)

	if len(args) == 2:
		configInput = args[1]
		configPath = get_config_path( configInput )
		configs = load_config(configPath)

	if len(args) > 2:
		configInput = args[1]
		loggingInput = args[2].replace('-','').lower()

		configPath = get_config_path( configInput )
		configs = load_config(configPath)
		
		if loggingInput in logLevelDict:
			loggingLevel = logLevelDict[loggingInput]
		elif loggingInput.isdigit():
			if int(loggingInput) in range(0,logging.CRITICAL):
				loggingLevel = loggingInput
		else:
			print("logging input not interpretable")

	return configs

if __name__ == "__main__":
	path = get_config_path("./config.yaml")
	print(load_config(path))

