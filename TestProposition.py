from RuleElements import *
import unittest

class TestProposition( unittest.TestCase ):

	def setUp( self ):
		self.p1 = Proposition( 'p1', True )
		self.p2 = Proposition( 'p2', True )
		self.p3 = Proposition( 'p3', False )
		self.p4 = Proposition( 'p4', False )
		
	def testConstructor( self ):
		assert self.p1.name == 'p1'
		assert self.p1.value == True
		
	def testAnd( self ):
		assert self.p1.And( self.p2 ).value ==  True
		assert self.p1.And( self.p3 ).value == False
		
	def testOr( self ):
		assert self.p1.Or( self.p2 ).value ==  True
		assert self.p1.Or( self.p3 ).value == True
		assert self.p3.Or( self.p4 ).value == False

	def testXor( self ):
		assert self.p1.Xor( self.p2 ).value ==  False
		assert self.p1.Xor( self.p3 ).value == True
		assert self.p3.Xor( self.p4 ).value == False

	def testNot( self ):
		assert self.p1.Not().value == False
		assert self.p3.Not().value == True
		
if __name__ == "__main__":
	unittest.main()
	
