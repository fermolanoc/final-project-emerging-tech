from django import forms


class VenueSearchForm(forms.Form):
    search_name = forms.CharField(label='Venue Name', max_length=200)