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
# Next, we need to define functions that give the preconditions
# for each action.  This allows us later to check whether the
# preconditions are satisfied without actually performing the
# effects.

#
#
# 
# Now we define the actual actions' effects on a state.
# 
# For debugging, actions will return 'True' if they are
# successfully performed, and 'False' if their preconditions
# are not met.
def precond_stack(state, ingredient):
	return ingredient in state["unused"] and stackable(ingredient) 

def stack(state, ingredient):
	if precond_stack(state, ingredient):
		state["unused"].remove(ingredient)
		state["stack"] = [ingredient] + state["stack"]
	else:
		print("stack: PRECONDITIONS NOT MET")

def precond_spread(state, ingredient, number):
	return ingredient in state["unused"] and number in [1, 2] and spreadable(ingredient)

def spread(state, ingredient, number):
	if precond_spread(state, ingredient, number):
		state["unused"].remove(ingredient)

		if number == 1:
			state["spread1"] = ingredient
		elif number == 2:
			state["spread2"] = ingredient
	
	else:
		print("spread: PRECONDITIONS NOT MET")

def precond_toast_stack(state):
	return True

def toast_stack(state):
	if precond_toast_stack(state):
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

	else:
		print("toast_stack: PRECONDITIONS NOT MET")

# We also define a general function for checking the preconditions
# of any arbitrary action.
def preconditions_met(action, state, arg1=None, arg2=None):
	if action.__name__ == "stack":
		return precond_stack(state, arg1)
	elif action.__name__ == "spread":
		return precond_spread(state, arg1, arg2)
	elif action.__name__ == "toast_stack":
		return precond_toast_stack(state)





