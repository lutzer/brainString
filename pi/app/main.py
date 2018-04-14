#!/usr/bin/python

# @Author: Lutz Reiter [http://www.lu-re.de]
# @Date:   2018-04-13T11:30:50+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-14T18:50:49+02:00

from __future__ import with_statement
import time
import logging
import sys

from config import *
from ui.PiScreen import PiScreen

audioThread = None
ui = None
running = False

# Debug options
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init():
	logger.info("starting program")
	global ui, running
	ui = PiScreen(fps = 30)
	ui.keyPressEvent += onKeyPressEvent
	running = True
	logger.info("program initialized, starting loop")

def loop():
	global ui
	ui.loop()

def stop():
	logger.info("programm stopped")
	global ui
	if (ui):
		ui.stop()

def onKeyPressEvent(symbol):
	global running
	# press esc to quit
	if symbol == 65307:
		running = False

### start main loop
init()
try:
   while running:
	  loop()
except KeyboardInterrupt:
   print("# program loop interrupted")
finally:
   stop()
