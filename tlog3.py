#!/usr/bin/python
import logging
import os
from cloghandler import ConcurrentRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s-|%(funcName)s|%(lineno)d|- %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("hello world")

def funclog():
	logger.warning("This is a warning message")





funclog()
