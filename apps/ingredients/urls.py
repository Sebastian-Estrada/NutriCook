from django.urls import path
from .views import (
    IngredientListView, IngredientCreateView, IngredientUpdateView,
    CategoryListView, CategoryCreateView, CategoryUpdateView
)

app_name = 'ingredients'

urlpatterns = [
    # Ingredient URLs
    path('ingredient/list/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient/create/', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredient/update/<int:pk>/', IngredientUpdateView.as_view(), name='ingredient_update'),

    # Category URLs
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
]
