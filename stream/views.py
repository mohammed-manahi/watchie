from django.shortcuts import render, get_object_or_404
from stream.models import Movie, Series, Category


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
