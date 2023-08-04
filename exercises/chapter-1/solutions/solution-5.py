# Chapter 1
import dj_scope

#################################################
#####   5 Delete Science-Fiction Category   #####
#################################################

from bookstores.models import Category

queryset = Category.objects.filter(name='Science-Fiction')

if queryset.exists():
    category = queryset.first()
    category.delete()
    print('Deleted!')
else:
    print('Record not found!')

for category in Category.objects.all():
    print(category.name)
