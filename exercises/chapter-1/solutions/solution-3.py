# Chapter 1
import dj_scope

########################################
####   3 Display Saved Categories   ####
########################################

from bookstores.models import Category

queryset = Category.objects.all()

for category in queryset:
    print('Id :',category.id, ' | Name :', category.name)

'''
    Id : 1  | Name : Fantasy
    Id : 2  | Name : Mystery
    Id : 3  | Name : Horror
    Id : 4  | Name : Adventure
    Id : 5  | Name : Sci-Fi
'''