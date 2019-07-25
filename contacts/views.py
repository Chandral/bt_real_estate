from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    """
        Submits user's inquiry on the listing they are interested in.

        Takes user input from the contact form. Checks if user is logged in and if they have already inquired about the
        particular listing. Registers the inquiry in the database.

        :param request: HTTP Request
        :return:
    """
    if request.method == "POST":

        # User inputs
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Checks if user is logged in and has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

            # Redirects to the same listing page with a message telling an inquiry has been already made
            if has_contacted:
                messages.error(request, "Inquiry exists")
                return redirect('/listings/' + listing_id)

        # Saves the new inquiry about the listing
        inquiry = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
        inquiry.save()
        messages.success(request, "We'll get in touch")

        # Sends an email to the realtor of that listing to notify about the interested user
        send_mail(
            "Inquiry received",
            "We have received an inquiry",
            'chandral.photos@gmail.com',
            [realtor_email],
            fail_silently=False
        )
        return redirect('/listings/'+listing_id)
