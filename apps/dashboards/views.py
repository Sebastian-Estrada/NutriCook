from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.recipes.models import Recipe
from apps.ingredients.models import Ingredient
from apps.meals.models import Meal
from apps.cuisine_types.models import CuisineType
from apps.meal_types.models import MealType
from apps.meal_planner.models import MealPlan

from django.http import JsonResponse

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        meal_plans = MealPlan.objects.filter(user=user)
        data = [{'title': event.name, 'start': str(event.date.isoformat())} for event in meal_plans]

        context['total_recipes'] = Recipe.objects.filter(author=user).count()
        context['total_ingredients'] = Ingredient.objects.all().count()
        context['total_meals'] = Meal.objects.filter(user=user).count()
        context['total_cuisine_types'] = CuisineType.objects.all().count()
        context['total_meal_types'] = MealType.objects.all().count()
        context['total_meal_plans'] = meal_plans.count()
        context['meal_plans'] = data
        context['user'] = self.request.user

        return context
