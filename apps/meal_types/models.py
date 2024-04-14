from django.db import models
from apps.core.models import CoreModel

class MealType(CoreModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
