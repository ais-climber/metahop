from recipebase import *

#####################################################################
# Meta Actions
# 
# This file contains descriptions of 'meta actions', i.e. actions
# that are performed on a *partial plan* in order to "fill it in".
# 
# A partial plan (given as parameter 'metastate') is represented
# as a 'RecipeCase' R, and has:
# 	- R.initial_state - The initial base state
# 	- R.goal_state - The final base state
# 	- R.plan - The (initially empty) plan to fill in.
# 
# Meta actions operate on our state R, and aim to fill in R.plan
# in order to be a complete plan from R.initial_state to R.goal_state.
# 
# NOTE: We assume that the working plan is VALID STARTING AT THE INITIAL
# 	STATE.  i.e. it is an incomplete plan, but is complete from the left-hand
# 	side.  All of these meta actions ensure that the working plan is
# 	valid from the initial state, i.e. all of the preconditions are
#	preserved.
#
###

#####################################################################
###########################  Meta Actions  ##########################
#####################################################################

#####################################################################
######################### HELPER FUNCTIONS ##########################
#####################################################################

#####################################################################
# Helper function to retrieve the closest plan from the casebase.
# 
# TODO: CHECK PRECONDITIONS!
###
def _retrieve_closest(metastate, casebase):
	return casebase.getSimilarRecipe(metastate).plan

#####################################################################
# Helper function to retrieve the plan of our choice from the casebase.
# 
###
def _precond_retrieve_indexed_plan(metastate, casebase, i):
	return i <= len(casebase.base) - 1

def _retrieve_indexed_plan(metastate, casebase, i):
	if _precond_retrieve_indexed_plan(metastate, casebase, i):
		return casebase.base[i]
	else:
		print("_retrieve_indexed_plan: PRECONDITIONS NOT MET")

#####################################################################
# 
# 
# TODO: CHECK PRECONDITIONS!  We can only substitute the ingredients
#	if the resulting plan is valid!
# TODO: DEBUG!  I haven't actually made sure that this works!
###
def _precond_substitute_ingredient_in_plan(metastate, somePlan, oldIngredient, newIngredient):
	return True

def _substitute_ingredient_in_plan(metastate, somePlan, oldIngredient, newIngredient):
	if precond_substitute_ingredient(metastate, somePlan, oldIngredient, newIngredient):
		# HEADS UP: This method of replacing strings in a list
		# is a cheeky hack.  We convert the list to a string, and then evaluate
		# it back to a list after replacement.
		# Finally, we substitute the ingredients in the intervening steps.
		return eval(str(somePlan).replace(oldIngredient, newIngredient))
		
	else:
		print("substitute_ingredient_in_plan: PRECONDITIONS NOT MET")


#####################################################################
########################### BASIC ACTIONS ###########################
#####################################################################

#####################################################################
# Basic meta action to insert a step into the working plan.
# 
# TODO: ENSURE THAT 'someAction' IS INSERTED S.T. PRECONDITIONS OF THE
# 	ACTION ARE MET!
###
def precond_insert_step(metastate, someAction, i):
	return i <= len(metastate.plan)

def insert_step(metastate, someAction, i):
	if precond_insert_step(metastate, someAction, i):
		metastate.plan.insert(i, someAction)
	else:
		print("insert_step: PRECONDITIONS NOT MET")

#####################################################################
# Basic meta action to remove a step from the working plan.
# 
# TODO: ENSURE THAT WE CAN ONLY DELETE THE STEP IF IT PRESERVES
# 	PRECONDITIONS UPON DELETION!
###
def precond_delete_step(metastate, i):
	return i <= len(metastate.plan) - 1

def delete_step(metastate, i):
	if precond_delete_step(metastate, i):
		metastate.plan.pop(i)
	else:
		print("delete_step: PRECONDITIONS NOT MET")

#####################################################################
# 
# 
# TODO: CHECK PRECONDITIONS!  We can only apply the plan if we
# 	can ensure each of the 'insert' actions!
# TODO: DEBUG!  I haven't actually made sure that this works!
###
def precond_apply_plan(metastate, somePlan, i):
	return True # TODO

def apply_plan(metastate, somePlan, i):
	if precond_apply_plan(metastate, somePlan, i):
		j = i
		for action in somePlan:
			insert_step(metastate, action, j)
			j += 1

	else:
		print("apply_plan: PRECONDITIONS NOT MET")

#####################################################################
# 
# 
# TODO: CHECK PRECONDITIONS!  We can only apply the closest plan
# 	if we can do the retrieval AND apply the plan!
###
def precond_apply_closest_plan(metastate, casebase, i):
	return precond_apply_plan(_retrieve_closest(metastate, casebase), i)

