from django.urls import path
from . import views

# List of view methods for user account management (login, logout, register etc.)
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]