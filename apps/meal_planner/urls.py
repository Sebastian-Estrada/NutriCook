from django.urls import path
from .views import PlannerListView, PlannerCreateView, PlannerUpdateView

app_name = 'meal_planner'

urlpatterns = [
    path('list', PlannerListView.as_view(), name='planner_list'),
    path('create/', PlannerCreateView.as_view(), name='planner_create'),
    path('<int:pk>/update/', PlannerUpdateView.as_view(), name='planner_update'),
]