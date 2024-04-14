from django.urls import path
from .views import (
    RecipeListView, RecipeCreateView, RecipeUpdateView,
    RecipeIngredientListView, RecipeIngredientCreateView,
    RecipeIngredientUpdateView
)

app_name = 'recipes'

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('update/<int:pk>/', RecipeUpdateView.as_view(), name='recipe_update'),

    path('recipe/<int:pk>/ingredients/', RecipeIngredientListView.as_view(), name='recipe_ingredient_list'),
    path('recipe/<int:recipe_pk>/ingredients/add/', RecipeIngredientCreateView.as_view(), name='recipe_ingredient_create'),
    path('recipe/<int:recipe_pk>/ingredients/<int:pk>/update/', RecipeIngredientUpdateView.as_view(), name='recipe_ingredient_update'),

]
