"""littlelemon URL Configuration

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
#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),

   path('restaurant/', include('restaurant.urls')),
   path('restaurant/menu/',include('restaurant.urls')),

   # Include the API endpoints for the BookingViewSet under the 'restaurant/booking/' URL route.
   path('restaurant/booking/', include(router.urls)),

   # Add Djoser URL routes for authentication
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
