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


'''
if re.search('\(', words):
    print(words)
    # get rid of trademark
        words = re.sub('\(R\)', '', words)
        # get rid of other parentheses
        words = re.sub(r'\s\([^)]*\)', '', words)
        print(words)
'''
def decompose_ingredient(start_url):
    food = ''
    quantity = []
    measurement = []
    ingredient = []
    data = ingredients_data(start_url)
    for i in data:
        for words in i[2]:
            if re.search('\(', words):
                words = re.sub('\(R\)', '', words)
                #get rid of other parens
                words = re.sub(r'\s\([^)]*\)', '', words)
            words_list = words.split()
            for word in words_list:
                if re.search('[1-9]', word) or re.search('[1-9]\/[1-9]', word) or re.search('\([1-9]+ [a-z]+\)', word):
                    quantity.append(word)
                elif word in ['teaspoon', 'teaspoons', 'cup', 'cups', 'pound', 'pounds', 'tablespoon', 'tablespoons']:
                    measurement.append(word)
                else:
                    food = food + ' ' +  word
            ingredient.append(food)
            food = ''
    return quantity, measurement, ingredient



#get_ingredient = decompose_ingredient('https://www.allrecipes.com/recipe/13883/manicotti/?internalSource=rotd&referringId=95&referringContentType=recipe%20hub')
#print(get_ingredient)
q, m, i = decompose_ingredient('https://www.allrecipes.com/recipe/13883/manicotti/?internalSource=rotd&referringId=95&referringContentType=recipe%20hub')
#print(q[1])
#print(m[1])
#print(i[1])