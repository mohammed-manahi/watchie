from django.urls import path
from stream import views

app_name = 'stream'

urlpatterns = [
    # Add movie list url pattern
    path('movie-list/', views.movie_list, name='movie_list'),
    path('movie-list/<slug:category_slug>/', views.movie_list, name='movie_list_by_category'),
]
