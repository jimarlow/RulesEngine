from RuleElements import *
from RuleContext import *

# This code is purposfully not very "pythonic" because I am using
# Python almost like pseudo code to present a simple version of the Rules 
# Engine that is easy to convert to other languages.

class Rule:
	
	# The Rule constructor
	def __init__( self, name ):
		self.name = name
		self.elements = []
	
	def addProposition( self, name, value = 0 ):
		self.elements.append( Proposition( name, value ) )
	
	def addVariable( self, name, value = 0.0 ):
		self.elements.append( Variable( name, value ) )

	def addDateVariable( self, name, value = 1035219600 ):
		self.elements.append( DateVariable( name, value ) )
		
	def addOperator( self, operator ):
		self.elements.append( Operator( operator ) )
		
	def evaluate( self, context ):
		# The context contains Propositions and Variables that have
		# specific values. To apply the context, simply copy these values
		# into the corresponding Propositions and Variables in the Rule
		for e in self.elements:
			if ( e.getType() == 'Proposition' ) or ( e.getType() == 'Variable' ):
				element = context.findElement( e.name )
				if element != None:
					e.value = element.value
				else:
					e.value = None		
		return self.process()
		
	def process( self ):
		# The stack is used to hold Propositions and Variables
		stack = []
		for e in self.elements:
			if e.getType() == 'Operator':
				self.processOperator( e, stack )
			elif e.getType() == 'Proposition':
				self.processProposition( e, stack )
			elif e.getType() == 'Variable':
				self.processVariable( e, stack )
			else:
				# This is a syntax error
				print 'Syntax error ' + e.getType()				
		return stack.pop()
		
	def processOperator( self, operator, stack ):
		if operator.name == 'AND':
			self.processAnd( stack )
		elif operator.name == 'OR':
			self.processOr( stack )
		elif operator.name == 'NOT':
			self.processNot( stack )
		elif operator.name == 'EQUALTO':
			self.processEqualTo( stack )
		elif operator.name == 'EQUALTO':
			self.processNotEqualTo( stack )
		elif operator.name == 'LESSTHAN':
			self.processLessThan( stack )
		elif operator.name == 'GREATERTHAN':
			self.processGreaterThan( stack )
		elif operator.name == 'LESSTHANOREQUALTO':
			self.processLessThanOrEqualTo( stack )
		elif operator.name == 'GREATERTHANOREQUALTO':
			self.processGreaterThanOrEqualTo( stack )		

	def processProposition( self, proposition, stack ):
		stack.append( proposition )
		
	def processVariable( self, variable,  stack ):
		stack.append( variable )
		
	def processAnd( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.And( lhs ) )
		
	def processOr( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.Or( lhs ) )

	def processXor( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.Xor( lhs ) )
		
	def processNot( self, stack ):
		rhs = stack.pop()
		stack.append( rhs.Not() )
		
	def processEqualTo( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.equalTo( lhs ) )

	def processNotEqualTo( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.notEqualTo( lhs ) )

	def processLessThan( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.lessThan( lhs ) )

	def processGreaterThan( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.greaterThan( lhs ) )

	def processLessThanOrEqualTo( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.lessThanOrEqualTo( lhs ) )

	def processGreaterThanOrEqualTo( self, stack ):
		rhs = stack.pop()
		lhs = stack.pop()
		stack.append( rhs.greaterThanOrEqualTo( lhs ) )
		
	def __str__( self ):
		resultString = self.name + '\n'
		for e in self.elements:
			resultString = resultString + str(e) + '\n'
		return resultString
		
