from django.shortcuts import render

from .models import Venue
from .forms import VenueSearchForm


# Create your views here.
def homepage(request):
    return render(request, 'music_events/home.html')


def venue_list(request):
    form = VenueSearchForm()
    search_name = request.GET.get('search_name')

    if search_name:
        # search for this venue, display results. Use case-insensitive contains
        venues_results = Venue.objects.filter(name__icontains=search_name).order_by('name')
    else:
        venues_results = Venue.objects.all().order_by('name')

    # venues_list = Venue.objects.all().order_by('name')
    # context =
    return render(request, 'music_events/venues/venue_list.html',
                  {'venues': venues_results,
                   'form': form,
                   'search_term': search_name})


def artists_list(request):
    return render(request, 'music_events/artists/artists_list.html')
