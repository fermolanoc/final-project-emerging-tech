from django import forms
from .models import Artist


class VenueSearchForm(forms.Form):
    search_name = forms.CharField(label='Venue Name', max_length=200)


class ArtistSearchForm(forms.Form):
    search_name = forms.CharField(label='Artist Name', max_length=200)


class NewArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('description', 'genre', 'nationality')
