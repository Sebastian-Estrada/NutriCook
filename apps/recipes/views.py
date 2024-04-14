from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_create.html'
    success_url = reverse_lazy('recipes:recipe_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_update.html'
    success_url = reverse_lazy('recipes:recipe_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeIngredientListView(LoginRequiredMixin, ListView):
    model = RecipeIngredient
    template_name = 'recipes/recipe_ingredient/recipe_ingredient_list.html'
    context_object_name = 'recipe_ingredients'

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_pk = self.kwargs.get('pk')
        if recipe_pk:
            queryset = queryset.filter(recipe_id=recipe_pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_pk = self.kwargs.get('pk')
        context["recipe"] = get_object_or_404(Recipe, pk=recipe_pk)
        return context

class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    model = RecipeIngredient
    form_class = RecipeIngredientForm
    template_name = 'recipes/recipe_ingredient/recipe_ingredient_create.html'

    def form_valid(self, form):
        recipe_pk = self.kwargs.get('recipe_pk')
        form.instance.recipe_id = recipe_pk
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_pk = self.kwargs.get('recipe_pk')
        context["recipe"] = get_object_or_404(Recipe, pk=recipe_pk)
        return context

    def get_success_url(self):
        recipe_pk = self.kwargs.get('recipe_pk')
        return reverse_lazy('recipes:recipe_ingredient_list', kwargs={'pk': recipe_pk})


class RecipeIngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeIngredient
    form_class = RecipeIngredientForm
    template_name = 'recipes/recipe_ingredient/recipe_ingredient_update.html'

    def get_success_url(self):
        recipe_pk = self.kwargs.get('recipe_pk')
        return reverse_lazy('recipes:recipe_ingredient_list', kwargs={'pk': recipe_pk})
