from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"