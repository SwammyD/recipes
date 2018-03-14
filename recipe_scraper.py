import bs4
import json
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

descriptors = [
	'chopped',
	'minced',
	'cut',
	'or',
	'sliced',
	'rinsed',
	'diced'
]

def scrape_ingredients(recipe_url):
	# url of award show wiki page
	my_url = recipe_url
	

	# grab webpage html
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	# html parsing
	page_soup = soup(page_html, "html.parser")

	recipe_script = []
	ingredient_list = []

	# find the ingredients by html tag
	recipe_script = page_soup.findAll('span', {"class": "recipe-ingred_txt added"})
	for ingredient in recipe_script:
		text = ingredient.text.strip()
		ingredient_list.append(text)
	return ingredient_list


def scrape_instructions(recipe_url):
	my_url = recipe_url
	

	# grab webpage html
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	# html parsing
	page_soup = soup(page_html, "html.parser")

	recipe_script = []
	instructions_list = []

	# find the instructions by html tag
	recipe_script = page_soup.findAll('span', {"class": "recipe-directions__list--item"})
	for step in recipe_script:
		text = step.text.strip()
		instructions_list.append(text)
	return instructions_list




def getIngredient(ingredients):
	parsed_ingredients = []
	ingredient = []
	quantity = []
	measurement = []

	for words in ingredients:
		if re.search('\(', words):
				# get rid of trademark
				words = re.sub('\(R\)', '', words)
				# get rid of other parentheses
				words = re.sub(r'\s\([^)]*\)', '', words)
		food = ''
		words_list = words.split()
		for word in words_list:
			if re.search('[1-9]', word) or re.search('[1-9]\/[1-9]', word) or re.search('\([1-9]+ [a-z]+\)', word):
				quantity.append(word)
			elif word in ['teaspoon', 'teaspoons', 'cup', 'cups', 'ounce', 'ounces', 'clove', 'pound', 'tablespoons', 'container', 'package', 'tablespoon', 'bunch', 'can', 'cans', 'pounds']:
				measurement.append(word)
			elif ')' not in word:
				food = food + ' ' +  word
		ingredient.append(food)

	matches = []
	for item in ingredient:
		#print(item)
		m = re.findall(r"((\w+ ?-?)+)", item)
		matches.append([x[0] for x in m])
	#print(matches)

	for part in matches:
		if len(part) > 1:
			ingr = ''
			found = False
			for descriptor in descriptors:
				if descriptor in part[1]:
					found = True
			if not found: 
				ingr = part[1]
				parsed_ingredients.append(ingr)
			else:
				ingr = part[0]
				parsed_ingredients.append(ingr)
		else:
			ingr = part[0]
			parsed_ingredients.append(ingr)

	return quantity, measurement, parsed_ingredients


ingredients_list = scrape_ingredients('https://www.allrecipes.com/recipe/21340/lindas-lasagna/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202')
extracted_ingredients = getIngredient(ingredients_list)
print(extracted_ingredients)
#print(scrape_instructions('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'))


#print(scrape_instructions('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'))