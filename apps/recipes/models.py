from django.db import models

from apps.cuisine_types.models import CuisineType
from apps.core.models import CoreModel
from apps.ingredients.models import Ingredient
from apps.users.models import User


class Recipe(CoreModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    cuisine_type = models.ForeignKey(CuisineType, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title

class RecipeIngredient(CoreModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.name}"
