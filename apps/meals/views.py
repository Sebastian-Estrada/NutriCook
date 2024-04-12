from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal
from .forms import MealForm

class MealListView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = 'meals/meal_list.html'
    context_object_name = 'meals'

class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'meals/meal_form.html'
    success_url = '/meals/'

class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = MealForm
    template_name = 'meals/meal_form.html'
    success_url = '/meals/'
