from django.shortcuts import render, get_object_or_404, redirect

from .models import Venue, Show, Artist
from .forms import VenueSearchForm, ArtistSearchForm, NewArtistForm


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


def artists_at_venue(request, venue_pk):  # pk = venue_pk
    """ Get all artists who have played a show at the venue with pk provided """

    shows = Show.objects.filter(venue=venue_pk).order_by('-show_date')
    venue = get_object_or_404(Venue, pk=venue_pk)

    return render(request, 'music_events/artists/artist_list_for_venue.html', {'venue': venue, 'shows': shows})


def venue_detail(request, venue_pk):
    venue = get_object_or_404(Venue, pk=venue_pk)
    return render(request, 'music_events/venues/venue_detail.html', {'venue': venue})


def artist_list(request):
    """ Get a list of all artists, ordered by name.

        If request contains a get parameter search_name then
        only include artists with names containing that text. """
    form = ArtistSearchForm()
    search_name = request.GET.get('search_name')
    if search_name:
        artists_results = Artist.objects.filter(name__icontains=search_name).order_by('name')
    else:
        artists_results = Artist.objects.all().order_by('name')

    return render(request, 'music_events/artists/artists_list.html',
                  {'artists': artists_results,
                   'form': form,
                   'search_term': search_name})


def artist_detail(request, artist_pk):
    """ Details about one artist """
    artist = get_object_or_404(Artist, pk=artist_pk)
    return render(request, 'music_events/artists/artist_detail.html', {'artist': artist})


def edit_artist(request, artist_pk):
    """Updates note"""
    artist = get_object_or_404(Artist, pk=artist_pk)

    form = NewArtistForm(request.POST or None, instance=artist)
    if form.is_valid():
        form.save()
        # messages.info(request, 'Artist updated')
        return redirect('events:artist_list')
    return render(request, 'music_events/artists/edit_artist.html',
                  {'artist': artist,
                   'form': form})


def delete_artist(request, artist_pk):
    """deletes note"""
    artist = get_object_or_404(Artist, pk=artist_pk)

    artist.delete()
    # messages.info(request, 'Note Deleted')
    return redirect('events:artist_list')

