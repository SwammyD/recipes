from recipe_scraper import *

ingredients = scrape_ingredients('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades')
recipe = scrape_instructions('https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades')


substitutions = [
	['milk', 'almond milk'],
	['cottage cheese', 'crumbled tofu'],
	['ricotta cheese', 'soaked raw nuts'],
	['scrambled eggs', 'tofu scramble'],
	['eggs', 'pureed soft tofu'], #for baking
	['eggs', 'soy flour'], # when eggs are a binding agent
	['beef stock', 'vegetable broth'],
	['chicken stock', 'vegetable broth'],
	['butter', 'vegan butter'], # if available
	['butter', 'sunflower oil'],
	['yogurt', 'vegan yogurt'], #it is a thing, apparently
	['sour cream', 'non-dairy yogurt'],
	['mayonnaise', 'vegan mayo'],
	['gelatin', 'agar flakes'],
	['honey', 'maple syrup'], # or agave nectar. Also, HONEY ISN'T VEGAN?!
	['sugar', 'beet sugar'],
	['chocolate', 'vegan chocolate'],
	['bologna', 'veggie deli slices'],
	['beef', 'tofu'], # these might also be veggie deli slices depending on what is being made.
	['turkey', 'tofu'], #if we are making a sandwich, it is probably going to be veggie deli slices
	['ham', 'tofu'],
	['ice cream', 'sorbet']
]


def makeVegan( ingredients, recipe ):
	for sub in substitutions:
		for n, ingredient in enumerate(ingredients):
			if sub[0] in ingredient:
				for word in ingredient.split():
					if word == sub[0]:
						ingredient = ingredient.replace(word, sub[0])
						ingredients[n] = ingredient
	print(ingredients)