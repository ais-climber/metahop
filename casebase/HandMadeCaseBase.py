# 
# 
# 
# 

# RECIPE FOR RECIPES
"""
RECIPEi = {"NAME" : "",
        "INITIAL" : {
            "UNUSED" : set({}),
            "MAKE_BOARD" : [],
            "CUT_BOARD" : set({}),
            "PAN" : set({}),
            "TEMP" : {},
            "TOASTED" : {},
            "FRIED" : {},
            "SLICED" : {}
        },
        "STEPS" : [[], []],
        "FINAL" : {
            "UNUSED" : set({}),
            "MAKE_BOARD" : [],
            "CUT_BOARD" : set({}),
            "PAN" : set({}),
            "TEMP" : {},
            "TOASTED" : {},
            "FRIED" : {},
            "SLICED" : {}
        },
}
"""

# Peanut Butter and Jelly
RECIPE1 = {"NAME" : "Peanut Butter and Jelly",
        "INITIAL" : {
            "UNUSED" : 
                set({"white bread 1", "white bread 2", 
                    "peanut butter", "grape jelly"}),
            "MAKE_BOARD" : [],
            "CUT_BOARD" : set({}),
            "PAN" : set({}),
            "TEMP" : {
                "white bread 1" : "COLD",
                "white bread 2" : "COLD",
                "peanut butter" : "COLD",
                "grape jelly" : "COLD"},
            "TOASTED" : {
                "white bread 1" : False,
                "white bread 2" : False,
                "peanut butter" : False,
                "grape jelly" : False}
            "FRIED" : {
                "white bread 1" : False,
                "white bread 2" : False,
                "peanut butter" : False,
                "grape jelly" : False},
            "SLICED" : {
                "white bread 1" : False,
                "white bread 2" : False,
                "peanut butter" : False,
                "grape jelly" : False}
        },
        "STEPS" : [
            ["MOVE", "white bread 1", "MAKE_BOARD"], 
            ["SPREAD", "peanut butter", "white bread 1"],
            ["MOVE", "white bread 2", "MAKE_BOARD"],
            ["SPREAD", "grape jelly", "white bread 2"],
            ["PLACE", "white bread 1", "white bread 2"]
            ],
        "FINAL" : {
            "UNUSED" : 
                set({}),
            "MAKE_BOARD" : ["white bread", "peanut butter", 
                "grape jelly", "white bread"],
            "CUT_BOARD" : set({}),
            "PAN" : set({}),
            "TEMP" : {
                "white bread 1" : "COLD",
                "white bread 2" : "COLD",
                "peanut butter" : "COLD",
                "grape jelly" : "COLD"},
            "TOASTED" : {
                "white bread 1" : False,
                "white bread 2" : False,
                "peanut butter" : False,
                "grape jelly" : False}
            "FRIED" : {
                "white bread 1" : False,
                "white bread 2" : False,
                "peanut butter" : False,
                "grape jelly" : False},
            "SLICED" : {
                "white bread 1" : False,
                "white bread 2" : False,
                "peanut butter" : False,
                "grape jelly" : False}
        },
}


