from django import forms
from .models import CuisineType

class CuisineTypeForm(forms.ModelForm):
    class Meta:
        model = CuisineType
        fields = ['name', 'description']
        labels = {
            'name': 'Name',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }