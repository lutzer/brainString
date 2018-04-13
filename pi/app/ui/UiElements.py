# @Author: Lutz Reiter [http://www.lu-re.de] <lutz>
# @Date:   2018-04-13T13:39:13+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-13T14:05:00+02:00
import pygame

from config import *

class UiWIdget(object):

	def __init__(self, surface, position, size):
		self.surface = surface
		self.position = position
		self.size = size

	def update(self):
		return;

	def draw(self, surface):
		return;

	def disable(self,disabled):
		self.disabled = disabled

class UiButton(UiWIdget):
	def __init__(self, surface, position, size, label = "None"):
		UiWIdget.__init__(self, surface, position, size)

	def draw(self):
		 pygame.draw.rect(self.surface, BUTTON_COLOR, self.position + self.size)
