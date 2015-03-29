from RuleElements import *
#from Proposition import *
#from Variable import *
#from DateVariable import *
#from Operator import *

class RuleSet:
	
	def __init__( self, name ):
		self.name = name
		self.rules = []
		self.ruleOverrides = []
	
	def addRule( self, rule ):
		self.rules.append( rule )
	
	def addRuleOverride( self, ruleOverride ):
		self.ruleOverride.append( ruleOverride )

	def evaluate( self, context ):
		# Each Rule in the RuleSet is evaluated, and the 
		# results ANDed together taking account of any RuleOverrides	
		resultsForRules = {}
		# Accumulate the results of evaluating the Rules
		for r in self.rules:
			result = r.evaluate( context )
			resultsForRules[ r.name ] = result
		# Apply the RuleOverrides
		for ro in self.ruleOverrides:
			result = resultsForRules[ ro.ruleName ]
			if result != None:
				result.value = ruleOverride.value
		# Work out the final result
		finalResult = 1
		for res in resultsForRules.values():
			finalResult = finalResult and res.value
		return Proposition( self.name, finalResult )
				
		
				

