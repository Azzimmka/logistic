from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('about/', about, name='about'),
    path('license/', license_view, name='license'),
    
]