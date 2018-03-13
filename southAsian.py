import recipe_scraper, re
from nltk import *
from textblob import TextBlob
import os
from stanfordcorenlp import StanfordCoreNLP


java_path = "C:/Program Files/Java/jdk1.8.0_151/bin/java.exe"
os.environ['JAVAHOME'] = java_path
#nlp = StanfordCoreNLP(r'C:\StanfordPOS\stanford-corenlp-full-2018-02-27')


urls = [
	['https://www.allrecipes.com/recipe/21340/lindas-lasagna/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202'],
	['https://www.allrecipes.com/recipe/223042/chicken-parmesan/?internalSource=streams&referringId=201&referringContentType=recipe%20hub&clickId=st_recipes_mades'],
	['https://www.allrecipes.com/recipe/231523/pork-lo-mein/?internalSource=staff%20pick&referringId=1014&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/255259/homemade-chili/?internalSource=staff%20pick&referringId=92&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/231523/pork-lo-mein/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=255259%20referringContentType%3Drecipe'],
	['https://www.allrecipes.com/recipe/14685/slow-cooker-beef-stew-i/?internalSource=hub%20recipe&referringId=200&referringContentType=recipe%20hub']
]

my_url = urls[1][0]
ingredients_list = recipe_scraper.scrape_ingredients(my_url)
recipe_list = recipe_scraper.scrape_instructions(my_url)



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
	'lean ground beef': 'lean ground turkey',
	'dried oregano': 'dried cumin',
	'chopped fresh basil': 'chopped fresh cilantro'
	#'shredded cheddar cheese': 'paneer'
}

methods = {
	'drain': 'boiling',
	'bake': 'baking',
	'baking': 'baking',
	'simmer': 'simmering',
	'simmering': 'simmering',
	'bring': 'boiling',
	'caramelize': 'caramelizing',
	'whisk': 'beating',
	'blend': 'blending'
}

descriptors = [
	'chopped',
	'minced',
	'cut',
	'or',
	'sliced',
	'rinsed',
	'diced'
]


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
						step = re.sub(item.split()[n], swaps[item].split()[n], step)
		new_recipe.append(step)
	print(recipe)
	print('\n')
	print(new_recipe)

	return ingredients


def getIngredient(ingredients):
	parsed_ingredients = []
	ingredient = []
	for words in ingredients:
		food = ''
		quantity = []
		measurement = []
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


	return parsed_ingredients



def extractMethods(recipe):
	methods_list = []

	for step in recipe:
		tagged_text = nlp.pos_tag(step)
		for item in tagged_text:
			if item[1][0] == 'V':
				lowercase_item = item[0].lower()
				if lowercase_item in methods:
					methods_list.append(methods[lowercase_item])

	return methods_list


#print(extractMethods(recipe_list))



extracted_ingredients = getIngredient(ingredients_list)
#print(extracted_ingredients)
print(makeSouthAsian(extracted_ingredients, recipe_list))



#depreciated version of Stanford POS tagger - might be useful

# stanford_classifier = 'C:\StanfordPOS\stanford-postagger-2018-02-27\models\english-bidirectional-distsim.tagger'
# stanford_ner_path = 'C:\StanfordPOS\stanford-postagger-2018-02-27\stanford-postagger.jar'
# st = StanfordPOSTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

# text = word_tokenize(recipe_list[4])
# classified = st.tag(text)
# print(classified)