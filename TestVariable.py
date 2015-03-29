from RuleElements import *
import unittest

class TestVariable( unittest.TestCase ):

	def setUp( self ):
		self.v1 = Variable( 'v1', 10.0 )
		self.v2 = Variable( 'v2', 9 )
		self.v3 = Variable( 'v3', 8 )
		self.v4 = Variable( 'v4', 10.1 )
		self.v5 = Variable( 'v5', 10.0 )
		self.true = Proposition( 'true', True )
		self.false = Proposition( 'false', False )

	def testEqualTo( self ):
		assert self.v1.equalTo( self.v5 ).value == True

	def testNotEqualTo( self ):
		assert self.v1.notEqualTo( self.v2 ).value == True

	def testLessThan( self ):
		assert self.v2.lessThan( self.v1 ).value == True
		assert self.v1.lessThan( self.v5 ).value == False

	def testGreaterThan( self ):
		assert self.v1.greaterThan( self.v2 ).value == True
		assert self.v1.greaterThan( self.v5 ).value == False

	def testLessThanOrEqualTo( self ):
		assert self.v2.lessThanOrEqualTo( self.v1 ).value == True
		assert self.v1.lessThanOrEqualTo( self.v5 ).value == True

	def testGreaterThanOrEqualTo( self ):
		assert self.v1.greaterThanOrEqualTo( self.v2 ).value == True
		assert self.v1.greaterThanOrEqualTo( self.v5 ).value == True

	def testGetType( self ):
		assert self.v1.getType() == 'Variable'

if __name__ == "__main__":
	unittest.main()


