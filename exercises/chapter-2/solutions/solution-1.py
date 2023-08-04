# Chapter 2
import dj_scope

##################################################################
##########   1 Save Book JSON data to Django database   ##########
##################################################################

from bookstores.models import Author, Book
import json

file = open('data.json', 'r')
data = json.load(file)
file.close()

l_books = data['books']

for book_data in l_books:
    book = Book()
    book.id = book_data['id']
    book.title = book_data['title']

    author_id = book_data['author']
    author = Author.objects.get(id=author_id)
    book.author = author
    book.save()

for book in Book.objects.all():
    print(f'Id : {book.id} | Title : {book.title}')