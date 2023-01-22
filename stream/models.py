from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from account.models import User


class Category(models.Model):
    """
    Create category model and associate it with many-to-one relationship with stream base model
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
    name = models.CharField(max_length=100, choices=FAVORITE_CHOICES, default=None, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stream:movie_list_by_category', args=[self.slug])


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
    trailer = models.FileField(upload_to='stream/movies/trailers',
                               validators=[FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])
    poster = models.ImageField(upload_to='stream/movies/posters',
                               validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    production_date = models.DateField()

    class Meta:
        indexes = [models.Index(fields=["-created_at"])]
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stream:movie_detail', args=[self.pk])


class Series(StreamBase):
    """
    Create tv series model which extends stream base model
    """
    episode_title = models.CharField(max_length=100)
    episode_number = models.PositiveIntegerField()
    episode = models.FileField(upload_to='stream/series/episodes',
                               validators=[FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])
    season_trailer = models.FileField(upload_to='stream/series/trailers',
                                      validators=[FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])
    season_poster = models.ImageField(upload_to='stream/series/posters',
                                      validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    season_title = models.CharField(max_length=100)
    season_number = models.PositiveIntegerField()
    season_production_date = models.DateField()

    class Meta:
        indexes = [models.Index(fields=["-created_at"])]
        verbose_name = 'series'
        verbose_name_plural = 'series'

    def __str__(self):
        return self.title
