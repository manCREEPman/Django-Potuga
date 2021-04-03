from django.shortcuts import render
from .models import *
from .forms import *
import re

# Create your views here.


def posts_home(request):
    return render(request, 'posts/index.html', {'title': 'Главная'})


def genres_page(request):
    genres = MusicGenre.objects.all()
    context = {'title': 'Жанры'}
    if genres is not None:
        context['queryset'] = genres
    return render(request, 'posts/genres.html', context)


def artists_page(request):
    artists = Artist.objects.all()
    context = {'title': 'Исполнители'}
    if artists is not None:
        context['queryset'] = artists
    return render(request, 'posts/artists.html', context)


def albums_page(request):
    albums = Album.objects.select_related('artist_id')
    context = {'title': 'Альбомы'}
    if albums is not None:
        context['queryset'] = albums
    return render(request, 'posts/albums.html', context)


def compositions_page(request):
    compositions = Composition.objects.select_related('genre_id', 'album_id')
    context = {'title': 'Композиции'}
    if compositions is not None:
        context['compositions'] = compositions
    return render(request, 'posts/compositions.html', context)


def update_element_page(request):
    if request.method == 'GET':
        table = request.GET.get('table', '')
        context = {'title': ''}
        print(table)
        if table == 'genre':
            context['title'] = 'Жанры'
            context['form'] = GenreForm()
        elif table == 'artist':
            context['title'] = 'Исполнители'
            context['form'] = ArtistForm()
        elif table == 'album':
            context['title'] = 'Альбомы'
            context['form'] = AlbumForm()
        elif table == 'composition':
            context['title'] = 'Композиции'
            context['form'] = CompositionForm()
        return render(request, 'posts/update_element_template.html', context)
    if request.method == 'POST':
        table = re.findall(r'/posts/(\w+)/update', request.path)[0]
        post_data = request.POST
        if table == 'genres':
            genre = MusicGenre(genre_name=post_data['genre_name'], genre_description=post_data['genre_description'])
            genre.save()
            queryset = MusicGenre.objects.all()
            context = {'title': 'Жанры'}
            if queryset is not None:
                context['queryset'] = queryset
            return render(request, 'posts/genres.html', context)
        if table == 'artists':
            artist = Artist(artist_name=post_data['artist_name'],
                            artist_start_career_date=post_data['artist_start_career_date'])
            artist.save()
            queryset = Artist.objects.all()
            context = {'title': 'Исполнители'}
            if queryset is not None:
                context['queryset'] = queryset
            return render(request, 'posts/artists.html', context)
        if table == 'albums':
            album = Album(artist_id=post_data['artist_id'],
                          album_name=post_data['album_name'],
                          album_desc=post_data['album_desc'],
                          album_release_date=post_data['album_release_date'])
            album.save()
            queryset = Album.objects.select_related('artist_id')
            context = {'title': 'Альбомы'}
            if queryset is not None:
                context['queryset'] = queryset
            return render(request, 'posts/albums.html', context)
# {'csrfmiddlewaretoken': ['bvB1nx5yu4TBAl1qwd82MZ3esytPSpqGwrR7WjTGPAhUR3mX4M28jx7g9hPVwuem'], 'genre_name': ['Джаз'], 'genre_description': ['Новое описание джаза']}>
# /posts/genres/update
