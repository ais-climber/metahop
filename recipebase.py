from pyhop import *
from RecipeCase import *

class Recipebase():

	#################################################################
	# The usual initializer.
	###
	def __init__(self, recipeCaseList):
		self.base = [recipe for recipe in recipeCaseList]

	#################################################################
	# Function to add a new recipe to the recipe base.
	###
	def addRecipe(self, someRecipe):
		self.base.append(someRecipe)

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
	# their final states.  Next take the difference between their plans.
	# Finally, sum this total difference.
	###
	def difference(self, recipe1, recipe2):
		diffInit = self.stateDifference(recipe1.initial_state, recipe2.initial_state)
		diffGoal = self.stateDifference(recipe1.goal_state, recipe2.goal_state)

		diffPlan = self.planDifference(recipe1.plan, recipe2.plan)

		return diffInit + diffGoal + diffPlan

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
	# Function to determine the difference between two plans,
	# each given as a 'list' of tuples (function, params),
	# where:
	# 	'function' is the function to be executed
	#	'params' is the 'list' of 'string' parameters to be fed into
	# 		the function.
	# 
	# We will not focus on the difference between the 'params', since
	# this is largely determined by the difference in ingredients (which
	# is handled by the 'stateDifference' method).
	# 
	# Instead, we *just* focus on the 'function's being used in each
	# plan, and their comparative frequency.  To this end, we make
	# dictionaries {function : frequency} that count the number of
	# occurances of 'function' in each plan.
	# 
	###
	def planDifference(self, plan1, plan2):
		totalDifference = 0
		freqDict1 = {}
		freqDict2 = {}

		allFunctionNames = [plan1[i][0].__name__ for i in range(0, len(plan1))] + [plan2[i][0] for i in range(0, len(plan2))]
		freqDict1 = {f : 0 for f in allFunctionNames}
		freqDict2 = {f : 0 for f in allFunctionNames}

		# Populate the frequency dictionaries.
		for f in allFunctionNames:
			# Count the number of occurences of 'f' in 'plan1'
			for pair in plan1:
				if pair[0].__name__ == f:
					freqDict1[f] += 1

			# Count the number of occurences of 'f' in 'plan2'
			for pair in plan2:
				if pair[0].__name__ == f:
					freqDict2[f] += 1

		# Now we get the difference between the frequency dictionaries.
		for f in allFunctionNames:
			totalDifference = abs(freqDict1[f] - freqDict2[f])

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


	
