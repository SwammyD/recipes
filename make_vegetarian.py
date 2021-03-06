from recipe_scraper import *

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

def makeVegetarian(url):
	my_url = url

	ingredients = scrape_ingredients(url)
	recipe = scrape_instructions(url)
	ingredients_data = get_ingredients_data(ingredients)
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

		#remove the word 'meat' in instructions if it's present
		if re.search('[M,m]eat', step):
			step = re.sub('\s?[M,m]eat[.,-]?', '', step)

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

	for step in recipe:
		print(step)
