
from django.urls import path
from .views import MealListView, MealCreateView, MealUpdateView

app_name = 'meals'

urlpatterns = [
    path('list/', MealListView.as_view(), name='meal_list'),
    path('create/', MealCreateView.as_view(), name='meal_create'),
    path('<int:pk>/update/', MealUpdateView.as_view(), name='meal_update'),
]