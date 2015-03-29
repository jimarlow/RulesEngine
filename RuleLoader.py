from Rule import *
from RuleContext import *
from RuleElements import *

class RuleLoader:

	# Rule files have the following form:
	#
	# p1 IS true		
	# p2 IS true	
	# AND
	# v1 EQUALS 10.1
	# v2 EQUALS 10.0		
	# LESSTHAN		
	# AND
	#
	# The keyword IS denotes a Proposition
	# The keyword EQUALS denotes a Variable
	# The keyword ON denotes a Date DateVariable
	
	def loadRule( self, fileName ):
		self.rule = Rule( fileName.split('.')[0] )
		ruleFile = open( fileName, 'r' )
		lines = ruleFile.readlines()
		ruleFile.close()
		for line in lines:
			self.tokens = line.split()
			if len( self.tokens ) == 1:
				# This line is an operation
				self.processOperator()
			if len( self.tokens ) == 3:
				# This line is a statement
				self.processStatement()
		return self.rule

	def loadRuleContext( self, fileName ):
		self.rule = RuleContext( fileName.split('.')[0] )
		ruleFile = open( fileName, 'r' )
		lines = ruleFile.readlines()
		ruleFile.close()
		for line in lines:
			self.tokens = line.split()
			# Every statement in the Rule file should have 3 tokens
			# if not - ignore it
			if len( self.tokens ) == 3:
				self.processStatement()
		return self.rule	
		
	def processStatement( self ):
		if self.tokens[1] == 'IS':
			# This is a Proposition
			if self.tokens[2] == 'true':
				self.rule.addProposition( self.tokens[0], 1 )
			else:
				self.rule.addProposition( self.tokens[0], 0 )
		elif self.tokens[1] == 'EQUALS':
			# This is a Variable
			self.rule.addVariable( self.tokens[0], self.tokens[2] )
		elif self.tokens[1] == 'ON':
			# This is a DateVariable
			self.rule.addDateVariable( self.tokens[0], self.tokens[2] )
			
	def processOperator( self ):
		# Process the operator
		self.rule.addOperator( self.tokens[0] )

