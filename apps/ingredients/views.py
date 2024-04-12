from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from apps.core.mixins import MessageMixin

from .models import Ingredient, Category
from .forms import (
    IngredientForm, IngredientUpdateForm,
    CategoryForm, CategoryUpdateForm
)

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'ingredients/ingredient_list.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class IngredientCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredients/ingredient_create.html'
    success_url = reverse_lazy('ingredient_list')


class IngredientUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = 'ingredients/ingredient_update.html'
    success_url = reverse_lazy('ingredient_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'ingredients/category/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'ingredients/category/category_create.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'ingredients/category/category_update.html'
    success_url = reverse_lazy('category_list')