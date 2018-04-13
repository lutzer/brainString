# @Author: Lutz Reiter [http://www.lu-re.de] <lutz>
# @Date:   2018-04-13T13:08:41+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-13T14:50:54+02:00
import pygame
import time

from config import *

from UiElements import UiButton

class PiScreen(object):

	def __init__(self, fps = 30):
		pygame.init()
		self.screen = pygame.display.set_mode(SCREEN_SIZE)
		self.fps = fps

		self.button = UiButton(self.screen,[10,10],[100,30])
		self.clock = pygame.time.Clock()

	def loop(self):
		pygame.event.get()
		self.screen.fill(BG_COLOR)
		self.button.draw()
		pygame.display.flip()

		# make loop wait
		self.clock.tick(self.fps)

	def stop(self):
		pygame.quit()
