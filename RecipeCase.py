from pyhop import *
import collections

# NOTE: initial_state and goal_state must be STRINGS
#       Similarly, 'states' must consist of strings indexing states!

class RecipeCase():
	
	#################################################################
	# The usual initializer.
	# 
	# initial_state and goal_state are to be specified by dictionaries
	# of 'item name' : 'value' for each 'item' described by the state
	# in our world.
	###
	def __init__(self, name, initial_state,
			goal_state, actions):
		self.initial_state = dict()
		self.goal_state = dict()

		self.name = name
		self.initial_state = initial_state
		self.goal_state = goal_state

		# The plan is a list of actions.  Actions are 'strings' that
		# are Python-executable (of the form "function(param, param, ...)" )
		# The plan may be empty,
		# incomplete, or incorrect.
		self.plan = actions

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		string = ""

		string += "Recipe Name: " + self.name + "\n"
		string += "Initial State: " + str(self.initial_state) + "\n\n"
		string += "Final State: " + str(self.goal_state) + "\n\n"

		string += "Plan: ["
		for action in self.plan:
			string += action + ", "
		string += "]\n\n"

		return string



