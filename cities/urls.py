import numpy
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name='cities'),
    path('submit/',submitInfo,name='submit'),
    path('recommend/',recommend,name='recommend')
]