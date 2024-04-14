from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import MealPlan
from .forms import PlannerForm

class PlannerListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = 'meal_planner/planner_list.html'
    context_object_name = 'meal_plans'

    def get_queryset(self):
        user = self.request.user
        return MealPlan.objects.filter(user=user)


class PlannerCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    form_class = PlannerForm
    template_name = 'meal_planner/planner_create.html'
    success_url = reverse_lazy('meal_planner:planner_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlannerUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    form_class = PlannerForm
    template_name = 'meal_planner/planner_update.html'
    success_url = reverse_lazy('meal_planner:planner_list')
