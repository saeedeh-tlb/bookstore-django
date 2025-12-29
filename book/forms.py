from django import forms
from book.models import Book


class CreateBook(forms.Form):
    class Meta:
        model = Book
        fields = "__all__"