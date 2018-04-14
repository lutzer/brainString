# @Author: Lutz Reiter [http://www.lu-re.de] <lutz>
# @Date:   2018-04-13T13:39:13+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-13T17:09:07+02:00
import pyglet

from config import *

class UiWidget(pyglet.graphics.Batch):

	def __init__(self, position, size=[0,0]):
		pyglet.graphics.Batch.__init__(self)
		self.position = position
		self.size = size

	def disable(self,disabled):
		self.disabled = disabled

class UiLabel(UiWidget):

	def __init__(self, text, position):
		UiWidget.__init__(self, position)

		label = pyglet.text.Label(text,
			font_name=FONT_FAMILY,
			font_size=FONT_SIZE,
			x=position[0],
			y=position[1],
			anchor_x='center',
			anchor_y='center',
			batch = self
		)


class UiButton(UiWidget):
	def __init__(self, surface, position, size, label = "None"):
		UiWidget.__init__(self, surface, position, size)

	def draw(self):
		return
