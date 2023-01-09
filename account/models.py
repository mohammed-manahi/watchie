import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    """
    Customize default user model to set email to a unique field
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    """
    Create profile model and associate one-to-one relationship with user model
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/users', default='assets/img/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} profile'


class Favorite(models.Model):
    """
    Create favorite model and associate many-to-many with user model
    """
    ACTION = 'AC'
    ADVENTURE = 'AD'
    BIOGRAPHY = 'BI'
    COMEDY = 'CO'
    CRIME = 'CR'
    HISTORY = 'HI'
    HORROR = 'HO'
    DRAMA = 'DR'
    SCIFI = 'SC'
    FAVORITE_CHOICES = [
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (BIOGRAPHY, 'Biography'),
        (COMEDY, 'Comedy'),
        (CRIME, 'Crime'),
        (HISTORY, 'History'),
        (HORROR, 'Horror'),
        (DRAMA, 'Drama'),
        (SCIFI, 'Sci-Fi'),
    ]
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorites')
    favorite = models.CharField(max_length=2, choices=FAVORITE_CHOICES, default=None, unique=True)

    def __str__(self):
        return self.favorite


class Subscription(models.Model):
    """
    Create subscription model and associate one-to-one relationship with user model
    """
    TRIAL = 'TR'
    STANDARD = 'ST'
    PREMIUM = 'PR'
    SUBSCRIPTION_CHOICES = [
        (TRIAL, 'Trial'),
        (STANDARD, 'Standard'),
        (PREMIUM, 'Premium'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=2, choices=SUBSCRIPTION_CHOICES, default=TRIAL)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return self.type
