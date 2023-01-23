from django.urls import path
from stream import views

app_name = 'stream'

urlpatterns = [
    # Add movie list url patterns
    path('movie-list/', views.movie_list, name='movie_list'),
    path('movie-list/<slug:category_slug>/', views.movie_list, name='movie_list_by_category'),
    # Add movie detail url pattern
    path('movies/<int:pk>', views.movie_detail, name='movie_detail'),
    # Add series list url patterns
    path('series-list/', views.series_list, name='series_list'),
    path('series-list/<slug:category_slug>/', views.series_list, name='series_list_by_category'),
    # Add series detail url pattern
    path('series/<int:pk>', views.series_detail, name='series_detail'),
]
