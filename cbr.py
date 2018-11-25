# The Case Based Reasoner (CBR)
#   for recipe generation
# 
# Author: Caleb Kisby

from recipebase import Recipebase

class CBR():
	
	#################################################################
	# The usual initializer.
	###
	def __init__(self, recipeCaseList):
		# Generate the recipe base from a hardcoded file.
		self.casebase = Recipebase(recipeCaseList)

	#################################################################
	# Function to generate a recipe.
	# 
	# This function takes in an *empty* RecipeCase and generates the
	# actual recipe, i.e. fills in its *plan* from its initial state
	# to its goal state.
	# 
	# NOTE: Currently we do the EXTREMELY NAIIVE THING, which is to
	# just return the most similar recipe.  This is just FOR TESTING
	# PURPOSES ONLY!
	###
	def generateRecipe(self, emptyRecipeCase):
		return self.casebase.getSimilarRecipe(emptyRecipeCase)

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		return str(self.casebase)

