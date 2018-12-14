
from cbr import *
from fileparser import *

#####################################################################
# 
###
def main():
	recipeCaseList = []
	recipeGoalList = []

	# We read in past recipes and future recipe goals from
	# an input file.
	(recipeCaseList, recipeGoalList) = parseJSONFile("casebase/JSONCaseBase.json")

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
		# cbr.storeRecipe(closest) ## TODO: Storing recipes does not work currently!
		print("Closest: " + closest.name)

		print("")
	print("______________________________")

main()