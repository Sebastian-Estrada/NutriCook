from django.db import models

from apps.users.models import User
from apps.meals.models import Meal

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    date = models.DateField()
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return f"{self.user.username}'s Meal Plan for {self.date}"
