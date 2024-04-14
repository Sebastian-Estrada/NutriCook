from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import MealType
from .forms import MealTypeForm

class MealTypeListView(LoginRequiredMixin, ListView):
    model = MealType
    template_name = 'meal_types/meal_type_list.html'
    context_object_name = 'meal_types'

class MealTypeCreateView(LoginRequiredMixin, CreateView):
    model = MealType
    form_class = MealTypeForm
    template_name = 'meal_types/meal_type_form.html'
    success_url = reverse_lazy('meal_types:meal_type_list')

class MealTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = MealType
    form_class = MealTypeForm
    template_name = 'meal_types/meal_type_form.html'
    success_url = reverse_lazy('meal_types:meal_type_list')
