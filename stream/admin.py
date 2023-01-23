from django.contrib import admin
from stream.models import Movie, Series, Category, Season, Episode


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Register movie model in admin site
    """
    list_display = ['title', 'description', 'category', 'movie', 'trailer', 'poster', 'production_date', 'author']
    list_filter = ['category', 'created_at', 'production_date']
    search_fields = ['category', 'movie']


class SeasonInline(admin.TabularInline):
    """
    Add subscription model as inline ui view for user in admin site
    """
    model = Season


class EpisodeInline(admin.TabularInline):
    """
    Add subscription model as inline ui view for user in admin site
    """
    model = Episode


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """
    Register series model in admin site
    """
    list_display = ['title', 'description', 'category', 'main_trailer', 'main_poster', 'initial_production_date']
    list_filter = ['category', 'created_at', 'initial_production_date']
    search_fields = ['category']
    inlines = [SeasonInline, EpisodeInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register category model in admin site
    """
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name']
