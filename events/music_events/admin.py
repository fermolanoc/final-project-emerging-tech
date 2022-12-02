from django.contrib import admin

# Register your models here.
from .models import Venue, Artist, Show

admin.site.register(Venue)
admin.site.register(Artist)
admin.site.register(Show)
