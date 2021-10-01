# Learning Multi-Plan Adaptation: A Puzzle

### notes by Caleb Kisby



“The importance of PARADOX and CONTRADICTION.
When you can prove that a statement S is true, 
and you can prove that the same statement S is false, 
then you KNOW that that you're on to something:
Something is wrong somewhere. 
Never underestimate the power of a contradiction. 
It is one of our most potent sources of knowledge.”

​				- Manuel Blum

----



I have been implementing a CBR system that _learns_ plan adaptation (much like WebAdapt and DIAL).  This system intends, in particular, to learn _multi-plan adaptation_ (of the kind described in [1] by Ram and Francis).



The model I have been using so far for such a multi-plan adaptation is the following:  We begin with an initial _empty plan_, and during the process of adaptation retrieve any number of relevant plans at any time, extract a segment of them, and apply that segment to the current plan (from the left-hand side of the plan).  This kind of adaptation is better called _plan generation_, since it involves the entire process of generating a plan by retrieving and adapting relevant past plans.

**Figure 1: Plan Generation**

$S_1 \quad \quad \quad \quad \quad \quad \quad S_n​$

$\quad \quad \quad \quad \downarrow \quad \quad \quad \quad$ (retrieve and apply relevant plan)

$\quad \quad \quad \quad \ldots \quad \quad \quad \quad$

$\quad \quad \quad \quad \downarrow \quad \quad \quad \quad$ (perhaps make some small changes to resulting plan)

$S_1 \to \to \to \to \to \to \to S_n$



Since my system hopes to _learn_ plan adaptation, we also have an _adaptation generation_ method, which begins with an _empty adaptation_ (i.e. has an _initial plan_ and a _final plan_, but has an empty sequence of steps to get from here to there).  Our adaptation generation retrieves past adaptations in order to fill in the sequence of steps to get to the final recipe.



Ok, so now the problem:



Suppose we are trying to generate a plan.  To make things concrete, let’s say we are trying to generate a recipe to prepare a grilled cheese with tomato.  Perhaps we already know how to make grilled cheese, and we have a number of adaptations that we already know how to perform (e.g. how to get a peanut butter and banana sandwich from a peanut butter and jelly sandwich).



So we begin generating the plan.  We start with the empty plan, where in this case $S_1$ is the state of ingredients being in the pantry, and $S_n$ is the completed grilled cheese sandwich with a tomato wedged in the middle.  Since we want to perform multi-plan adaptation, we do not retrieve and apply a particular plan yet; instead, we leave it up to our adaptation to decide when to retrieve and apply plans.  Since we are learning adaptation, our adaptation should be whatever is generated via _adaptation generation_.  So we perform adaptation generation.  By our specification above, adaptation generation requires an _initial plan_ and a _final plan_.  We have our initial recipe, namely:

$S_1 \quad \quad \quad \quad \quad \quad \quad S_n$

But what of our final plan?  We cannot give adaptation generation any final plan because the final plan is _exactly_ what we are trying to generate!  To quote Blum above, “something is wrong somewhere.”



So what gives (i.e. what is able to give)?  The main assumption that this issue seems to rest on is that our adaptation generation requires a complete final plan in order to execute.  We could imagine generating an adaptation without knowing what the final recipe will be; that is, we would retrieve and apply  past adaptations only knowing what the initial plan is.  Think back to our grilled cheese with tomato example.  Our consideration of what past adaptation is most relevant would have _nothing to do_ with the fact that we want a grilled cheese with tomato!  It would only consider what ingredients we have in our pantry.  In my opinion, this would lose all of the power that case-based reasoning offers.



----

### References

[1] ftp://ftp.cc.gatech.edu/pub/groups/ai/ram/er-96-06.pdf