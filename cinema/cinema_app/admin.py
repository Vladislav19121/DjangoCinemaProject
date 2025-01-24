from django.contrib import admin
from .models import Movie, Actor
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )



class ActorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)