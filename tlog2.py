#!/usr/bin/python
import os
import yaml
import logging
import logging.config
import cloghandler
#from cloghandler import ConcurrentRotatingFileHandler

def setup_logging(
	default_path = 'logging.yaml',
	default_level= logging.INFO,
	env_key = 'LOG_CFG'
):
	'''Setup logging config from file: logging.yaml
	 
	You can set the config file(logging.yaml)'s path to the env:LOG_CFG
	by export LOG_CG=/xx/xx/xx/xx/logging.yaml in /etc/profile
	'''
	path = default_path
	value = os.getenv(env_key, None)
	if value:
		path = value
	if os.path.exists(path):
		with open(path, 'rt') as f:
			config = yaml.load(f.read())
		logging.config.dictConfig(config)
	else:
		purepath = os.getcwd()
		purename = "default_algopox.log"
		filepath = os.path.join(purepath, purename)
		logging.basicConfig(filename = filepath,
			level = logging.INFO,filemode = 'a',format='%(asctime)s-%(levelname)s:%(message)s')


def test():
	setup_logging()
	logger = logging.getLogger(__name__)
	import time
	for i in range(0,10):
		time.sleep(1)
		logger.warning("This is a warring message for using config file %d",i)

test()








