import bs4
import json
import re
from recipe_scraper import *
from tools_list import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import nltk

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




def get_ingredients_data(ingredients):

	# a list of tuples, where the first item in the tuple is a list of the quantities, the second is a list of measurements, and the third is a string with the meaningful part of the food (everything else parsed out)
	ingredients_data = []

	for words in ingredients:
		quantity = []
		measurement = []
		food = ''

		# if parens are in the ingredient, delete them
		if re.search('\(', words):
			# get rid of trademark
			words = re.sub('\(R\)', '', words)
			# get rid of other parentheses
			words = re.sub(r'\s\([^)]*\)', '', words)

		words_list = words.split()
		for word in words_list:
			# if it's a quantity
			if re.search('[1-9]', word) or re.search('[1-9]\/[1-9]', word) or re.search('\([1-9]+ [a-z]+\)', word):
				quantity.append(word)
			# if it's a measure
			elif word in ['teaspoon', 'teaspoons', 'cup', 'cups', 'ounce', 'ounces', 'clove', 'pound', 'tablespoons', 'container', 'package', 'tablespoon', 'bunch', 'can', 'cans', 'pounds']:
				measurement.append(word)
			# otherwise it's part of food so create a string that has the entire food part of the ingredient
			else:
				if food == '':
					food += word
				else:
					food += ' ' + word
			if len(quantity) > 1:
				quantity = ['+'.join(x for x in quantity)]

		# now we have a string of the food part of the ingredient. let's take out stuff we don't need
		m = re.findall(r"((\w+ ?-?)+)", food)
		match = [x[0] for x in m]

		if len(match) > 1:
			found = False
			for descriptor in descriptors:
				if descriptor in match[1]:
					found = True
					if not found:
						food = match[1]
					else:
						food = match[0]
				else:
					food = match[0]

		ingredients_data.append(['Quantity:', quantity, 'Measurement:', measurement, 'Ingredient:', food])

	return ingredients_data




def ingredient_analysis(start_url):
	analysis_res = []
	ingredients_list = scrape_ingredients(start_url)
	recipe_list = scrape_instructions(start_url)
	extracted_ingredients = get_ingredients_data(ingredients_list)

	for ingredient_list in extracted_ingredients:
		descriptor = []
		preparation = []
		food_list = ingredient_list[-1]
		text = nltk.word_tokenize(food_list)
		for tag in nltk.pos_tag(text):
			if tag[1] == 'JJ':
				descriptor.append(tag[0])
			if tag[1] == 'VBN':
				preparation.append(tag[0])
		analysis_res.append(['Recipes:', ingredient_list, 'Descriptor:', descriptor, 'Preparation:', preparation])
	analysis_res.append(['Primary Methods:', extractMethods(recipe_list)])
	analysis_res.append(['Tools:', makeToolsList(start_url)])
	return analysis_res


start_url = 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%203'
analysis_res = ingredient_analysis(start_url)



with open('data.json', 'w') as outfile:
	for i in analysis_res:
		print(i)
		json.dump(i, outfile)

