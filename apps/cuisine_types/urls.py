from django.urls import path
from .views import CuisineTypeListView, CuisineTypeCreateView, CuisineTypeUpdateView

app_name = 'cuisine_types'

urlpatterns = [
    path('list/', CuisineTypeListView.as_view(), name='cuisine_type_list'),
    path('create/', CuisineTypeCreateView.as_view(), name='cuisine_type_create'),
    path('<int:pk>/update/', CuisineTypeUpdateView.as_view(), name='cuisine_type_update'),
]
