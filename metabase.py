from pyhop import *
from metacase import *

class AdaptationBase():

	#################################################################
	# The usual initializer.
	###
	def __init__(self, metaCaseList):
		self.adaptationBase = [adaptation for adaptation in metaCaseList]

	#################################################################
	# Function to return the recipe most similar to 'someRecipe'
	# in the recipe base.
	###
	def getSimilarRecipe(self, someRecipe):
		index = 0;
		runningDifference = self.difference(someRecipe, self.base[0])

		for i in range(len(self.base)):
			thisDifference = self.difference(someRecipe, self.base[i])

			if thisDifference < runningDifference:
				runningDifference = thisDifference
				index = i

		return self.base[index]

	#################################################################
	# Function to determine the difference between two recipes
	# in the recipe base.
	# 
	# For now, we do the naiive thing:  Take the difference between
	# the two recipes' initial states.  Then take the difference between
	# their final states.  Then sum this total difference.
	###
	def difference(self, recipe1, recipe2):
		diffInit = self.stateDifference(recipe1.initial_state, recipe2.initial_state)
		diffGoal = self.stateDifference(recipe1.goal_state, recipe2.goal_state)

		return diffInit + diffGoal

	#################################################################
	# Function to determine the difference between two states,
	# each represented as a 'dict'.
	# 
	###
	def stateDifference(self, state1, state2):
		state1Keys = state1.keys()
		state2Keys = state2.keys()

		# We perform a sanity check: Make sure that the two states
		# have exactly the same names for keys.
		if state1Keys != state2Keys:
			print("stateDifference: STATE1 AND STATE2 HAVE DIFFERENT KEYS")

		totalDifference = 0

		for (key1, val1), (key2, val2) in zip(state1.items(), state2.items()):

			# If this is in fact the same key, we compare values.
			if key1 == key2:
				# If the values are 'list' (or other iterable), then
				# the difference between the two is the number of items
				# that they do not share in common.
				# 
				# Note: This works great for list of 'str' differences, but *terribly*
				# when we are checking differences of, say, lists of bools.
				if isinstance(val1, collections.Iterable):
					totalDifference += len(set(val1).__xor__(set(val2)))
					#for i in range(len(val1)):
					#	totalDifference += abs(val2[i] - val1[i])
					
				# Otherwise, we just take the difference between the values.
				else:
					totalDifference += abs(val2 - val1)

		return totalDifference

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		string = ""

		string += "Recipe Base:\n"

		for recipe in self.base:
			string += str(recipe) + "\n\n"

		return string


	

