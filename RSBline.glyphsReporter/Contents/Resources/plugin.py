# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from AppKit import NSBezierPath, NSColor
from math import tan, radians


class showRSB(ReporterPlugin):


	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Show RSB',
			'de': 'Mein Plugin',
			'fr': 'Ma extension',
			'es': 'Mi plugin',
			'pt': 'Meu plug-in',
			})

	@objc.python_method
	def drawLine(self, x1, y1, x2, y2, strokeWidth,):
		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1, y1))
		path.lineToPoint_((x2, y2))
		path.setLineWidth_(strokeWidth)
		path.stroke()

	@objc.python_method
	def drawTriangle(self, x1, y1, x2, y2, x3, y3, strokeWidth, color):
		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1, y1))
		path.lineToPoint_((x2, y2))
		path.lineToPoint_((x3, y3))
		path.closePath()
		path.setLineWidth_(strokeWidth)
		color.set()
		path.fill()
	
	@objc.python_method
	def italo(self, yPos, angle, xHeight):
		'''
		ITALIC OFFSET
		'''
		offset = tan(radians(angle)) * xHeight/2
		shift = tan(radians(angle)) * yPos - offset
		return shift

	@objc.python_method
	def drawRSB(self, layer):

		angle = layer.master.italicAngle
		xHeight = layer.master.xHeight
		scale = Glyphs.font.currentTab.scale
		x1, y1 = layer.width, layer.ascender
		x2, y2 = x1, layer.descender
		strokeWidth = 1 * scale
		triColor = 	NSColor.colorWithRed_green_blue_alpha_(0.4, 0.7, 0.9, 0.4)
		print(self.italo(x1, angle, xHeight))
		self.drawLine(x1 + self.italo(y1, angle, xHeight), y1 , x2 + + self.italo(y2, angle, xHeight), y2, strokeWidth)
		
		self.drawTriangle((x1-25) + self.italo(y1, angle, xHeight), y1, x1 + self.italo(y1, angle, xHeight), (y1-25), (x1+25)+ self.italo(y1, angle, xHeight), y1, strokeWidth, triColor)
		# self.drawTriangle((x1-25), y2, x1, (y2+25), (x2+25), y2, strokeWidth, triColor)

	# @objc.python_method
	# def foreground(self, layer):

	# 	scale = Glyphs.font.currentTab.scale
	# 	x1, y1 = layer.width, layer.ascender
	# 	x2, y2 = x1, layer.descender
	# 	strokeWidth = 1 * scale
	# 	triColor = 	NSColor.colorWithRed_green_blue_alpha_(0.4, 0.7, 0.9, 0.4)
	# 	angle = layer.master.italicAngle
		
	# 	self.drawLine(x1, self.italo(y1, angle), x2, self.italo(y2, angle), strokeWidth)
		
	# 	self.drawTriangle((x1-25), self.italo(y1, angle), x1, self.italo((y1-25), angle), (x1+25), self.italo(y1, angle), strokeWidth, triColor)
	# 	self.drawTriangle((x1-25), y2, x1, (y2+25), (x2+25), y2, strokeWidth, triColor)
	
	@objc.python_method
	def background(self, layer):
		
		self.drawRSB(layer)


	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
