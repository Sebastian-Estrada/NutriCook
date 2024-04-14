from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('meals:meal_list')

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user = self.request.user
        meal.save()
        return super().form_valid(form)


class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = MealForm
    template_name = 'meals/meal_form.html'
    success_url = reverse_lazy('meals:meal_list')
