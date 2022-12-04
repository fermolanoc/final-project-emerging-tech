from django.urls import path
from . import views

app_name = 'music_events'
urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Venue-related
    path('venues/list/', views.venue_list, name='venue_list'),
    path('venues/detail/<int:venue_pk>/', views.venue_detail, name='venue_detail'),
    path('venues/artists_at/<int:venue_pk>/', views.artists_at_venue, name='artists_at_venue'),

    # Artist related
    path('artists/list/', views.artist_list, name='artist_list'),
    path('artists/detail/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('artists/edit/<int:artist_pk>/', views.edit_artist, name='edit_artist'),
    path('artists/delete/<int:artist_pk>/', views.delete_artist, name='delete_artist'),
]
