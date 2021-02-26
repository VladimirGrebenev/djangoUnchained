from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
]