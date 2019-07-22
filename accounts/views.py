from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing error messages')
        return redirect('register')
    return render(request, "accounts/register.html")


def login(request):
    return render(request, "accounts/login.html")


def logout():
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")