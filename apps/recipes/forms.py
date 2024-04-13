from django import forms
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget

from apps.cuisine_types.models import CuisineType
from apps.ingredients.models import Ingredient

from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    cuisine_type = forms.ModelChoiceField(
        queryset=CuisineType.objects.all(),
        empty_label='Select cuisine type',
        widget=ModelSelect2Widget(
            model=CuisineType,
            search_fields=['name__icontains'],
            attrs={'data-minimum-input-length': ''}
        )
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'author', 'cuisine_type', 'active']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'author': 'Author',
            'cuisine_type': 'Cuisine Type',
            'active': 'Active'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'ingredients': ModelSelect2MultipleWidget(model=Ingredient, queryset=Ingredient.objects.all(), search_fields=['name__icontains'],attrs={'data-minimum-input-length': ''}),
        }


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']
        labels = {
            'ingredient': 'Ingredient',
            'quantity': 'Quantity',
            'unit': 'Unit'
        }
