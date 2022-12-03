from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'music_events/home.html')


def venue_list(request):
    return render(request, 'music_events/venues/venue_list.html')
