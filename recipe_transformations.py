import recipe_scraper, re

# input recipe url
url = 'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/?internalSource=streams&referringId=95&referringContentType=recipe%20hub&clickId=st_recipes_mades'

ingredients_list = recipe_scraper.scrape_ingredients(url)
instructions_list = recipe_scraper.scrape_instructions(url)

print(ingredients_list)
print(instructions_list)

