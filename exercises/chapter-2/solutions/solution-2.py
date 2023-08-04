# Chapter 2
import dj_scope

############################################################################
##########   2 Get Book Categories ( ManyToMany Foreign Field )   ##########
############################################################################

from bookstores.models import Book, Category
import json

file = open('data.json', 'r')
data = json.load(file)
file.close()

l_books = data['books']

for book_data in l_books:

    l_categories = book_data['categories']
    queryset = Category.objects.filter( id__in = l_categories )
    print(book_data['title'])
    for category in queryset:
        print('\t',category.name)