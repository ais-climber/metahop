import unittest

from RecipeCase import *
from recipebase import *
from cbr import *
from fileparser import *

class TestSuite(unittest.TestCase):

	#################################################################
	# The usual initializer.
	# 
	# We start by clearing the case base, so that we have dummy
	# values in our case base.
	###
	def __init__(self):
		self.shutDownCaseBase()

	#################################################################
	# Function to initialize the case base by reading
	# from the Test Suite input file.
	###
	def setUpCaseBase(self):
		self.recipeCaseList = []
		self.recipeGoalList = []

		# We read in past recipes and future recipe goals from
		# the Test Suite input file.
		(self.recipeCaseList, self.recipeGoalList) = parseFile("casebase/HandMadeCaseBase.txt")

		# We initialize the CBR reasoner.
		self.cbr = CBR(recipeCaseList)

	#################################################################
	# Function to clear the case base, in case the case base is modified
	# during the course of a test.
	###
	def shutDown(self):
		self.recipeCaseList = []
		self.recipeGoalList = []
		self.cbr = CBR([])
		

#	def testDummyTest(self):
#		self.assertEqual("foo".upper(), "FOO")

unittest.main()


