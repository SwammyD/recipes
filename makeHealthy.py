import nltk


fats = [

	['bread', 'whole wheat bread'],
	['salted', 'unsalted'],
	['whole milk', 'milk'],
	['milk', 'low-fat milk'],
	['mayonnaise', 'low-fat cottage cheese'],
	['whipping cream', 'imitiation whipping cream'],
	['sour cream', 'plain low-fat yogurt'],
	['granola', 'bran flakes'],
	['beef', 'lean beef'],
	['cheese', 'low-fat cheese'],
	['bun', 'lettuce wrap'],
	['french fries', 'sweet potato fries'],
	['butter', 'olive oil'],
	['flour', 'whole wheat flour']

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

# example recipe that contains some of the words
recipe = 'Take the whole milk and eat some salted bread'
# should be transformed into 'Take the milk and eat some unsalted whole wheat bread'

# this will need to be changed based on how we define the recipe, 
# but the basic logic should remain the same
def makeHealthy( recipe ):
	for fat in fats:
		for word in recipe.split():
			if fat[0] in word:
				recipe = recipe.replace(word, fat[1])

	for carb in carbs:
		for word in recipe.split():
			if carb[0] in word:
				recipe = recipe.replace(word, carb[1])

	#reduceProportions(recipe)
	print(recipe)


def reduceProportions( recipe ):
	for ingredient in recipe['ingredients']:
		# will need to change based on actual parsing
		if ingredient['substance'] == 'sugar' or ingredient == 'butter':
			ingredient['amount'] = float(ingredient['amount'])
			ingredient['amount'] = int(ingredient['amount'] / 2)

makeHealthy(recipe)