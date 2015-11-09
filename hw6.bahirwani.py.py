#!/usr/bin/env python

"""
Python class example.

"""

# Step 1
# Create an Element class for rendering an html element.
# It should have class attributes for the tag name ("html" first) and the indentation (spaces to indent for pretty printing)
# The constructor signature should look like
# Element(content=None)
# where content is a string
# It should have an append method that can add another string to the content.
# It should have a render(file_out, ind = "") method that renders the tag and the strings in the content.
# file_out could be any file-like object ( i.e. have a write() method ).
# ind is a string with the indentation level in it: the amount that the tag should be indented for pretty printing.
# (Note ind will be the amount that this element should be indented already. It will be from zero [an empty string] to a lot of spaces, depending on how deep it is in the tree.)
# The amount of indentation should be set by the class attribute indent
# You should now be able to render an html tag with text in it as content.



# The start of it all:
# Fill it all in here.
class Element(object):
	tag = u"html"
	indent = u"    "
	attributes=u""
	def __init__(self, content = None, **kwargs):
		if not content:
			self.children = []
		else:
			self.children = [content]
			
		for key, value in kwargs.iteritems():
			self.attributes+=u' %s="%s"' % (key, value)
			
	def append(self, element):
		self.children.append(element)
		
	def render(self, file_out, ind=u""):
		file_out.write(unicode(ind))
		# listOfAttributes=""
		# for attribute in kwargs:
			# listOfAttributes+=attribute + ""
		if self.attributes == "":
			file_out.write(unicode("<%s>"%self.tag))
		else:
			file_out.write(unicode("<%s%s>"%(self.tag,self.attributes)))
		file_out.write(unicode("\n"))
		
		# for item in self.children:
			# item.render(file_out, ind+self.indent)
			# file_out.write(unicode(ind + self.indent))
			# file_out.write(unicode(item))
			# file_out.write(unicode("\n"))
			# #file_out.write()
			
		for child in self.children:
			try:
				child.render(file_out, ind+self.indent) # everytime it calls itself recursively, adds indent of whatever child we're passing into it and the indent gets bigger
			except AttributeError: # if you pass in something it's not expecting. 
				#file_out.write(u"\n")
				file_out.write(ind + self.indent)
				file_out.write(unicode(child))
				file_out.write(u"\n")
		
		
		file_out.write(ind)
		file_out.write(u"</%s>"%self.tag)
		file_out.write(u"\n")
		
		# file_out.write(unicode(ind))
		# file_out.write(unicode("</%s>"%self.tagname))
		# file_out.write(unicode("\n"))
		
class Html(Element):
	tag = u"html"
	def render(self, file_out, ind=u""):
		file_out.write(u"<!DOCTYPE html>")
		file_out.write(u"\n")
		super(Html, self).render(file_out, ind=u"");

class Body(Element):
	tag = u"body"

class P(Element):
	tag = u"p"
	
class Head(Element):
	tag = u"head"

class OneLineTag(Element):
	def render(self, file_out, ind=u""):
		file_out.write(unicode(ind))
		file_out.write(unicode("<%s>"%self.tag))
		for child in self.children:
			file_out.write(unicode(child))	
		
		#file_out.write(ind)
		file_out.write(u"</%s>"%self.tag)
		file_out.write(u"\n")
		
class Title(OneLineTag):
	tag = u"title"
	
class SelfClosingTag(Element):	
	def __init__(self, content=None, **kwargs):
		super(SelfClosingTag, self).__init__(content=None,**kwargs)
	def render(self, file_out, ind=u""):
		file_out.write(unicode(ind))
		if self.attributes == "":
			file_out.write(unicode("<%s"%self.tag))
		else:
			file_out.write(unicode("<%s%s"%(self.tag,self.attributes)))
		file_out.write(u" />")
		file_out.write(u"\n")
		
class Hr(SelfClosingTag):
	tag = u"hr"
class Br(SelfClosingTag):
	tag = u"br"
	
class A(Element):
	tag = u"a"
	def __init__(self, link, content):
		if not content:
			self.children = []
		else:
			self.children = [content]
			
		# for key, value in kwargs.iteritems():
			# self.attributes+=u'"%s = %s"' % (key, value)
		self.attributes=' href="'+link+ '"'
	def render(self, file_out, ind=u""):
		file_out.write(unicode(ind))
		file_out.write(unicode("<%s%s>"%(self.tag,self.attributes)))
		file_out.write(unicode(self.children[0]))
		file_out.write(unicode("</%s>"%self.tag))
		file_out.write(u"\n")	
	

class Ul(Element):
	tag = u"ul"
class Li(Element):
	tag = u"li"
class H(OneLineTag):
	def __init__(self, headerLevel, headerText):
		self.tag= u"h"+u""+str(headerLevel)
		if not headerText:
			self.children = []
		else:
			self.children = [headerText]
			
class Meta(SelfClosingTag):
	tag = u"meta"
	
	def __init__(self, content=None,**kwargs):
		super(Meta, self).__init__(content=None,**kwargs)
		# if not attributes:
			# self.attributes = ""
		# else:
			# self.attributes = attributes