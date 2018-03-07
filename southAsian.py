import recipe_scraper, re

url = 'https://www.allrecipes.com/recipe/228256/cilantro-and-pork-stir-fry/?internalSource=staff%20pick&referringId=673&referringContentType=recipe%20hub'

ingredients_list = recipe_scraper.scrape_ingredients(url)
recipe_list = recipe_scraper.scrape_instructions(url)


spices = [
	['Italian seasoning','paprika']
	#['','']
	#['','']
]

meats = [
	['Italian sausage','turkey sausage'],
	['ground beef','ground lamb'],
	['pork chops','lamb chops'],
	['ham','lamb'],
	['pork tenderloin','lamb tenderloin'],
	['pork','lamb']
	#['','']
]

def makeSouthAsian(ingredients, recipe):
	for meat in meats:
		for n, ingredient in enumerate(ingredients):
			if meat[0] in ingredient:
				m = re.sub(meat[0], meat[1], ingredient)
				ingredients[n] = m

	for spice in spices:
		for n, ingredient in enumerate(ingredients):
			if spice[0] in ingredient:
				m = re.sub(spice[0], spice[1], ingredient)
				ingredients[n] = m
						

	return ingredients



print(makeSouthAsian(ingredients_list, recipe_list))
