from django import forms
from django_select2.forms import Select2Widget

from .models import Ingredient, Category

class IngredientForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=Select2Widget
    )

    class Meta:
        model = Ingredient
        fields = ['name', 'description', 'category', 'active']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'category': 'Category',
            'active': 'Active'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class IngredientUpdateForm(IngredientForm):
    class Meta(IngredientForm.Meta):
        fields = ['name', 'description', 'category', 'active']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'active']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'active': 'Active'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class CategoryUpdateForm(CategoryForm):
    class Meta(CategoryForm.Meta):
        fields = ['name', 'description', 'active']
