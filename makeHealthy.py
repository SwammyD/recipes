from recipe_scraper import *
from fractions import Fraction


#recipe = 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'


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
	['sausage', 'turkey sausage'],
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



# DONE
def makeHealthyIngredients( recipe ):
	full_ingredients = scrape_ingredients(recipe)
	ingredients = get_ingredients_data(full_ingredients)
	for fat in fats:
		for n, ingredient in enumerate(ingredients):
			if 'cheese' in ingredient[2] and 'low-fat' not in ingredient[2]:
				ingredient[2] = 'low-fat ' + ingredient[2]
				ingredients[n] = ingredient
			elif fat[0] in ingredient[2] and 'lean' not in ingredient[2]:
				ingredient[2] = fat[1]
				ingredients[n] = ingredient

	for carb in carbs:
		for n, ingredient in enumerate(ingredients):
			if carb[0] in ingredient[2]:
				ingredient[2] = carb[1]
				ingredients[n] = ingredient
	reduceProportions(ingredients)
	
	print("ingredients:")
	
	for ingr in ingredients:
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

#DONE
def makeHealthyRecipe( recipe ):
	instructions = scrape_instructions(recipe)
	for fat in fats:
		for x, step in enumerate(instructions):
			if fat[0] in step and 'lean ground' not in step:
				step = step.replace(fat[0], fat[1])
				instructions[x] = step

	for carb in carbs:
		for n, step in enumerate(instructions):
			if carb[0] in step:
				step = step.replace(carb[0], carb[1])
				instructions[n] = step

	print(instructions)

#DONE
def reduceProportions( ingredients ):
	for x, ingredient in enumerate(ingredients):
		if 'sugar' in ingredient[2] or 'salt' in ingredient[2]:
			new_amt = ingredient[0]/2
			ingredient[0] = new_amt
			ingredients[x] = ingredient
	#print(ingredients)

#DONE
def makeUnhealthyIngredients( recipe ):
	full_ingredients = scrape_ingredients(recipe)
	ingredients = get_ingredients_data(full_ingredients)
	for fat in fats:
		for n, ingredient in enumerate(ingredients):
			if fat[1] in ingredient[2]:
				ingredient[2] = fat[0]
				ingredients[n] = ingredient

	for carb in carbs:
		for n, ingredient in enumerate(ingredients):
			if carb[1] in ingredient[2]:
				ingredient[2] = carb[0]
				ingredients[n] = ingredient
	
	print("ingredients:")
	
	for ingr in ingredients:
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

#DONE
def makeUnhealthyRecipe( recipe ):
	instructions = scrape_instructions(recipe)
	for fat in fats:
		for x, step in enumerate(instructions):
			if fat[1] in step:
				step = step.replace(fat[1], fat[0])
				instructions[x] = step

	for carb in carbs:
		for n, step in enumerate(instructions):
			if carb[1] in step:
				step = step.replace(carb[1], carb[0])
				instructions[n] = step
	print(instructions)

