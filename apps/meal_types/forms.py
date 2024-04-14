from django import forms
from .models import MealType

class MealTypeForm(forms.ModelForm):
    class Meta:
        model = MealType
        fields = ['name', 'description']
        labels = {
            'name': 'Name',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
