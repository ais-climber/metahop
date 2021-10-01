from RecipeCase import *
from actions import *
import json
import re

#####################################################################
# Function to parse a step of the recipe in the file into a
# Python-executable command.
###
def parseStepToCommand(step):
	# Parse this step of the recipe into a string 'function' with list of
	# string 'parameters'.
	function = step.split("(")[0]
	paramsList = (step.split("(")[1]).strip(")").split(", ")

	# Combine the function and its parameters into a string 'command' 
	# that is executable by python.
	command = ""
	command += function + "("
	for param in paramsList:
		command += "'" + param + "'" + ", "
	command += ")"

	# Put the executable command in our 'plan'
	return command

#####################################################################
# Function to parse JSON-structured input file into a Recipe base.
#
#
# File is given by its 'string' name, 'filename'.
###
def parseJSONCaseBase(filename):
	recipeCaseList = []
	recipeGoalList = []

	filestring = open(filename, 'r').read()
	parsed_json = json.loads(filestring)
	
	for recipedict in parsed_json:
		if recipedict["type"] in ["case", "goal"]:
			recipeName = recipedict["name"]
			
			# We assume that the first case listed in
			# our input file is an empty dummy case.
			initialState = parsed_json[0]["result"]
			initialState["unused"] = recipedict["ingredients"]

			initialState["hot"] = set(initialState["hot"])
			initialState["melted"] = set(initialState["melted"])
			initialState["toasted"] = set(initialState["toasted"])
			initialState["fried"] = set(initialState["fried"])

			goalState = recipedict["result"]

			goalState["hot"] = set(goalState["hot"])
			goalState["melted"] = set(goalState["melted"])
			goalState["toasted"] = set(goalState["toasted"])
			goalState["fried"] = set(goalState["fried"])

			plan = []

			for action in recipedict["steps"]:
				function = eval(action.split("(")[0])
				params = action.split("(")[1].rstrip(")").split(", ")

				# The hardcoded string 'state' is ALWAYS the first parameter
				# of any recipe action.  So we prepend it to the params.
				params = ["state"] + params

				plan.append((function, params))

			thisRecipe = RecipeCase(recipeName, initialState, goalState, plan)

			# Append this RecipeCase to either our casebase or our goals,
			# depending on whether this recipe is a 'goal' recipe.
			if recipedict["type"] == "case":
				recipeCaseList.append(thisRecipe)
			elif recipedict["type"] == "goal":
				recipeGoalList.append(thisRecipe)

	return (recipeCaseList, recipeGoalList)

def parseJSONAdaptationBase(filename):
	pass
