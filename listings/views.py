from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    """
        Shows all the listings sorted by latest posted with pagination for more than 3 listings.

        :param request: HTTP Request
        :return: Renders page with all the listings
    """
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {"listings": paged_listings}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    """
        Shows listing of specific property.

        :param request: HTTP Request
        :param listing_id: Listing's ID (int)
        :return: Renders page with information of the specific listing
    """
    specific_listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": specific_listing}
    return render(request, "listings/listing.html", context)


def search(request):
    """
        Allows the user to search for properties.

        Accepts the user inputs which are filters of keywords, city, state, bedrooms and price.

        :param request: HTTP Request
        :return: Renders a page based on filter based search result
    """

    # Creates a list of all the property listings which are published
    queryset_list = Listing.objects.order_by("-list_date").filter(is_published=True)

    # Filters the queryset_list for keywords and saves it into the same variable overwriting that list
    if 'keywords' in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Filters the queryset_list for city and saves it into the same variable overwriting that list
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Filters the queryset_list for state and saves it into the same variable overwriting that list
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Filters the queryset_list for number of bedrooms and saves it into the same variable overwriting that list
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Filters the queryset_list for price and saves it into the same variable overwriting that list
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }

    return render(request, "listings/search.html", context)
