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
	'beef' : 'vegan meat',
	'pork' : 'tofu',
	'chicken' : 'vegan chicken',
	'turkey' : 'vegan turkey',
	'quail' : 'tofu',
	'ham' : 'tempeh',
	'veal' : 'tofu',
	'lamb' : 'tofu',
	'mutton' : 'tofu',
	'sausage' : 'vegan sausage',
	'duck' : 'tofu',
	'gelatin' : 'agar agar',
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


	# transform recipe
	for n, step in enumerate(recipe):
		for item in swaps:
			# how are they doing it without this
			without_first = None
			split_item = item.split()
			if len(split_item) > 1:
				without_first = ' '.join(split_item[1:])
			last_word = split_item[-1]
			first_word = split_item[0]

			# check if entire item is in step
			re_obj = re.search(item, step)
			if re_obj:
				step = re.sub(item, swaps[item], step)

			# check if all but first word is in step
			elif without_first != None and re.search(without_first, step):
				step = re.sub(without_first, swaps[item], step)

			# check if last word is in step
			elif re.search(last_word, step):
				step = re.sub(last_word, swaps[item], step)

			elif (len(split_item) < 3):
				if re.search(first_word, step):
					step = re.sub(first_word, swaps[item].split()[0], step)

			recipe[n] = step

	return ingredients_data, recipe

ingredients_data = get_ingredients_data(ingredients)
print(make_vegetarian(ingredients_data, recipe))
