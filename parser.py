# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_html(link):
    html = urlopen(link)
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    #print(bsObj.prettify())
    return bsObj

def ingredients_data(start_url):
    data = []
    recipe_link = set()
    allrecipes = get_html(start_url)
    for link in allrecipes.find_all('a'):
        if str(link.get('href')).startswith('https://www.allrecipes.com/recipe/'):
            recipe_link.add(link.get('href'))

    for link in list(recipe_link):
        soup = get_html(link)
        #print(url.prettify())
        ingredients = []
        for li in soup.find_all('li'):
            if 'checkList__line' in str(li):
                ingredient = re.search('title="(.*)"', str(li))
                if ingredient:
                    ingredients.append(ingredient.group(0)[7:-1])
        data.append([soup.title.string, link, ingredients])
    return data

data = ingredients_data("https://www.allrecipes.com/recipes/")
for i in data:
    print(i)


