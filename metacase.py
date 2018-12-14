
from pyhop import *
import collections

# NOTE: initial_state and goal_state must be STRINGS
#       Similarly, 'states' must consist of strings indexing states!

class MetaCase():
	
	#################################################################
	# The usual initializer.
	# 
	# initial_recipe and goal_recipe are the initial and final
	# 'RecipeCase' recipes, and 'metaplan' is the sequence of
	# plan operations that transforms the init_recipe into the
	# final_recipe.
	###
	def __init__(self, name, initial_recipe,
			goal_recipe, metaactions):
		self.initial_recipe = []
		self.goal_recipe = []

		self.name = name
		self.initial_recipe = initial_recipe
		self.goal_recipe = goal_recipe

		# The metaplan is a list of meta-actions.  Meta-actions,
		# like base actions, are 'strings' that are Python-executable 
		# (of the form "function(param, param, ...)" )
		# but operate on a 'recipe' rather than a 'state'.
		# The plan may be empty, incomplete, or incorrect.
		self.metaplan = metaactions

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		string = ""

		string += "Recipe Name: " + self.name + "\n"
		string += "Initial State: " + str(self.initial_recipe) + "\n\n"
		string += "Final State: " + str(self.goal_recipe) + "\n\n"

		string += "Plan: ["
		for metaaction in self.metaplan:
			string += metaaction + ", "
		string += "]\n\n"

		return string




