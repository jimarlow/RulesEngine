from RuleElements import *
#from Proposition import *
#from Variable import *
#from DateVariable import *
#from Operator import *

class RuleContext:
	
	# the constructor
	def __init__( self, name ):
		self.name = name
		# elements is a dictionary - a set of {name, value} pairs
		# The names are Proposition or Variable names and
		# the values are the Propositions or Variables themselves
		self.elements = {}
	
	def addProposition( self, statement, value ):
		self.elements[ statement ] = Proposition( statement, value )
	
	def addVariable( self, name, value ):
		self.elements[ name ] = Variable( name, value )

	def addDateVariable( self, name, value ):
		self.elements[ name ] = DateVariable( name, value )
		
	# Returns a Proposition or Variable or None
	def findElement( self, name ):
		return self.elements.get( name )
		
	# Appends another RuleContext to this one	
	def append( self, context ):
		for e in context.elements.values():
			self.elements[ e.name ] = e
	
	# converts to a String	
	def __str__( self ):
		resultString = ''
		for e in self.elements.values():
			resultString = resultString + str( e ) + '\n'
		return resultString
