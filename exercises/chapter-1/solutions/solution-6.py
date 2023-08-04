# Chapter 1
import dj_scope

#################################################
#####   6 Delete Science-Fiction Category   #####
#################################################

from bookstores.models import Author
import json

file = open('data.json', 'r')
data = json.load(file)
file.close()

l_authors = data['authors']

for author_data in l_authors:
    author = Author( **author_data )
    author.save()

queryset = Author.objects.all()

for author in queryset:
    print(f'ID : {author.id} | Name : {author.name}')