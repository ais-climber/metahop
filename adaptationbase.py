from pyhop import *
from adaptationcase import *
import recipebase

class AdaptationBase():

	#################################################################
	# The usual initializer.
	###
	def __init__(self, adaptationCaseList):
		self.base = [adaptation for adaptation in adaptationCaseList]

	#################################################################
	# Function to add a new adaptation to the adaptation base.
	###
	def addAdaptation(self, someAdaptation):
		self.base.append(someAdaptation)

	#################################################################
	# Function to return the adaptation most similar to 'someAdaptation'
	# in the adaptation base.
	###
	def getSimilarAdaptation(self, someAdaptation):
		index = 0;
		runningDifference = self.difference(someAdaptation, self.base[0])

		for i in range(len(self.base)):
			thisDifference = self.difference(someAdaptation, self.base[i])

			if thisDifference < runningDifference:
				runningDifference = thisDifference
				index = i

		return self.base[index]

	#################################################################
	# Function to determine the difference between two adaptations
	# in the adaptation base.
	# 
	# For now, we do the naiive thing:  Take the difference between
	# the two adaptations' initial recipes.  Then take the difference between
	# their final recipes.  Then sum this total difference.
	###
	def difference(self, adapt1, adapt2):
		diffInit = recipebase.difference(adapt1.initial_recipe, adapt2.initial_recipe)
		diffGoal = recipebase.difference(adapt1.goal_recipe, adapt2.goal_recipe)

		return diffInit + diffGoal

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		string = ""

		string += "Recipe Base:\n"

		for adaptation in self.base:
			string += str(adaptation) + "\n\n"

		return string


	

