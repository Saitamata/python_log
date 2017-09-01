#!/usr/bin/python
import logging
import os
from cloghandler import ConcurrentRotatingFileHandler

def configlogger():
	purepath = os.getcwd()
	purename = "log.txt"
	filepath = os.path.join(purepath,purename)

	logging.basicConfig(filename = filepath,\
		level = logging.INFO,filemode = 'a',format='%(asctime)s-%(levelname)s:%(message)s')

configlogger()

logging.debug('debug test')
logging.info("info test")
logging.warning("warn test")
logging.error("error test")


