from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


class MusicGenreModelAdmin(admin.ModelAdmin):
    list_display = ['genre_id', 'genre_name']
    list_display_links = ['genre_name']
    list_filter = ['genre_id']
    search_fields = ['genre_name']

    class Meta:
        model = MusicGenre


class ArtistModelAdmin(admin.ModelAdmin):
    list_display = ['artist_id', 'artist_name', 'artist_start_career_date']
    list_display_links = ['artist_name']
    list_filter = ['artist_id', 'artist_start_career_date', 'artist_name']
    search_fields = ['artist_name']

    class Meta:
        model = Artist


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ['album_id', 'album_name', 'album_release_date']
    list_display_links = ['album_name']
    list_filter = ['album_id', 'album_release_date', 'album_name']
    search_fields = ['album_name']

    class Meta:
        model = Album


class CompositionModelAdmin(admin.ModelAdmin):
    list_display = ['composition_id', 'composition_title', 'composition_duration']
    list_display_links = ['composition_title']
    list_filter = ['album_id', 'composition_duration', 'composition_title']
    search_fields = ['composition_title']

    class Meta:
        model = Composition


admin.site.register(MusicGenre, MusicGenreModelAdmin)
admin.site.register(Artist, ArtistModelAdmin)
admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Composition, CompositionModelAdmin)
