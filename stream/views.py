from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stream.models import Movie, Series, Category
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


@login_required()
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
    return redirect('index')
