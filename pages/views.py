from django.shortcuts import render
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    """
        Displays the home page of the site.

        :param request: HTTP Request
        :return: Renders a page with the latest 3 listings published on the site.
    """

    # Fetches the latest 3 listings published
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    """
        Displays the about page of the site.

        :param request: HTTP Request
        :return: Renders the about page with the realtors registered on the site. Also displays seller(s) of the month.
    """
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
