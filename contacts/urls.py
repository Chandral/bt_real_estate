from django.urls import path
from . import views

# List of view methods for contact inquiry form
urlpatterns = [
    path('contact', views.contact, name='contact'),
]
