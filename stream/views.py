from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stream.models import Movie, Series, Category, Season, Episode
from account.helpers import is_subscription_active


def movie_list(request, category_slug=None):
    """
    Create movie list view
    :param request:
    :return:
    """
    category = None
    movies = Movie.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        movies = Movie.objects.filter(category=category)
    template = 'stream/movie_list.html'
    context = {'movies': movies, 'categories': categories, 'category': category}
    return render(request, template, context)


@login_required
def movie_detail(request, pk):
    """
    Create movie detail view
    :param request:
    :param pk:
    :return:
    """
    if is_subscription_active(request.user.pk):
        movie = get_object_or_404(Movie, pk=pk)
        suggested_movies = Movie.objects.filter(category=movie.category).exclude(pk=pk).order_by('-created_at')[:3]
        template = 'stream/movie_detail.html'
        context = {'movie': movie, 'suggested_movies': suggested_movies}
        return render(request, template, context)
    messages.error(request, "You don't have an active subscription to watch this content")
    return redirect('stream:movie_list')


def series_list(request, category_slug=None):
    """
    Create series list view
    :param request:
    :param category_slug:
    :return:
    """
    category = None
    series = Series.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        series = Series.objects.filter(category=category)
    template = 'stream/series_list.html'
    context = {'series': series, 'categories': categories, 'category': category}
    return render(request, template, context)


@login_required
def series_detail(request, pk):
    """
    Create series detail view
    :param request:
    :param pk:
    :return:
    """
    if is_subscription_active(request.user.pk):
        if request.user.subscription.type == 'PR':
            series = get_object_or_404(Series, pk=pk)
            all_seasons = series.seasons.all()
            all_episodes = series.series_episodes.all()
            number_of_episodes = series.series_episodes.count()
            template = 'stream/series_detail.html'
            context = {'series': series, 'all_seasons': all_seasons, 'number_of_episodes': number_of_episodes,
                       'all_episodes': all_episodes}
            return render(request, template, context)
        messages.error(request, "You subscription does not include watching this content")
        return redirect('stream:series_list')
    messages.error(request, "You don't have an active subscription to watch this content")
    return redirect('index')


@login_required
def season_detail(request, pk, series_pk):
    """
    Create season detail view
    :param request:
    :param pk:
    :return:
    """
    if is_subscription_active(request.user.pk):
        if request.user.subscription.type == 'PR':
            series = Series.objects.get(pk=series_pk)
            season = get_object_or_404(Season, pk=pk)
            season_episodes = Episode.objects.filter(season=season)
            number_of_episodes = season_episodes.count()
            template = 'stream/season_detail.html'
            context = {'season': season, 'season_episodes': season_episodes, 'number_of_episodes': number_of_episodes,
                       'series': series}
            return render(request, template, context)
        messages.error(request, "You subscription does not include watching this content")
        return redirect('stream:series_list')
    messages.error(request, "You don't have an active subscription to watch this content")
    return redirect('index')


@login_required
def episode_detail(request, pk, series_pk, season_pk):
    """
    Create episode detail view
    :param request:
    :param pk:
    :param series_pk:
    :param season_pk:
    :return:
    """
    if is_subscription_active(request.user.pk):
        if request.user.subscription.type == 'PR':
            series = Series.objects.get(pk=series_pk)
            season = Season.objects.get(pk=season_pk)
            episode = get_object_or_404(Episode, pk=pk)
            template = 'stream/episode_detail.html'
            context = {'series': series, 'season': season, 'episode': episode}
            return render(request, template, context)
        messages.error(request, "You subscription does not include watching this content")
        return redirect('stream:series_list')
    messages.error(request, "You don't have an active subscription to watch this content")
    return redirect('index')
