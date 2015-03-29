class RuleElement:
	
	def __init__( self, name ):
		self.name = name
	
	def getType( self ):
		pass
	
	def __eq__( self, other ):
		return ( self.name == other.name )
		
class Operator( RuleElement ):
	
	# The Operator constructor
	def __init__( self, operator ):
		# This is the set of all allowed operators
		self.operators = [ 'AND', 'OR', 'NOT', 'EQUALTO', 'NOTEQUALTO', 'LESSTHAN', 'GREATERTHAN', 'LESSTHANOREQUALTO', 'GREATERTHANOREQUALTO' ]
		# If operator is not in the set then raise an exception
		if operator in self.operators:
			RuleElement.__init__( self, operator )
		else:
			raise 'Syntax error: ' + operator + ' is not a valid operator'

	def __str__( self ):
		return self.name
		
	def getType( self ):
		return 'Operator'
		
class Proposition( RuleElement ):

	def __init__( self, name, value ):
		self.value = value
		RuleElement.__init__( self, name )
		
	def __str__( self ):
		if self.value == True:
			truth = 'true'
		else:
			truth = 'false'
		return 'Proposition statement = ' + self.name + ', value = ' + truth
	
	def getType( self ):
		return 'Proposition'
	
	# I have had to capitalize the methods And(), Or(), Xor() and Not()
	# because "and", "or" and "not" are Python keywords
	def And( self, proposition ):
		resultName = '( ' + self.name + ' AND ' + proposition.name + ' )'
		resultValue = self.value and proposition.value
		return Proposition(resultName, resultValue);	
		
	def Or( self, proposition ):
		resultName = '( ' + self.name + ' OR ' + proposition.name + ' )'
		resultValue = self.value or proposition.value
		return Proposition(resultName, resultValue);				
		
	def Not( self ):
		resultName = '( NOT ' + self.name + ' )'
		resultValue = not self.value
		return Proposition( resultName, resultValue );	

	def Xor( self, proposition ):
		resultName = '( ' + self.name + ' XOR ' + proposition.name + ' )'
		if ( self.value == proposition.value ):
			return Proposition( resultName, 0 )
		else:
			return Proposition( resultName, 1 )
		
	def __eq__( self, other ):
		return ( self.value == other.value ) & ( self.name == other.name )
		
class Variable( RuleElement ):
	
	def __init__( self, name, value ):
		self.value = value
		RuleElement.__init__( self, name )
		
	def __str__( self ):
		return 'Variable name = ' + self.name + ', value = ' + str( self.value )

	def equalTo( self, variable ):
		statement = '( ' + self.name + ' == ' + variable.name + ' )'
		truthValue = ( self.value == variable.value )
		return Proposition(statement, truthValue)

	def notEqualTo( self, variable ):
		statement = '( ' + self.name + ' != ' + variable.name + ' )'
		truthValue = ( self.value != variable.value )
		return Proposition(statement, truthValue)
		
	def lessThan( self, variable ):
		statement = '( ' + self.name + ' < ' + variable.name + ' )'
		truthValue = ( self.value < variable.value )
		return Proposition(statement, truthValue)
		
	def greaterThan( self, variable ):
		statement = '( ' + self.name + ' > ' + variable.name + ' )'
		truthValue = ( self.value > variable.value )
		return Proposition(statement, truthValue)
		
	def greaterThanOrEqualTo( self, variable ):
		statement = '( ' + self.name + ' >= ' + variable.name + ' )'
		truthValue = ( self.value >= variable.value )
		return Proposition(statement, truthValue)

	def lessThanOrEqualTo( self, variable ):
		statement = '( ' + self.name + ' <= ' + variable.name + ' )'
		truthValue = ( self.value <= variable.value )
		return Proposition(statement, truthValue)
		
	def getType( self, ):
		return 'Variable'

from time import *
from calendar import *

class DateVariable( Variable ):

	def __init__( self, name, value ):
		# Date string format is YYYY:MM:DD:HH:MM
		# Convert the date string to a Unix timestamp
		# using the function timegm(). This takes 9 parameters
		# year, month, day, hour, minute, seconds, weekday, Julian day, daylight savings flag
		dateElements = value.split( ':' )
		i = 0
		for e in dateElements:
			dateElements[i] = int(e)
			i = i + 1
		dateElements.append( 0 ) # seconds
		dateElements.append( 0 ) # weekday
		dateElements.append( 0 ) # Julian day
		dateElements.append( 0 ) # daylight savings flag
		# Convert the 9 parameters to a UNIX timestamp
		# This is an integer value that is the number of seconds since the start of 1970
		tempValue = timegm( dateElements )
		Variable.__init__( self, name, tempValue )
		
	def __str__( self ):
		# gmtime() converts a UNIX timestamp back to the 9 parameters
		# needed by timegm()
		dateElements = gmtime( self.value )
		dateString = dateElements[0] + ':' + dateElements[1] + ':' + dateElements[2] + ':' + dateElements[3] + ':' + dateElements[4]
		return 'DateVariable name = ' + self.name + ', value = ' + dateString

	def getType( self, ):
		return 'DateVariable'

