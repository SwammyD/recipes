from recipe_scraper import *

#instructions = scrape_instructions()

# basic idea: certain cooking terms will be linked to different tools
# when a cooking term shows up, we know that the corresponding tool is used
tools = [

	["al dente", "pot"],
	["al dente", "stove"],
	["bake", "oven"],
	["bake", "baking sheet"],
	["barbeque", "grill"],
	["baste", "baster"],
	["batter", "mixer"],
	["batter", "plastic spatula"],
	["batter", "bowl"],
	["beat", "whisk"],
	["beat", "bowl"],
	["blanch", "pot"],
	["blanch", "stove"],
	["blend", "mixer"],
	["blend", "bowl"],
	["blend", "blender"],
	["boil", "pot"],
	["boil", "stove"],
	["broil", "oven"],
	["broil", "baking sheet"],
	["brush", "brush"],
	["caramelize", "pan"],
	["chop", "knife"],
	["combine", "bowl"],
	["cream", "whisk"],		# or fork
	["cure", "salt shaker"],
	["cure", "smokehouse"],
	["deglaze", "pan"],
	["degrease", "refrigerator"],
	["degrease", "wooden spoon"],
	["dice", "knife"],
	["dissolve", "wooden spoon"],
	["dissolve", "pot"],
	["dissolve", "stove"],
	["drizzle", "baster"],		# up for debate
	["dust", "strainer"],
	["fillet", "knife"],
	["flambe", "alcohol"],
	["flambe", "lighter"],
	["fold", "plastic spatula"],
	["fry", "deep fryer"],
	["pan-fry", "pan"],
	["glaze", "brush"],
	["grate", "grater"],
	["gratin", "oven"],
	["gratin", "baking sheet"],
	["grill", "grill"],
	["grind", "grinder"],
	["heat setting", "oven"],
	["julienne", "knife"],
	["kneed", "hands"],
	["loaf", "loaf pan"],
	["marinate", "brush"],
	["meuniere", "pan"],
	["mince", "knife"],
	["mix", "wooden spoon"],
	["pan-broil", "fry pan"],
	["pan-fry", "shallow pan"],
	["parboil", "pot"],
	["parboil", "stove"],
	["pare", "knife"],
	["peel", "knife"],
	["peel", "peeler"],
	["pickle", "brine"],
	["pit", "knife"],
	["planked", "wooden plank"],	# apparently this is a thing?
	["plump", "bowl"],
	["poach", "pot"],
	["pot", "wooden spoon"],
	["puree", "blender"],
	["reduce", "pot"],
	["reduce", "stove"],
	["refresh", "kitchen sink"],
	["roast", "oven"],
	["roast", "baking sheet"],
	["saute", "shallow pan"],
	["scallop", "oven"],
	["scallop", "baking sheet"],
	["score", "knife"],
	["sear", "flame"],
	["shred", "knife"],
	["sift", "sieve/sifter"],
	["simmer", "pot"],
	["simmer", "stove"],
	["skim", "wooden spoon"],
	["slice", "slicer"],
	["slice", "knife"],
	["soup", "ladle"],
	["steam", "pressure cooker"],
	["steep", "stove"],
	["steep", "pot"],
	["stew", "pot"],
	["stew", "stove"],
	["stir", "wooden spoon"],
	["tablespoon", "tablespoon"],
	["teaspoon", "teaspoon"],
	["thermometer", "thermometer"],
	["toss", "tongs"],
	["toss", "bowl"],
	["truss", "skewers"],
	["whip", "whisk"],
	["whip", "mixer"],
	["whip", "bowl"],
	["microwave", "microwave oven"],
	["chicken", "gloves"]

]

def makeToolsList( url ):
	instructions = scrape_instructions(url)
	toolsList = []
	for term in tools:
		for step in instructions: 
			if  term[0] in step.lower() and term[1] not in toolsList:
				toolsList.append(term[1])
			if term[1] in step.lower() and term[1] not in toolsList:
				toolsList.append(term[1])
	if 'bowl' in toolsList and 'wooden spoon' not in toolsList:
		toolsList.append('wooden spoon')
	return toolsList