# @Author: Lutz Reiter [http://www.lu-re.de] <lutz>
# @Date:   2018-04-13T13:39:13+02:00
# @Project: Brain String
# @Last modified by:   lutz
# @Last modified time: 2018-04-14T19:49:34+02:00
import pyglet

from config import *

class Rectangle(object):
	'''Draws a rectangle into a batch.'''
	def __init__(self, x1, y1, x2, y2, batch, color, filled=True):

		self.vertex_list = batch.add(4, pyglet.gl.GL_QUADS if filled else pyglet.gl.GL_LINE_LOOP, None,
			('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
			('c4B', color * 4)
		)

class UiWidget(pyglet.graphics.Batch):

	def __init__(self, position, size=None):
		pyglet.graphics.Batch.__init__(self)
		self.position = position
		self.size = size

	def disable(self,disabled):
		self.disabled = disabled

	def visible(self,visible):
		self.visible = visible

class UiLabel(UiWidget):

	def __init__(self, text, position, align="center"):
		UiWidget.__init__(self, position)

		label = pyglet.text.Label(text,
			font_name=FONT_FAMILY,
			font_size=FONT_SIZE,
			x=position[0],
			y=position[1],
			anchor_x= align,
			anchor_y='center',
			color = TEXT_COLOR,
			batch = self
		)

class UiImage(UiWidget):
	def __init__(self, file, position, size = None):
		UiWidget.__init__(self, position, size)

		image = pyglet.image.load(file)

		self.originalSize = [image.width, image.height]
		self.sprite = pyglet.sprite.Sprite(image, x=position[0], y=position[1], batch=self)

		self.resize()

	def resize(self):
		if self.size == None:
			return

		xRatio = float(self.size[0]) / self.originalSize[0]
		yRatio = float(self.size[1]) / self.originalSize[1]

		xRatio = 1 if xRatio == 0 else xRatio
		yRatio = 1 if yRatio == 0 else yRatio

		self.sprite.scale = min(xRatio,yRatio)



class UiButton(UiWidget):
	def __init__(self, position, size, label = "None"):
		UiWidget.__init__(self, position, size)
