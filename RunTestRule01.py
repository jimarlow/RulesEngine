from Rule import *
from RuleContext import *
from RuleLoader import *
from RuleSet import *

def runTestRule01():
	# Set the path to the right directory
	path = 'G:/PythonRules/RulesLatest002/'
	ruleFileName = path + 'testrule01.rul'
	ruleContext = path + 'testrule01.con'
	
	# Create a RuleLoader	
	loader = RuleLoader()

	# Load the Rule and the RuleContext
	rule = loader.loadRule( ruleFileName )
	ruleContext = loader.loadRuleContext( ruleContext  )
		
	# Evaluate the Rule		
	result = rule.evaluate( ruleContext )
	
	# Print the results
	print 'The Rule...'
	print rule
	print '\nThe Result...'
	print result
	
if __name__ == '__main__':
	runTestRule01()
	
