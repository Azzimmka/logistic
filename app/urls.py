from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base, name='base'),
    path('about/', about, name='about'),
    
]