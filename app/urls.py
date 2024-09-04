from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('about/', user_input_view, name='about'),
    path('license/', license_view, name='license'),
    path('services/', services, name='services'),
    path('some/', some, name='some'),
    path('contacts/', contacts, name='contacts'),
    
]