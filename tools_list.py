# basic idea: certain cooking terms will be linked to different tools
# when a cooking term shows up, we know that the corresponding tool is used
# TODO: attach cooking methodology to each tool.
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

#instructions = 'Combine ground beef, onion, bread crumbs, broth, egg, Parmesan cheese, 2 tablespoons ketchup, Worcestershire sauce, Italian seasoning, parsley, and garlic powder in a bowl using your hands. Form into a loaf. Center the loaf in the bottom of a slow cooker, leaving room on the sides. Coat meatloaf with 1/4 cup ketchup and surround with potatoes and carrots. Cook on High, about 2 hours. Reduce heat setting to Low; cook until meatloaf is no longer pink in the center and vegetables are tender, 4 to 6 hours more. An instant-read thermometer inserted into the center should read at least 160 degrees F (70 degrees C).'

instructions = "Preheat oven to 350 degrees F (175 degrees C). Grease and flour a 9x13 inch pan. In a large bowl, beat together eggs, oil, white sugar and 2 teaspoons vanilla. Mix in flour, baking soda, baking powder, salt and cinnamon. Stir in carrots. Fold in pecans. Pour into prepared pan. Bake in the preheated oven for 40 to 50 minutes, or until a toothpick inserted into the center of the cake comes out clean. Let cool in pan for 10 minutes, then turn out onto a wire rack and cool completely. To Make Frosting: In a medium bowl, combine butter, cream cheese, confectioners' sugar and 1 teaspoon vanilla. Beat until the mixture is smooth and creamy. Stir in chopped pecans. Frost the cooled cake."

# stove
# tongs
# oven
# wooden spoon
# spatula
# shaker
# strainer

def makeToolsList( instructions ):
	toolsList = []
	for term in tools:
			if  term[0] in instructions.lower():
				if term[1] not in toolsList:
					toolsList.append(term[1])
	if 'bowl' in toolsList and 'wooden spoon' not in toolsList:
		toolsList.append('wooden spoon')
	print(toolsList)

makeToolsList(instructions)