import recipe_scraper, re
from nltk import *
from textblob import TextBlob
import os
from stanfordcorenlp import StanfordCoreNLP


java_path = "C:/Program Files/Java/jdk1.8.0_151/bin/java.exe"
os.environ['JAVAHOME'] = java_path

url = 'https://www.allrecipes.com/recipe/34942/cheesy-italian-tortellini/'

ingredients_list = recipe_scraper.scrape_ingredients(url)
recipe_list = recipe_scraper.scrape_instructions(url)


substitutions = {
	'Italian seasoning': 'paprika',
	'dry red wine': 'olive oil',
	'red wine': 'olive oil',
	'sweet Italian sausage': 'turkey sausage',
	'ground beef': 'ground lamb',
	'pork chops': 'lamb chops',
	'ham': 'lamb',
	'pork tenderloin': 'lamb tenderloin',
	'pork': 'lamb',
	'bacon': 'turkey bacon',
	'pork loin': 'lamb loin',
	'pork loin roast': 'lamb loin roast',
	'soy sauce': 'chili sauce',
	'Parmesan cheese': 'paneer',
	'bow tie pasta': 'basmati rice',
	'minced fresh parsley': 'cilantro',
	'Italian sausage': 'turkey sausage',
	'shredded cheddar cheese': 'paneer'
}


def makeSouthAsian(ingredients, recipe):
	swaps = {}
	new_recipe = []
	# in theory this should work once we parse exact ingredients
	for n, ingredient in enumerate(ingredients):
		ingredient = ingredient.lower()
		if ingredient in substitutions:
			ingredients[n] = substitutions[ingredient]
			swaps[ingredient] = substitutions[ingredient]

	for step in recipe:
		for item in swaps:
			for n, part in enumerate(item.split()):
				if part in step:
					if n > len(swaps[item].split()):
						step = re.sub(item.split()[n], swaps[item], step)
					else:
						step = re.sub(item.split()[n], swaps[item], step)
		new_recipe.append(step)
	print(recipe)
	print('\n')
	print(new_recipe)

	# for spice in spices:
	# 	for n, ingredient in enumerate(ingredients):
	# 		if spice[0] in ingredient:
	# 			m = re.sub(spice[0], spice[1], ingredient)
	# 			ingredients[n] = m
						

	return ingredients

def getIngredient(ingredients):
	extracted_ingredients = [];

	for n, ingredient in enumerate(ingredients):
		token = word_tokenize(ingredient)
		if ',' in token:
			comma_index = token.index(',')
			current_ingredient = ' '.join(token[2:comma_index])
		elif len(token) < 3:
			curr_ingredient = ingredient
		elif token[1] == '(':
			current_ingredient = ' '.join(token[6:])
		else:
			current_ingredient =' '.join(token[2:])

		extracted_ingredients.append(current_ingredient)

	return extracted_ingredients



extracted_ingredients = getIngredient(ingredients_list)
#print(extracted_ingredients)
print(makeSouthAsian(extracted_ingredients, recipe_list))








# nlp = StanfordCoreNLP(r'C:\StanfordPOS\stanford-corenlp-full-2018-02-27')
# text = recipe_list[2]
# print(nlp.pos_tag(text))









# depreciated version of Stanford POS tagger - might be useful

# stanford_classifier = 'C:\StanfordPOS\stanford-postagger-2018-02-27\models\english-bidirectional-distsim.tagger'
# stanford_ner_path = 'C:\StanfordPOS\stanford-postagger-2018-02-27\stanford-postagger.jar'
# st = StanfordPOSTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

# text = word_tokenize(recipe_list[4])
# classified = st.tag(text)
# print(classified)