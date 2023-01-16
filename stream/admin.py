from django.contrib import admin
from stream.models import Movie, Series, Category


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'movie', 'trailer', 'poster', 'production_date', 'author']
    list_filter = ['category', 'created_at', 'production_date']
    search_fields = ['category', 'movie']


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'episode', 'season_title', 'season_number', 'season_trailer',
                    'season_poster', 'season_production_date']
    list_filter = ['category', 'created_at', 'season_production_date']
    search_fields = ['category', 'episode', 'season_title', 'season_number']
