from django import forms
from .models import *

# Model Form for AdminBooks
class NewCatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = ['authors', 'book_title', 'isbn', 'book_id', 'description', 'edition', 'quantity', 'image', 'category']
        widgets = {
            'authors': forms.TextInput(attrs={'class': 'form-control'}),
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.NumberInput(attrs={'class': 'form-control'}),
            'book_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows':2, 'maxlength': 1000, 'class': 'form-control'}),
            'edition': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'image': 'Image File'
        }



class ReviewForm(forms.ModelForm):
    class Meta:
        model = CatalogueReview
        fields = ['review']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'maxlength': '5000'})
        }
