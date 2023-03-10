"""watchie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views

urlpatterns = [
    # Add django authentication url patterns
    path('', include('django.contrib.auth.urls')),
    # Include url patterns of account app
    path('account/', include('account.urls', namespace='account')),
    path('admin/', admin.site.urls),
    # Add default route
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    # Include url patterns of stream app
    path('stream/', include('stream.urls', namespace='stream')),
    # Include url patterns of payment app
    path('payment/', include('payment.urls', namespace='payment')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
