import bs4
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


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


#print(scrape_instructions('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'))