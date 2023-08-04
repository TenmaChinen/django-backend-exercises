import dj_setup

from bookstores.models import Book, Author, Category

Book.objects.all().delete()
Author.objects.all().delete()
Category.objects.all().delete()