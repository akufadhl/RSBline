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
	def foreground(self, layer):
		# layer = Glyphs.font.selectedLayers[0]
		scale = Glyphs.font.currentTab.scale
		x1, y1 = layer.width, layer.ascender
		x2, y2 = x1, layer.descender
		strokeWidth = 0.5 * scale
		
		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1, y1))
		path.lineToPoint_((x2, y2))
		path.setLineWidth_(strokeWidth)
		NSColor.grayColor().set()
		path.stroke()

		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1-25,y1))
		path.lineToPoint_((x1,y1-25))
		path.lineToPoint_((x1+25,y1))
		NSColor.colorWithRed_green_blue_alpha_(0.4, 0.7, 0.9, 0.4).set()
		path.closePath()
		path.fill()

		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1-25,y2))
		path.lineToPoint_((x1,y2+25))
		path.lineToPoint_((x2+25,y2))
		NSColor.colorWithRed_green_blue_alpha_(0.4, 0.7, 0.9, 0.4).set()
		path.closePath()
		path.fill()
	
	@objc.python_method
	def background(self, layer):
		# layer = Glyphs.font.selectedLayers[0]
		scale = Glyphs.font.currentTab.scale
		x1, y1 = layer.width, layer.ascender
		x2, y2 = x1, layer.descender
		strokeWidth = 0.5 / scale
		
		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1, y1))
		path.lineToPoint_((x2, y2))
		path.setLineWidth_(strokeWidth)
		NSColor.grayColor().set()
		path.stroke()

		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1-25,y1))
		path.lineToPoint_((x1,y1-25))
		path.lineToPoint_((x1+25,y1))
		NSColor.colorWithRed_green_blue_alpha_(0.2, 0.1, 0.7, 0.4).set()
		path.closePath()
		path.fill()

		path = NSBezierPath.bezierPath()
		path.moveToPoint_((x1-25,y2))
		path.lineToPoint_((x1,y2+25))
		path.lineToPoint_((x2+25,y2))
		NSColor.colorWithRed_green_blue_alpha_(0.2, 0.1, 0.7, 0.4).set()
		path.closePath()
		path.fill()


	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
