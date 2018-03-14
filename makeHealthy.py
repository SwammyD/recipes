import nltk
from recipe_scraper import *
from fractions import Fraction
from ingredients import *

full_ingredients = scrape_ingredients('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades')
recipe = scrape_instructions('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades')

quantity, measurement, ingredients = decompose_ingredient('https://www.allrecipes.com/recipe/13883/manicotti/?internalSource=rotd&referringId=95&referringContentType=recipe%20hub')
print(len(quantity))
print(len(ingredients))
#print(recipe)

fats = [

	['bread', 'whole wheat bread'],
	['salted', 'unsalted'],
	['whole milk', 'milk'],
	['milk', 'low-fat milk'],
	['mayonnaise', 'low-fat cottage cheese'],
	['whipping cream', 'imitiation whipping cream'],
	['sour cream', 'plain low-fat yogurt'],
	['granola', 'bran flakes'],
	['ground beef', 'lean ground beef'],
	['beef', 'lean beef'],
	['bun', 'lettuce wrap'],
	['french fries', 'sweet potato fries'],
	['butter', 'olive oil'],
	['flour', 'whole wheat flour'],
	['bacon', 'canadian bacon'],
	['ground sausage', 'ground turkey'],
	['sausage', 'lean ham'],
	['eggs', 'egg substitutes'], # unless baking

]



carbs = [

	['hamburger buns', 'portabello mushrooms'],
	['mashed potatoes', 'cauliflower'],
	['potatoes', 'daikon'],	# or rutabaga
	['rice', 'cauliflower rice'],
	['lasagna', 'zucchini slices'],
	['spaghetti', 'spaghetti squash'],
	['pancakes', 'oatmeal pancakes'],
	['macaroni', 'diced vegetables (cauliflower)'],
	['bread', 'wheat bread'],
	['chips', 'carrots'],
	['trail mix', 'almonds']

]



# this will need to be changed based on how we define the recipe, 
# but the basic logic should remain the same
def makeHealthyIngredients( ingredients ):
	for fat in fats:
		for n, ingredient in enumerate(ingredients):
			if 'cheese' in ingredient and 'low-fat' not in ingredient:
				ingredient = 'low-fat' + ingredient
				ingredients[n] = ingredient
			elif fat[0] in ingredient and 'lean' not in ingredient:
				ingredient = fat[1]
				ingredients[n] = ingredient

	for carb in carbs:
		for n, ingredient in enumerate(ingredients):
			if carb[0] in ingredient:
				ingredient = carb[1]
				ingredients[n] = ingredient

	#reduceProportions(ingredients)
	print(ingredients)

def makeHealthyRecipe( recipe ):
	for fat in fats:
		for word in recipe.split():
			if fat[0] in word:
				recipe = recipe.replace(word, fat[1])

	for carb in carbs:
		for word in recipe.split():
			if carb[0] in word:
				recipe = recipe.replace(word, carb[1])

	#print(recipe)

def reduceProportions( ingredients ):
	for x, ingredient in enumerate(ingredients):
		if 'sugar' in ingredient or 'salt' in ingredient:
			new_amt = float(Fraction(ingredient.split()[0])/2)
			for y, word in enumerate(ingredient.split()):
				if y == 0:
					ingredient = ingredient.replace(word, str(new_amt))
					ingredients[x] = ingredient
	#print(ingredients)

def makeUnhealthyIngredients( ingredients ):
	for fat in fats:
		for n, ingredient in enumerate(ingredients):
			if fat[1] in word:
				ingredient = fat[0]
				ingredients[n] = ingredient

	for carb in carbs:
		for n, ingredient in enumerate(ingredients):
			if carb[1] in word:
				ingredient = ingredient.replace(word, carb[0])
				ingredients[n] = ingredient

def makeUnhealthyRecipe( recipe ):
	for fat in fats:
		for word in recipe.split():
			if fat[1] in word:
				recipe = recipe.replace(word, fat[0])

	for carb in carbs:
		for word in recipe.split():
			if carb[1] in word:
				recipe = recipe.replace(word, carb[0])

makeHealthyIngredients(ingredients)
# quantities do not break down fractions properly