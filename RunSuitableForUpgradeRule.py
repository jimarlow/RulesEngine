from Rule import *
from RuleContext import *
from RuleLoader import *
from RuleSet import *

def runSuitableForUpgradeRule():
	
	# Set the path to the right directory
	path = 'C:/Documents and Settings/v128477/Desktop/RulesLatest002/'
	ruleFileName = path + 'SuitableForUpgrade.rul'
	ruleContextFileName = path + 'SuitableForUpgrade.con'

	# Create a RuleLoader	
	loader = RuleLoader()

	# Load the Rule and the RuleContext
	rule = loader.loadRule( ruleFileName  )
	ruleContext = loader.loadRuleContext( ruleContextFileName  )

	# Evaluate the Rule		
	result = rule.evaluate( ruleContext )

	# Print the results
	print 'The Rule...'
	print rule
	print '\nThe Result...'
	print result
	
if __name__ == '__main__':
	runSuitableForUpgradeRule()	
