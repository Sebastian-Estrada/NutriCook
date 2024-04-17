from django.db import models
from apps.core.models import CoreModel

class Ingredient(CoreModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_actives():
        return Ingredient.objects.filter(active=True)

    @staticmethod
    def get_all():
        return Ingredient.objects.all()

    @staticmethod
    def get_ingredient_by_id(id):
        try:
            return Ingredient.objects.get(id=id)
        except Ingredient.DoesNotExist:
            return None

class Category(CoreModel):
    # Fruits, Vegetable, Dairy, Grains, Condiments, Canned, etc.
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
