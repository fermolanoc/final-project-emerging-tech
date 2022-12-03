from django.urls import path
from . import views

app_name = 'music_events'
urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Venue-related
    path('venues/list/', views.venue_list, name='venue_list'),
]
