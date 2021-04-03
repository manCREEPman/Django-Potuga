from django import forms
from .models import *


class GenreForm(forms.ModelForm):
    class Meta:
        model = MusicGenre
        fields = ['genre_name', 'genre_description']


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name', 'artist_start_career_date']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist_id', 'album_name', 'album_desc', 'album_release_date']


class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = ['genre_id', 'album_id', 'composition_title',
                  'composition_duration', 'composition_text']
