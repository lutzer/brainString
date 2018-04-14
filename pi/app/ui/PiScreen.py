# @Author: Lutz Reiter [http://www.lu-re.de] <lutz>
# @Date:   2018-04-13T13:08:41+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-13T17:08:40+02:00
import pyglet
import time

from config import *


from utils.eventHandler import EventHandler
from utils.pygletHelpers import convertColor
from UiElements import UiLabel

class PiScreen(object):

	keyPressEvent = EventHandler()

	def __init__(self, fps = 30):
		self.window = pyglet.window.Window(
		 	width = SCREEN_SIZE[0],
			height = SCREEN_SIZE[1],
			fullscreen = RUN_IN_FULLSCREEN
		)
		pyglet.clock.set_fps_limit(fps)

		self.width = SCREEN_SIZE[0]
		self.height = SCREEN_SIZE[1]

		#setup ui elements
		self.title = UiLabel("Rattus norvegicus forma domestica", [self.width/2, self.height/2])

		# setup window events
		@self.window.event
		def on_key_press(symbol, modifiers):
			self.keyPressEvent.emit(symbol)

		@self.window.event
		def on_mouse_motion(x, y, dx, dy):
			return;

		#self.button = UiButton(self.screen,[10,10],[100,30])

	def draw(self):
		pyglet.gl.glClearColor(*convertColor(BG_COLOR))
		self.window.clear()

		self.title.draw()

	def loop(self):
		# redraw frame
		self.draw()

		# tell piglet to redraw window
		self.window.switch_to()
		self.window.dispatch_events()
		self.window.dispatch_event('on_draw')
		self.window.flip()

		# wait to set fps
		pyglet.clock.tick()

	def stop(self):
		self.window.close()
