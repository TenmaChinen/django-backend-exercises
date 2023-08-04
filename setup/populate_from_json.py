import dj_scope

from foos.models import Author, Book
import json

file = open('data.json', 'r')
l_data = json.load(file)
file.close()

for d_author in l_data:

    author = Author( first_name=d_author['first_name'], last_name=d_author['last_name'])
    author.save()
        
    for d_book in d_author['books']:
        book = Book( author=author, **d_book )
        book.save()
