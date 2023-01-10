from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'

urlpatterns = [
    # Add user dashboard url pattern
    path('dashboard/<str:username>/<int:pk>/', views.dashboard, name='dashboard'),
    # Add user registration url pattern
    path('register/', views.register, name='register'),
    # # Add user edit url pattern
    # path('edit/', views.edit, name='edit'),
]
