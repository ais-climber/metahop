from pyhop import *

# NOTE: initial_state and goal_state must be STRINGS
#       Similarly, 'states' must consist of strings indexing states!

class RecipeCase():
    def __init__(self, name, states, initial_state_name,
            goal_state_name, actions):
        self.name = name
        self.initial_state_name = initial_state
        self.goal_state_name = goal_state

        # The plan is a list of actions.  The plan may be empty,
        # incomplete, or incorrect.
        self.plan = actions

        # 



