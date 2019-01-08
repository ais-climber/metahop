# Actions
# 
# 

# First, we need a VERY basic knowledge base in order
# to determine what effects certain actions have.

def stackable(ingredient):
	stackables = ["white bread", "cheddar cheese", "pimento cheese", "banana", "tomato", "spinach"]

	return ingredient in stackables

def spreadable(ingredient):
	spreadables = ["peanut butter", "grape jelly", "butter", "mayonnaise", "honey"]

	return ingredient in spreadables

def heatable(ingredient):
	heatables = ["white bread", "cheddar cheese", "pimento cheese", "banana", "tomato", "spinach", 
				"peanut butter", "grape jelly", "butter", "mayonnaise", "honey"]

	return ingredient in heatables

def meltable(ingredient):
	meltables = ["cheddar cheese", "pimento cheese", "peanut butter", "grape jelly", "butter", "mayonnaise", "honey"]

	return ingredient in meltables

def toastable(ingredient):
	toastables = ["white bread", "banana", "tomato"]

	return ingredient in toastables

#
#
# 
# Now we define the actual actions on a state:

def stack(state, ingredient):
	if (ingredient in state["unused"] and stackable(ingredient)):
		state["unused"].remove(ingredient)
		state["stack"] = [ingredient] + state["stack"]
	else:
		print("stack: PRECONDITIONS NOT MET")

def spread(state, ingredient, number):
	if (ingredient in state["unused"] and number in [1, 2] and spreadable(ingredient)):
		state["unused"].remove(ingredient)

		if number == 1:
			state["spread1"] = ingredient
		elif number == 2:
			state["spread2"] = ingredient
	
	else:
		print("spread: PRECONDITIONS NOT MET")

def toast_stack(state):
	# No preconditions are necessary; we can always toast the stack.

	# Heat and melt any heatable or meltable ingredients, including the spreads.
	for ingredient in state["stack"] + [state["spread1"]] + [state["spread2"]]:
		if heatable(ingredient):
			state["hot"].append(ingredient)

		if meltable(ingredient):
			state["melted"].append(ingredient)

	# Toast the ingredients on the two ends of the sandwich stack, if they are
	# toastable.
	for ingredient in [state["stack"][0]] + [state["stack"][len(state["stack"]) - 1]]:
		if toastable(ingredient):
			state["toasted"].append(ingredient)







