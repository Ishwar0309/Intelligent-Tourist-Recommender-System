"""Itrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from tourism import views
from tourism.views import HotelDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('loginModule.urls')),
	path('base/' , views.base,name = 'base'),
    path('profile/' , views.profile, name = 'profile'), 
    #path('upload/' , views.upload, name = 'upload'),
    path('home/' , views.home , name = 'tourism-home'),
    path('hotel/<int:pk>/' , HotelDetailView.as_view(), name = "hotel-details"),
    path('itemDelete/<int:pk>/', views.deleteItem , name = 'itemDelete'),
    path('cart/' , views.cart, name = "cart"),
    path('cities/',include('cities.urls')),
]