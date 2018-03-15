from recipe_scraper import *

ingredients = scrape_ingredients('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades')
recipe = scrape_instructions('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades')

# if we find one of these things, I want to replace just the food part of the ingredient (quantiy, measurement, food)
# maybe add keywords for if the quanitity won't work for the substitue (e.g. one chicken)

# TODO: add fish
subs = {
	'beef stock' : 'vegetable broth',
	'chicken stock' : 'vegetable broth',
	'beef broth' : 'vegetable broth',
	'chicken broth' : 'vegetable broth',
	'beef' : 'tofu',
	'pork' : 'tofu',
	'chicken' : 'tofu',
	'turkey' : 'tofu',
	'quail' : 'tofu',
	'ham' : 'tofu',
	'veal' : 'tofu',
	'lamb' : 'tofu',
	'mutton' : 'tofu',
	'sausage' : 'tofu',
	'duck' : 'tofu',
	'gelatin' : 'agar agar'
}

#special case: fish products (fish sauce, fish paste) just change to "vegan fish _____ substitute"
# fish_product_sub = [('fish'), '']

def make_vegetarian(ingredients_data, recipe):
	# the actual swaps we make
	swaps = {}

	# transform ingredients
	for n, ingredient in enumerate(ingredients_data):
		curr_food = ingredient[2]

		for key, value in subs.items():
			if key in curr_food:
				# tuples don't support item assignment, we could either pop the tuple or represent ings with a list of lists
				ingredients_data[n][2] = value
				swaps[key] = value

	return ingredients_data, recipe

ingredients_data = get_ingredients_data(ingredients)
print(make_vegetarian(ingredients_data, recipe))
