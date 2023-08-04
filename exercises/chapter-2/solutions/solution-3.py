# Chapter 2
import dj_scope

####################################################################
########   3 Update Category Foreign field from each Book   ########
####################################################################

from bookstores.models import Book, Category
import json

file = open('data.json', 'r')
data = json.load(file)
file.close()

l_books = data['books']

for book_data in l_books:
    queryset = Book.objects.filter( id = book_data['id'] )
    if queryset.exists():
        book = queryset.first()

        l_categories = book_data['categories']
        queryset = Category.objects.filter( id__in = l_categories )
        
        if queryset.exists():
            book.category.set(queryset)
            book.save()


for book in Book.objects.all():
    print(f'\nTitle : {book.title}')
    l_categories = [ category.name for category in book.category.all() ]
    print(l_categories)