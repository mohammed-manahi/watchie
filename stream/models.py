from django.core.validators import FileExtensionValidator
from django.db import models
from account.models import User


class Category(models.Model):
    """
    Create category model and associate it with many-to-one relationship with stream base model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)


class StreamBase(models.Model):
    """
    Create abstract model for stream types
    """
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='%(class)s_related')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_related')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Movie(StreamBase):
    """
    Create movie model which extends stream base model
    """
    movie = models.FileField(upload_to='stream/movies/videos',
                             validators=[FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])
    trailer = models.FileField(upload_to='stream/movies/trailers')
    poster = models.ImageField(upload_to='stream/movies/posters')
    production_date = models.DateField()

    class Meta:
        indexes = [models.Index(fields=["-created_at"])]

    def __str__(self):
        return self.movie


class Series(StreamBase):
    """
    Create tv series model which extends stream base model
    """
    episode = models.FileField(upload_to='stream/series/episodes',
                               validators=[FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])
    season_trailer = models.ImageField(upload_to='stream/series/trailers')
    season_poster = models.ImageField(upload_to='stream/series/posters')
    season_title = models.CharField(max_length=100)
    season_number = models.PositiveIntegerField()
    season_production_date = models.DateField()

    class Meta:
        indexes = [models.Index(fields=["-created_at"])]

    def __str__(self):
        return self.episode
