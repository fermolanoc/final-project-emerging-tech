from django.shortcuts import render

from .models import Venue


# Create your views here.
def homepage(request):
    return render(request, 'music_events/home.html')


def venue_list(request):
    venues_list = Venue.objects.all().order_by('name')
    context = {'venues_list': venues_list}
    return render(request, 'music_events/venues/venue_list.html', context)


def artists_list(request):
    return render(request, 'music_events/artists/artists_list.html')
