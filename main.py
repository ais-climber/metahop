
from cbr import *
from fileparser import *

#####################################################################
# 
###
def main():
	recipeCaseList = []
	recipeGoalList = []

	adaptationCaseList = []
	adaptationGoalList = []

	# We read in past recipes, adaptations and future recipe, adaptation *goals* from
	# an input file.
	(recipeCaseList, recipeGoalList) = parseJSONCaseBase("casebase/JSONCaseBase.json")
	(adaptationCaseList, adaptationGoalList) = parseJSONAdaptationBase("casebase/JSONAdaptationBase.json")

	# We initialize the CBR reasoner.
	cbr = CBR(recipeCaseList, adaptationCaseList) #TODOTODOTODO Give it an 'adaptationCase'!!!
	#print(str(cbr)) # TEST

	###########################################################################
	# 							THE ACTUAL TESTS							  #
	###########################################################################

	# We output the case in the casebase that is most similar
	# to each goal recipe.
	print("Now testing SIMILARITY MEASURE")
	print("______________________________")
	print("")
	for goal in recipeGoalList:
		print("______________________________")
		print("Goal: " + goal.name + "\n")

		closest = cbr.casebase.getSimilarRecipe(goal)
		# cbr.storeRecipe(closest) ## TODO: Storing recipes does not work currently!
		print("Closest: ")
		print(closest)

		print("")
	print("______________________________")

main()