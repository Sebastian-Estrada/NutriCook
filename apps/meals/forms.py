from django import forms
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget

from .models import Meal

from apps.meal_types.models import MealType
from apps.recipes.models import Recipe

class MealForm(forms.ModelForm):
    meal_type = forms.ModelChoiceField(
        queryset=MealType.objects.all(),
        empty_label='Select meal type',
        widget=ModelSelect2Widget(
            model=MealType,
            search_fields=['name__icontains'],
            attrs={'data-minimum-input-length': ''}
        )
    )

    recipes = forms.ModelMultipleChoiceField(
        queryset=Recipe.objects.all(),
        required=True,
        widget=ModelSelect2MultipleWidget(
            model=Recipe,
            search_fields=['name__icontains'],
            attrs={'data-minimum-input-length': ''}
        )
    )

    class Meta:
        model = Meal
        fields = ['name', 'meal_type', 'recipes', 'active']
        labels = {
            'name': 'Name',
            'meal_type': 'Meal Type',
            'recipes': 'Recipes',
            'active': 'Active'
        }
