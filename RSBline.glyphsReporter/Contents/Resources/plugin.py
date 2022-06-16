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
			'en': 'RSB',
			'de': 'Nachbreite',
			'fr': 'approche droite',
			'es': 'lado derecho',
			})
	
	@objc.python_method
	def conditionsAreMetForDrawing(self):
		"""
		Only activate if text or pan (hand) tool are active.
		"""
		currentController = self.controller.view().window().windowController()
		if currentController:
			tool = currentController.toolDrawDelegate()
			textToolIsActive = tool.isKindOfClass_( NSClassFromString("GlyphsToolText") )
			if textToolIsActive: 
				return True
		return False
	
	@objc.python_method
	def drawLine(self, x1, y1, x2, y2, strokeWidth):
		path = NSBezierPath.bezierPath()
		path.moveToPoint_(NSPoint(x1, y1))
		path.lineToPoint_(NSPoint(x2, y2))
		path.setLineWidth_(strokeWidth)
		# NSColor.separatorColor().colorWithAlphaComponent_(0.4).set()
		NSColor.keyboardFocusIndicatorColor().set()
		path.stroke()

	@objc.python_method
	def drawTriangle(self, x1, y1, x2, y2, x3, y3):
		path = NSBezierPath.bezierPath()
		path.moveToPoint_(NSPoint(x1, y1))
		path.lineToPoint_(NSPoint(x2, y2))
		path.lineToPoint_(NSPoint(x3, y3))
		path.closePath()
		NSColor.systemRedColor().colorWithAlphaComponent_(0.4).set()
		# NSColor.keyboardFocusIndicatorColor().set()
		path.fill()
	
	@objc.python_method
	def italicShift(self, yPos, angle, xHeight):
		'''
		ITALIC OFFSET. TAKEN FROM MARK FROMBERG'S SMART PLUMBLINES
		'''
		offset = tan(radians(angle)) * xHeight/2
		shift = tan(radians(angle)) * yPos - offset
		return shift

	@objc.python_method
	def drawRSB(self, layer):
		angle = layer.italicAngle
		xHeight = layer.master.xHeight
		x1, y1 = layer.width, layer.ascender
		x2, y2 = x1, layer.descender
		
		# draw line:
		strokeWidth = 1.0 * self.getScale() ** -0.9
		self.drawLine( 
			x1 + self.italicShift(y1, angle, xHeight), y1 , 
			x2 + self.italicShift(y2, angle, xHeight), y2, 
			strokeWidth,
			)
		
		# triangle:
		triangleSize = 10.0 / self.getScale()  ** 1
		self.drawTriangle(
			x1/2-triangleSize + self.italicShift(y2, angle, xHeight), y2,
			x1/2 + self.italicShift(y2+triangleSize, angle, xHeight), (y2+triangleSize),
			x1/2+triangleSize + self.italicShift(y2, angle, xHeight), y2,
			)
	
	@objc.python_method
	def background(self, layer):
		if self.conditionsAreMetForDrawing():
			self.drawRSB(layer)

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
