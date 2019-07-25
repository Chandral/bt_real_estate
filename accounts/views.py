from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contacts.models import Contact


def register(request):
    """
        Registers users for the site.

        Accepts information submitted by the user for registration. Checks the following things before registering the
        user: (1) Passwords match (2) User does not already exist in the database.

        :param request: HTTP Request

        :return: Redirects to the same page with an error message if the checks fail or else redirects to the login
        page with a success message.

    """

    if request.method == 'POST':

        # User inputs
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password validation
        if password == password2:

            # Checks if users already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username taken")
                return redirect('register')

            # Registers user
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Registered")
                return redirect('login')

        # Redirects because passwords did not match
        else:
            messages.error(request, "Passwords don't match")
            return redirect('register')

    return render(request, 'accounts/register.html')


def login(request):
    """
        Logs in the user.

        Accepts information submitted by the user for login. Checks the following things before logging in the user:
        (1) username and password matches with the database.

        :param request: HTTP Request
        :return: Redirects to the user dashboard if login is successful or else redirects to the same page with an
        error message.
    """

    if request.method == 'POST':

        # User inputs
        username = request.POST['username']
        password = request.POST['password']

        # Authenticates the user and checks if user exists
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "Logged in")
            return redirect('dashboard')

        # Redirects to the same page if user credentials are incorrect
        else:
            messages.success(request, "Invalid credentials")
        return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    """
        Logs the user out
        :param request: HTTP Request
        :return: Redirects to login page
    """

    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Logged out")
        return redirect('index')


def dashboard(request):
    """
        Takes user to their dashboard page.

        Fetches all the inquires user has made and lists them in the dashboard.

        :param request: HTTP Request
        :return: Renders dashboard page
    """

    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {'contacts': contacts}
    return render(request, "accounts/dashboard.html", context)
