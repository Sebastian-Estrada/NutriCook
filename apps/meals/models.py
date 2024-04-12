from django.db import models
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