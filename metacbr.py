# The Meta - Case Based Reasoner (MetaCBR)
#   for recipe generation
# 
# Author: Caleb Kisby

from adaptationbase import adaptationbase

class MetaCBR():
	
	#################################################################
	# The usual initializer.
	###
	def __init__(self, adaptationCaseList):
		# Generate the recipe base from a hardcoded file.
		self.metabase = AdaptationBase(adaptationCaseList)

	#################################################################
	# Function to generate an adaptation.
	# 
	# This function takes in an *empty* AdaptationCase and generates
	# the actual adaptation, i.e. fills in its *metaplan* from
	# its initial recipe to its goal recipe.
	# 
	# We intend to do this fairly naiively, and domain-independently.
	# 
	# NOTE: Currently we do the EXTREMELY NAIIVE THING, which is to
	# just return the most similar adaptation.  This is just FOR TESTING
	# PURPOSES ONLY!
	###
	def generateAdaptation(self, emptyAdaptationCase):
		return self.metabase.getSimilarAdaptation(emptyAdaptationCase)

	#################################################################
	# Function to store an adaptation in the case base.
	# 
	# This function takes in a *complete* AdaptationCase and stores it
	# in the metabase.
	###
	def storeAdaptation(self, completeAdaptationCase):
		self.metabase.addAdaptation(completeAdaptationCase)

	#################################################################
	# The usual toString.
	###
	def __str__(self):
		return str(self.metabase)


