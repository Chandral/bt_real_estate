from django.urls import path
from . import views

# List of view methods for dispaying static web pages of the site
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
