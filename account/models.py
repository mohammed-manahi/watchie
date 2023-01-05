from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Customize default user model to set email to a unique field
    """
    email = models.EmailField(unique=True)
