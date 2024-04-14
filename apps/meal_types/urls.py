from django.urls import path
from .views import MealTypeListView, MealTypeCreateView, MealTypeUpdateView

app_name = 'meal_types'

urlpatterns = [
    path('list/', MealTypeListView.as_view(), name='meal_type_list'),
    path('create/', MealTypeCreateView.as_view(), name='meal_type_create'),
    path('<int:pk>/update/', MealTypeUpdateView.as_view(), name='meal_type_update'),
]
