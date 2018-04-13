#!/usr/bin/python

# @Author: Lutz Reiter [http://www.lu-re.de]
# @Date:   2018-04-13T11:30:50+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-13T14:46:21+02:00

from __future__ import with_statement
import time
import logging
import sys
import pygame

from config import *
from ui.PiScreen import PiScreen

audioThread = None
ui = None

# Debug options
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init():
	global ui
	ui = PiScreen(fps = 30)

def loop():
	global ui
	ui.loop()

def stop():
	global ui
	if (ui):
		ui.stop()
### start main loop
init()
try:
   while True:
	  loop()
except KeyboardInterrupt:
   print("# program loop interrupted")
finally:
   stop()
