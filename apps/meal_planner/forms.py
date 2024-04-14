from django import forms
from django_select2.forms import ModelSelect2MultipleWidget

from apps.meals.models import Meal

from .models import MealPlan


class PlannerForm(forms.ModelForm):
    meals = forms.ModelMultipleChoiceField(
        queryset=Meal.objects.all(),
        widget=ModelSelect2MultipleWidget(
            model=Meal,
            attrs={
                'data-placeholder': 'Select meals', 'data-minimum-input-length': ''
            },
            search_fields=['name__icontains'],
        ),
        required=False,
        label='Meals'
    )

    class Meta:
        model = MealPlan
        fields = ['name', 'date', 'meals']
        labels = {
            'name': 'Name',
            'date': 'Meal Date',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
