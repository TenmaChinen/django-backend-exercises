# Chapter 1
import dj_scope

########################################
#####   4 Update Sci-Fi Category   #####
########################################

from bookstores.models import Category

queryset = Category.objects.filter(id=5)

if queryset.exists():
    category = queryset.first()
    category.name = 'Science-Fiction'
    category.save()
else:
    print('No Exists')


for category in Category.objects.all():
    print(category.name)

'''
    Fantasy
    Mystery
    Horror
    Adventure
    Science-Fiction
'''