import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from multiselectfield import MultiSelectField


class User(AbstractUser):
    """
    Customize default user model to set email to a unique field
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, unique=True)

    def get_absolute_url(self):
        # Create canonical url for detail view
        return reverse('account:dashboard', args=[self.pk, self.username])

    def __str__(self):
        return self.username


class Profile(models.Model):
    """
    Create profile model and associate one-to-one relationship with user model
    """
    ACTION = 'ACTION'
    ADVENTURE = 'ADVENTURE'
    BIOGRAPHY = 'BIOGRAPHY'
    COMEDY = 'COMEDY'
    CRIME = 'CRIME'
    HISTORY = 'HISTORY'
    HORROR = 'HORROR'
    DRAMA = 'DRAMA'
    SCIFI = 'SCIFI'
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite = MultiSelectField(max_length=100, choices=FAVORITE_CHOICES, default=None, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/users', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} profile'


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
        return str(self.type)
