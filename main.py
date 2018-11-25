
from cbr import *
from RecipeCase import *

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
# Function to parse structured input file into a RecipeCase.
# 
# File is given by its 'string' name, 'filename'
###
def parseFile(filename):
	recipeCaseList = []
	recipeGoalList = []

	# Initialize hardcoded input file.
	inputstream = open(filename)

	# We read the case base and goal file line by line.
	thisLine = inputstream.readline().strip()
	thisRecipe = RecipeCase("dummy", None, None, [])
	
	# We read each recipe until we reach the end of the file.
	while thisLine:

		# We skip commented lines before the recipe.
		if thisLine[0] == "#":
			thisLine = inputstream.readline().strip()
			continue
		elif thisLine == "":
			thisLine = inputstream.readline().strip()
			continue
		elif thisLine == "RECIPE BEGIN" or "GOAL BEGIN":
			# First we keep in memory whether this recipe
			# is a goal or casebase recipe.
			isGoal = False
			if thisLine == "GOAL BEGIN":
				isGoal = True

			# We then initialize RecipeCase variables.
			recipeName = ""
			initialState = {
				"Name" : "",
				"Unused" : [],
				"Stack" : [],
				"Spread2" : "",
				"Spread1" : "",
				"Hot" : [],
				"Melted" : [],
				"Toasted" : [],
				"Fried" : [],
				"Sliced" : []
			}
			goalState = {
				"Name" : "",
				"Unused" : [],
				"Stack" : [],
				"Spread2" : "",
				"Spread1" : "",
				"Hot" : [],
				"Melted" : [],
				"Toasted" : [],
				"Fried" : [],
				"Sliced" : []
			}
			plan = []

			# We read the recipe in full, requiring it to
			# be specified according to a certain format.
			thisLine = inputstream.readline().strip()
			while thisLine != "END":
				# We skip commented lines within the recipe.
				if thisLine[0] == "#":
					thisLine = inputstream.readline().strip()
					continue
				elif thisLine == "":
					thisLine = inputstream.readline().strip()
					continue
				elif thisLine == "NAME":
					# We get the recipe's name on the next line.
					thisLine = inputstream.readline().strip()
					recipeName = thisLine
					initialState["Name"] = thisLine
					goalState["Name"] = thisLine

					# Move along
					thisLine = inputstream.readline().strip()
					continue

				elif thisLine == "INGREDIENTS":
					# We update our state to incorporate the
					# ingredients of the recipe.
					thisLine = inputstream.readline().strip()

					while thisLine != "STEPS":
						initialState["Unused"].append(thisLine)
						thisLine = inputstream.readline().strip()

					# We do not take an additional step here, since
					# we have already stepped one line too far.
					continue

				elif thisLine == "STEPS":
					# We update our recipe plan to incorporate
					# the steps of the recipe.
					thisLine = inputstream.readline().strip()

					while thisLine != "RESULT":
						plan.append(parseStepToCommand(thisLine))
						thisLine = inputstream.readline().strip()

					# We do not take an additional step here, since
					# we have already stepped one line too far.
					continue
					 
				elif thisLine == "RESULT":
					# We update our goal's state to incorporate
					# the resulting state of the recipe.
					thisLine = inputstream.readline().strip()
					while thisLine != "END":
						# We skip commented lines within the results.
						if thisLine[0] == "#":
							thisLine = inputstream.readline().strip()
							continue
						elif thisLine == "":
							thisLine = inputstream.readline().strip()
							continue
						else:
							# We assume then that 'thisLine' refers to
							# one of the keys for our goal state.
							thisKey = thisLine.title()

							thisLine = inputstream.readline().strip()
							# Continue reading in values until we reach a
							# different key property (in upper case)
							while thisLine.upper() != thisLine:
								if thisKey == "Stack":
									goalState[thisKey].append(thisLine)
								elif thisKey in ["Spread2", "Spread1"]:
									goalState[thisKey] = thisLine
								else:
									goalState[thisKey].append(thisLine)

								thisLine = inputstream.readline().strip()

					continue

			thisRecipe = RecipeCase(recipeName, initialState, goalState, plan)

			# Append this RecipeCase to either our casebase or our goals,
			# depending on whether this recipe is a 'goal' recipe.
			if isGoal:
				recipeGoalList.append(thisRecipe)
			else:
				recipeCaseList.append(thisRecipe)

			# Step once more in file to look for the next recipe.
			thisLine = inputstream.readline().strip()
			continue

	return (recipeCaseList, recipeGoalList)


#####################################################################
# 
###
def main():
	recipeCaseList = []
	recipeGoalList = []

	# We read in past recipes and future recipe goals from
	# an input file.
	(recipeCaseList, recipeGoalList) = parseFile("casebase/HandMadeCaseBase.txt")

	# We initialize the CBR reasoner.
	cbr = CBR(recipeCaseList)
	#print(str(cbr)) # TEST

	# We output the case in the casebase that is most similar
	# to each goal recipe.
	print("Now testing SIMILARITY MEASURE")
	print("______________________________")
	print("")
	for goal in recipeGoalList:
		print("Goal: " + goal.name)

		closest = cbr.casebase.getSimilarRecipe(goal)
		print("Closest: " + closest.name)

		print("")
	print("______________________________")

main()