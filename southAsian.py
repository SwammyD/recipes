import recipe_scraper, re
from nltk import *
from textblob import TextBlob
import os
from stanfordcorenlp import StanfordCoreNLP


java_path = "C:/Program Files/Java/jdk1.8.0_151/bin/java.exe"
os.environ['JAVAHOME'] = java_path
nlp = StanfordCoreNLP(r'C:\StanfordPOS\stanford-corenlp-full-2018-02-27')


urls = [
	['https://www.allrecipes.com/recipe/21340/lindas-lasagna/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202'],
	['https://www.allrecipes.com/recipe/223042/chicken-parmesan/?internalSource=streams&referringId=201&referringContentType=recipe%20hub&clickId=st_recipes_mades'],
	['https://www.allrecipes.com/recipe/231523/pork-lo-mein/?internalSource=staff%20pick&referringId=1014&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/255259/homemade-chili/?internalSource=staff%20pick&referringId=92&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/231523/pork-lo-mein/?clickId=right%20rail1&internalSource=rr_feed_recipe_sb&referringId=255259%20referringContentType%3Drecipe'],
	['https://www.allrecipes.com/recipe/14685/slow-cooker-beef-stew-i/?internalSource=hub%20recipe&referringId=200&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/12897/white-chili-i/?internalSource=staff%20pick&referringId=17021&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/240583/cheesy-ham-and-corn-chowder/?internalSource=staff%20pick&referringId=205&referringContentType=recipe%20hub'],
	['https://www.allrecipes.com/recipe/255865/slow-cooker-thai-curried-beef/?internalSource=staff%20pick&referringId=92&referringContentType=recipe%20hub']
]

my_url = urls[4][0]
ingredients_list = recipe_scraper.scrape_ingredients(my_url)
recipe_list = recipe_scraper.scrape_instructions(my_url)



substitutions = {
	'Italian seasoning': 'paprika',
	'dry red wine': 'olive oil',
	'red wine': 'olive oil',
	'sweet Italian sausage': 'turkey sausage',
	'ground beef': 'ground lamb',
	'ground pork': 'ground lamb',
	'pork chops': 'lamb chops',
	'ham': 'lamb',
	'pork tenderloin': 'lamb tenderloin',
	'pork': 'lamb',
	'bacon': 'turkey bacon',
	'pork loin': 'lamb loin',
	'pork loin roast': 'lamb loin roast',
	'soy sauce': 'chili sauce',
	'bow tie pasta': 'basmati rice',
	'minced fresh parsley': 'cilantro',
	'Italian sausage': 'turkey sausage',
	'lean ground beef': 'lean ground turkey',
	'dried oregano': 'dried cumin',
	'chopped fresh basil': 'chopped fresh cilantro',
	'low-sodium soy sauce': 'chili sauce',
	'linguine': 'rice',
	'great northern beans': 'chickpeas',
	'dried marjoram': 'fenugreek',
	'diced cooked ham': 'diced cooked lamb',
	'lean stew beef': 'lean stew lamb',
	'beef broth': 'lamb broth',
	'jasmine rice': 'basmati rice',
	'fresh basil leaves': 'fresh cilantro leaves'
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
	'blend': 'blending',
	'saute': 'sauteing',
	'slow': 'slow cook',
	'pressure': 'pressure cook'
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
	new_recipe = recipe

	for n, ingredient in enumerate(ingredients):
		ingredient = ingredient.lower()
		if ingredient in substitutions:
			ingredients[n] = substitutions[ingredient]
			swaps[ingredient] = substitutions[ingredient]

	for n, step in enumerate(new_recipe):
		for item in swaps:
			split_item = item.split()
			if len(split_item) > 1:
				without_first = ' '.join(split_item[1:])
			last_word = split_item[-1]
			first_word = split_item[0]

			# check if entire item is in step
			re_obj = re.search(item, step)
			if re_obj:
				step = re.sub(item, swaps[item], step)

			# check if all but first word is in step
			elif re.search(without_first, step):
				step = re.sub(without_first, swaps[item], step)

			# check if last word is in step
			elif re.search(last_word, step):
				step = re.sub(last_word, swaps[item], step)

			elif (len(split_item) < 3):
				if re.search(first_word, step):
					step = re.sub(first_word, swaps[item].split()[0], step)


		new_recipe[n] = step

	# print(new_recipe)

	return ingredients, new_recipe






def extractMethods(recipe):
	methods_list = []

	for step in recipe:
		# tagged_text = nlp.pos_tag(step)
		# for item in tagged_text:
		# 	if item[1][0] == 'V':
		# 		#print(item)
		# 		lowercase_item = item[0].lower()
		# 		if lowercase_item in methods:
		# 			methods_list.append(methods[lowercase_item])

		words = step.split()
		for word in words:
			stripped_word = word.replace(',', '')
			stripped_word = stripped_word.replace('.', '')
			if stripped_word.lower() in methods:
				methods_list.append(methods[stripped_word.lower()])

	return methods_list


print(extractMethods(recipe_list))



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