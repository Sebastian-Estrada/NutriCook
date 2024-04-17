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

    def get_meals(self):
        """
        Returns all meals associated with this instance.

        Returns:
            QuerySet: A queryset containing all meals associated with this instance.
        """
        return self.meals.all()

    @staticmethod
    def retrieve_meal_plans_for_user(user):
        return MealPlan.objects.filter(user=user)

    @staticmethod
    def retrieve_meal_plans_in_date_range(user, start_date, end_date):
        return MealPlan.objects.filter(user=user, date__range=[start_date, end_date])

    @staticmethod
    def meal_plan_exists(user, name, date):
        return MealPlan.objects.filter(user=user, name=name, date=date).exists()

    def count_meals(self):
        return self.meals.count()

    @staticmethod
    def iso_format_date(meal_plans):
        return [{'title': event.name, 'start': str(event.date.isoformat())} for event in meal_plans]