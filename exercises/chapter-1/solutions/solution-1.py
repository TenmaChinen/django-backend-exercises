# Chapter 1
import dj_scope

#####################################
##########   1 JSON Data   ##########
#####################################

import json

file = open('data.json', 'r')
data = json.load(file)
file.close()


for category_data in data['categories']:
    print(category_data)