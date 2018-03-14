import recipe_scraper, re

# input recipe url
url = 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'

ingredients_list = recipe_scraper.scrape_ingredients(url)
instructions_list = recipe_scraper.scrape_instructions(url)


def makeVegetarian(ingredients):

    meat_keywords = ['beef', 'pork', 'chicken', 'turkey', 'quail' 'ham', 'veal', 'lamb', 'mutton', 'sausage', 'duck']

    # search thru ingredients and replace any meat with tofu
    # TODO: update cooking methods in instructions
    # TODO: edit adjectives and measurements?
    for i in range(len(ingredients)):
        for meat in meat_keywords:
            if meat in ingredients[i]:
                ingredients[i] = re.sub(meat, 'tofu', ingredients[i])
                print("here")

    return ingredients

veg_ingredients = makeVegetarian(ingredients_list)

print(veg_ingredients)
print(instructions_list)

