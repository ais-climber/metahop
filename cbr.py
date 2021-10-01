# The Case Based Reasoner (CBR)
#   for recipe generation
# 
# Author: Caleb Kisby

from recipebase import Recipebase
from adaptationcase import AdaptationCase
from metaactions import *
from metacbr import MetaCBR

class CBR():
	
	#################################################################
	# The usual initializer.
	###
	def __init__(self, recipeCaseList, adaptationCaseList):
		# Generate the recipe base from a hardcoded file.
		self.casebase = Recipebase(recipeCaseList)

		# TODOTODOTODOTODOTODO:
		# 	We should NOT have a single 'adaptationCase' for our
		# 	CBReasoner that we change each time.  Instead, our
		#	'generateRecipe' method should use the MetaCBR to
		# 	RETRIEVE the most relevant case adaptation for our
		# 	particular recipes, and apply *that*.
		#
		#	So MetaCBR will refer to its base, and the base will
		# 	refer to its Meta.
		#
		#	Auroboris-Borialis
		self.metacbr = MetaCBR(adaptationCaseList)


	#################################################################
	# Function to generate a recipe.
	# 
	# This function takes in an *empty* RecipeCase and generates the
	# actual recipe, i.e. fills in its *plan* from its initial state
	# to its goal state.
	# 
	# First, we use the metacbr to generate an 'adaptationCase' that
	# is relevant and applicable to the 'emptyRecipeCase' at hand.
	# (The metacbr retrieves the most relevant adaptations, and adapts
	# them (including substitution) in order to generate this adaptation.)
	# 
	# We then follow the steps of the resulting 'adaptationCase' by executing
	# them in order.
	# 
	###
	def generateRecipe(self, emptyRecipeCase):
		#return self.casebase.getSimilarRecipe(emptyRecipeCase)

		# TODO: Right now we just do an extremely naiive application of the 
		# 'adaptationCase' to our 'emptyRecipeCase'.  We currently DO NOT
		# do any substitution of any sort, which may result in weird or
		# incorrect adaptations (like spreading butter on a peanut butter
		# and jelly sandwich).
		precondTestString = ""
		applicationString = ""

		for (function, params) in self.adaptationCase.metaplan:
			# 'metaaction' is formatted as (function, [params])
			# Our 'metastate' is 'emptyRecipeCase'
			precondTestString = "meta_preconditions_met" + "(emptyRecipeCase, "
			applicationString = function.__name__ + "(emptyRecipeCase, "
			for param in params:
				precondTestString += param + ", "
				applicationString += param + ", "
			applicationString += ")"
			
			# We have to define a 'namespace' for our exec() function
			# so that our 'emptyRecipeCase' is actually mutated.
			namespace = {"emptyRecipeCase" : emptyRecipeCase}

			# Next, we actually execute the action string, so long as the
			# preconditions are met.
			if (exec(precondTestString)):
				exec(applicationString, namespace)
			else:
				# Preconditions were not met for this action, so this
				# adpatation case is not valid for the given initial
				# recipe.  Abort.
				print("generateRecipe: Preconditions for " + function.__name__
					+ " not met.  Abort.")

			# We have to update 'emptyRecipeCase' to reflect changes
			# done to the namespace.
			emptyRecipeCase = namespace["emptyRecipeCase"]


		# TODO: The resulting recipe will very often *not be correct*.
		# 	We can account for that by using PYHOP (at this point) to
		# 	bridge the gap from our final state to the goal state.  We
		# 	then store the resulting recipe *with PYHOP changes*, and
		# 	evaluate the efficiency/accuracy of *that*.

		return emptyRecipeCase

	#################################################################
	# Function to store a recipe in the case base.
	# 
	# This function takes in a *complete* RecipeCase and stores it
	# in the case base.
	###
	def storeRecipe(self, completeRecipeCase):
		self.casebase.addRecipe(completeRecipeCase)

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		return str(self.casebase)