def apply_closest_plan(metastate, casebase, i):
	if precond_apply_closest_plan(metastate, casebase, i):
		closest = _retrieve_closest(metastate, casebase)
		apply_plan(closest, i)
	else:
		print("apply_closest_plan: PRECONDITIONS NOT MET")

#####################################################################
# 
# 
# TODO: CHECK PRECONDITIONS!  We can only apply the closest plan
# 	if we can do the retrieval AND apply the plan!
###
def precond_apply_indexed_plan(metastate, casebase, i, j):
	return (precond_retrieve_indexed_plan(metastate, casebase, i) and
		precond_apply_plan(_retrieve_indexed_plan(metastate, casebase, i), j))

def apply_indexed_plan(metastate, casebase, i, j):
	if precond_apply_indexed_plan(metastate, casebase, i, j):
		indexed = _retrieve_indexed_plan(metastate, casebase, i)
		apply_plan(indexed, j)
	else:
		print("apply_indexed_plan: PRECONDITIONS NOT MET")

#####################################################################
# 
# 
# TODO: CHECK PRECONDITIONS!  We can only apply the substituted plan
# 	if we can do the substitution AND apply the plan!
###
def precond_apply_substituted_plan(metastate, somePlan, oldIngredient, newIngredient, i):
	return precond_apply_plan(_substitute_ingredient_in_plan(metastate, somePlan, oldIngredient, newIngredient), i)

def apply_substituted_plan(metastate, somePlan, oldIngredient, newIngredient, i):
	if precond_apply_substituted_plan(metastate, somePlan, oldIngredient, newIngredient, i):
		subst = _substitute_ingredient_in_plan(metastate, somePlan, oldIngredient, newIngredient)
		apply_plan(subst, i)
	else:
		print("apply_substituted_plan: PRECONDITIONS NOT MET")

#####################################################################
# 
# 
# TODO: CHECK PRECONDITIONS!  We can only apply the substituted plan
# 	if we can do the substitution AND apply the plan!
###
def precond_apply_closest_and_substitute(metastate, casebase, oldIngredient, newIngredient, i):
	return precond_apply_plan(_substitute_ingredient_in_plan(metastate, 
		_retrieve_closest(metastate, casebase), oldIngredient, newIngredient), i)

def apply_closest_and_substitute(metastate, casebase, oldIngredient, newIngredient, i):
	if precond_apply_closest_and_substitute(metastate, casebase, oldIngredient, newIngredient, i):
		closest = _retrieve_closest(metastate, casebase)
		subst = _substitute_ingredient_in_plan(metastate, closest, oldIngredient, newIngredient)
		apply_plan(subst, i)
	else:
		print("apply_closest_and_substitute: PRECONDITIONS NOT MET")


#####################################################################
# Meta action to swap two actions in the working plan.
# 
# TODO: PRECONDITIONS?  We should only do this if the preconds
# 	for the inserts and deletes are met.
# TODO: DEBUG!  I actually haven't debugged this at all yet.
###
def precond_switch_steps(metastate, i, j):
	return precond_insert_step(metastate, metastate.plan[i], j) and
		precond_insert_step(metastate, metastate.plan[j+1], i) and
		precond_delete_step(metastate, i+1) and
		precond_delete_step(metastate, j+1)

def switch_steps(metastate, i, j):
	if precond_switch_steps(metastate, i, j):
		insert_step(metastate, metastate.plan[i], j)
		insert_step(metastate, metastate.plan[j+1], i)
		delete_step(metastate, i+1)
		delete_step(metastate, j+1)

	else:
		print("switch_steps: PRECONDITIONS NOT MET")

#####################################################################
##################### USER-FACING META-ACTIONS ######################
#####################################################################








# We also define a general function for checking the preconditions
# of any arbitrary meta-action.
def meta_preconditions_met(metaaction, metastate, arg1=None, arg2=None, arg3=None):
	if metaaction.__name__ == "insert_step":
		return precond_insert_step(metastate, arg1, arg2)
	elif metaaction.__name__ == "delete_step":
		return precond_delete_step(metastate, arg1)
	elif metaaction.__name__ == "apply_plan":
		return precond_apply_plan(metastate, arg1, arg2)
	elif metaaction.__name__ == "apply_closest_plan":
		return precond_apply_closest_plan(metastate, arg1, arg2)
	elif metaaction.__name__ == "apply_indexed_plan":
		return precond_apply_indexed_plan(metastate, arg1, arg2, arg3)
	elif metaaction.__name__ == "switch_steps":
		return precond_switch_steps(metastate, arg1, arg2)
