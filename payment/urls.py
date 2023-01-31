from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
    # Add subscribe url pattern
    path('subscribe/', views.subscribe, name='subscribe'),
    path('standard-subscription/', views.standard_subscription, name='standard_subscription'),
    path('premium-subscription/', views.premium_subscription, name='premium_subscription'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),

]
