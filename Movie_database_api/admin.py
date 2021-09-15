from django.contrib import admin
from .models import Actor, Genre, Movie, Rating

# Register your models here.

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)
