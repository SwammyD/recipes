import recipe_scraper, re
import southAsian
from makeHealthy import *
from make_vegetarian import *
from ingredient_analysis import analyzeIngredients
# import make_vegetarian, tools_list
# import makeHealthy, southAsian, ingredients

# input recipe url
url = 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'

ingredients_list = recipe_scraper.scrape_ingredients(url)
instructions_list = recipe_scraper.scrape_instructions(url)

print("Transformation options:")
print("1: To and from vegetarian")
print("2: To and from healthy")
print("3: To south asian")
transformation_type = int(input("Please select your transformation type: "))
recipe_url = input("Please input your recipe url: ")

ingredients_list = recipe_scraper.scrape_ingredients(str(recipe_url))
instructions_list = recipe_scraper.scrape_instructions(str(recipe_url))

if transformation_type == 1:
	makeVegetarian(recipe_url)
elif transformation_type == 2:
	healthy_type = int(input("Please select either healthy (1) or unhealthy (2): "))
	if healthy_type == 1:
		makeHealthyIngredients(recipe_url)
		makeHealthyRecipe(recipe_url)
	elif healthy_type == 2: 
		makeUnhealthyIngredients(recipe_url)
		makeUnhealthyRecipe(recipe_url)
elif transformation_type == 3:
	southAsian.makeSouthAsian(ingredients_list, instructions_list, url)

# analyzes original recipe and dumps into json file
analysis_res = analyzeIngredients(recipe_url)
with open('data.json', 'w') as outfile:
	for i in analysis_res:
		json.dump(i, outfile)