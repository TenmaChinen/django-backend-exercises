from bookstores.models import Author, Category, Book
from django import forms


class FormAuthor(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class FormCategory(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class FormBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'