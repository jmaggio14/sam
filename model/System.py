import yaml


def load_config(filename = "config.yaml"):
	configFile = open(filename)
	configs = yaml.safe_load(configFile)
	return configs
