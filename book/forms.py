from django import forms

from .models import *

class NewBookForm(forms.ModelForm):
    model = Book
    fields = ['title', 'author', 'cover', 'document']
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'cover': forms.FileInput(attrs={'class': 'form-control'}),
        'document': forms.FileInput(attrs={'class': 'form-control'})
    }

