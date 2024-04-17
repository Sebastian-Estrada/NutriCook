import random

from django.db import models

from datetime import datetime

from apps.core.models import CoreModel
from apps.meal_types.models import MealType
from apps.recipes.models import Recipe
from apps.users.models import User


class Meal(CoreModel):
    name = models.CharField(max_length=100)
    meal_type = models.ForeignKey(MealType, on_delete=models.PROTECT, blank=True, null=True)
    recipes = models.ManyToManyField(Recipe, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    @staticmethod
    def get_users_meals(user):
        return Meal.objects.filter(user=user)

    @staticmethod
    def get_recommended_meal(user):
        MEAL_CATEGORIES = {
            'breakfast': [6, 7, 8, 9, 10],
            'lunch': [12, 13, 14],
            'dinner': [18, 19, 20],
            'snack': [10, 11, 12, 15, 16, 17]
        }

        current_hour = datetime.now().hour
        current_category = None

        for category, hours in MEAL_CATEGORIES.items():
            if current_hour in hours:
                current_category = category
                break

        if current_category:
            recipes_in_category = Meal.get_users_meals(user).filter(meal_type__name__iexact=current_category)

            if recipes_in_category.exists():
                return random.choice(recipes_in_category)

        return None