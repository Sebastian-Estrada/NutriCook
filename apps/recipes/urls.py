from django.urls import path
from .views import (
    RecipeListView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView
)

app_name = 'recipes'

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('update/<int:pk>/', RecipeUpdateView.as_view(), name='recipe_update'),
]
