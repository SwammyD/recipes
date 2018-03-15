import recipe_scraper, re
from nltk import *
from textblob import TextBlob
import os
from stanfordcorenlp import StanfordCoreNLP




urls = [
	['https://www.allrecipes.com/recipe/21340/lindas-lasagna/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202'],
	['https://www.allrecipes.com/recipe/223042/chicken-parmesan/?internalSource=streams&referringId=201&referringContentType=recipe%20hub&clickId=st_recipes_mades'],
	['https://www.allrecipes.com/recipe/231523/pork-lo-mein/?internalSource=staff%20pick&referringId=1014&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/255259/homemade-chili/?internalSource=staff%20pick&referringId=92&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/231523/pork-lo-mein/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=255259%20referringContentType%3Drecipe'],
	['https://www.allrecipes.com/recipe/14685/slow-cooker-beef-stew-i/?internalSource=hub%20recipe&referringId=200&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/12897/white-chili-i/?internalSource=staff%20pick&referringId=17021&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/240583/cheesy-ham-and-corn-chowder/?internalSource=staff%20pick&referringId=205&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/255865/slow-cooker-thai-curried-beef/?internalSource=staff%20pick&referringId=92&referringContentType=recipe%20hub']
]

#my_url = urls[4][0]
# ingredients_list = recipe_scraper.scrape_ingredients(my_url)
# recipe_list = recipe_scraper.scrape_instructions(my_url)



substitutions = {
	'Italian seasoning': 'paprika',
	'dry red wine': 'olive oil',
	'red wine': 'olive oil',
	'sweet Italian sausage': 'turkey sausage',
	'ground beef': 'ground lamb',
	'ground pork': 'ground lamb',
	'pork chops': 'lamb chops',
	'ham': 'lamb',
	'pork tenderloin': 'lamb tenderloin',
	'pork': 'lamb',
	'bacon': 'turkey bacon',
	'pork loin': 'lamb loin',
	'pork loin roast': 'lamb loin roast',
	'soy sauce': 'chili sauce',
	'bow tie pasta': 'basmati rice',
	'minced fresh parsley': 'cilantro',
	'Italian sausage': 'turkey sausage',
	'lean ground beef': 'lean ground turkey',
	'dried oregano': 'dried cumin',
	'chopped fresh basil': 'chopped fresh cilantro',
	'low-sodium soy sauce': 'chili sauce',
	'linguine': 'rice',
	'great northern beans': 'chickpeas',
	'dried marjoram': 'fenugreek',
	'diced cooked ham': 'diced cooked lamb',
	'lean stew beef': 'lean stew lamb',
	'beef broth': 'lamb broth',
	'jasmine rice': 'basmati rice',
	'fresh basil leaves': 'fresh cilantro leaves'
}

methods = {
	'drain': 'boiling',
	'bake': 'baking',
	'baking': 'baking',
	'simmer': 'simmering',
	'simmering': 'simmering',
	'bring': 'boiling',
	'caramelize': 'caramelizing',
	'whisk': 'beating',
	'blend': 'blending',
	'saute': 'sauteing',
	'slow': 'slow cook',
	'pressure': 'pressure cook'
}

descriptors = [
	'chopped',
	'minced',
	'cut',
	'or',
	'sliced',
	'rinsed',
	'diced'
]


def makeSouthAsian(ingredients, recipe, url):
	my_url = url
	# ingredients_list = recipe_scraper.scrape_ingredients(my_url)
	# recipe_list = recipe_scraper.scrape_instructions(my_url)

	ingredients_data = recipe_scraper.get_ingredients_data(ingredients)

	swaps = {}
	new_recipe = recipe

	for n, ingredient in enumerate(ingredients_data):
		curr_food = ingredient[2]

		if curr_food in substitutions:
			ingredients_data[n][2] = substitutions[curr_food]
			swaps[curr_food] = substitutions[curr_food]


	# for n, ingredient in enumerate(ingredients):
	# 	ingredient = ingredient.lower()
	# 	if ingredient in substitutions:
	# 		ingredients[n] = substitutions[ingredient]
	# 		swaps[ingredient] = substitutions[ingredient]

	for n, step in enumerate(new_recipe):
		for item in swaps:
			split_item = item.split()
			if len(split_item) > 1:
				without_first = ' '.join(split_item[1:])
			else: 
				without_first = split_item
			last_word = split_item[-1]
			first_word = split_item[0]

			# check if entire item is in step
			re_obj = re.search(item, step)
			if re_obj:
				step = re.sub(item, swaps[item], step)

			# check if all but first word is in step
			elif re.search(without_first, step) and without_first != '':
				step = re.sub(without_first, swaps[item], step)

			# check if last word is in step
			elif re.search(last_word, step):
				step = re.sub(last_word, swaps[item], step)

			elif (len(split_item) < 3):
				if re.search(first_word, step):
					step = re.sub(first_word, swaps[item].split()[0], step)


		new_recipe[n] = step


	print("ingredients:")
	
	for ingr in ingredients_data:
		ingr_str = ''
		for item in ingr:
			if type(item) is list:
				if item != []:
					if ingr_str == '':
						ingr_str = ''.join(item)
					else:
						ingr_str = ingr_str + ' ' + ' '.join(item)
			elif type(item) is int or float:
				ingr_str = ingr_str + ' ' + str(item)
			else:
				if ingr_str == '':
					ingr_str = item
				else:
					ingr_str = ingr_str + ' ' + item

		print(ingr_str)

	print("\n")
	print("recipe:")

	for step in new_recipe:
		print(step)








def extractMethods(recipe):
	methods_list = []

	for step in recipe:
		words = step.split()
		for word in words:
			stripped_word = word.replace(',', '')
			stripped_word = stripped_word.replace('.', '')
			if stripped_word.lower() in methods:
				methods_list.append(methods[stripped_word.lower()])

	return methods_list


# print(extractMethods(recipe_list))

# recipe_url = 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'
# ingredients_list = recipe_scraper.scrape_ingredients(str(recipe_url))
# instructions_list = recipe_scraper.scrape_instructions(str(recipe_url))
# # #print(extracted_ingredients)
# makeSouthAsian(ingredients_list, instructions_list, recipe_url)

