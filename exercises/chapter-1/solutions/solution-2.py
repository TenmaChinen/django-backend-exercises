# Chapter 1
import dj_scope

######################################
####   2 Saving Book Categories   ####
######################################

from bookstores.models import Category
import json

file = open('data.json', 'r')
data = json.load(file)
file.close()

for category_data in data['categories']:
    category = Category()
    category.id = category_data['id']
    category.name = category_data['name']
    category.save()