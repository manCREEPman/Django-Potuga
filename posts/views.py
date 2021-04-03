from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
import re


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
        context['queryset'] = compositions
    return render(request, 'posts/compositions.html', context)


def update_element_page(request):
    if request.method == 'GET':
        table = request.GET.get('table', '')
        context = {'title': ''}
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
            album = Album(artist_id=Artist.objects.filter(artist_id=int(post_data['artist_id']))[0],
                          album_name=post_data['album_name'],
                          album_desc=post_data['album_desc'],
                          album_release_date=post_data['album_release_date'])
            album.save()
            queryset = Album.objects.select_related('artist_id')
            context = {'title': 'Альбомы'}
            if queryset is not None:
                context['queryset'] = queryset
            return render(request, 'posts/albums.html', context)
        if table == 'compositions':
            composition = Composition(genre_id=MusicGenre.objects.filter(genre_id=int(post_data['genre_id']))[0],
                                      album_id=Album.objects.filter(album_id=int(post_data['album_id']))[0],
                                      composition_title=post_data['composition_title'],
                                      composition_duration=post_data['composition_duration'],
                                      composition_text=post_data['composition_text'])
            composition.save()
            queryset = Composition.objects.select_related('genre_id', 'album_id')
            context = {'title': 'Композиции'}
            if queryset is not None:
                context['queryset'] = queryset
            return render(request, 'posts/compositions.html', context)


def element_view(request):
    table = re.findall(r'/posts/(\w+)/\d+', request.path)[0]
    id = int(re.findall(r'/posts/\w+/(\d+)', request.path)[0])
    if table == 'genres':
        genre = MusicGenre.objects.filter(genre_id=id)
        context = {'title': 'Жанр'}
        if genre is not None:
            context['queryset'] = genre
        return render(request, 'posts/genre.html', context)
    if table == 'artists':
        artist = Artist.objects.filter(artist_id=id)
        context = {'title': 'Исполнитель'}
        if artist is not None:
            context['queryset'] = artist
        return render(request, 'posts/artist.html', context)
    if table == 'albums':
        album = Album.objects.filter(album_id=id)
        context = {'title': 'Альбом'}
        if album is not None:
            context['queryset'] = album
        return render(request, 'posts/album.html', context)
    if table == 'compositions':
        composition = Composition.objects.filter(composition_id=id)
        context = {'title': 'Композиция'}
        if composition is not None:
            context['queryset'] = composition
        return render(request, 'posts/composition.html', context)


def element_change(request):
    if request.method == 'GET':
        table = re.findall(r'/posts/(\w+)/change/\d+', request.path)[0]
        id = int(re.findall(r'/posts/\w+/change/(\d+)', request.path)[0])
        if table == 'genres':
            instance = get_object_or_404(MusicGenre, genre_id=id)
            form = GenreForm(request.POST or None, instance=instance)
            context = {
                'form': form,
            }
            return render(request, 'posts/edit_element_template.html', context)
        if table == 'artists':
            instance = get_object_or_404(Artist, artist_id=id)
            form = ArtistForm(request.POST or None, instance=instance)
            context = {
                'form': form,
            }
            return render(request, 'posts/edit_element_template.html', context)
        if table == 'albums':
            instance = get_object_or_404(Album, album_id=id)
            form = AlbumForm(request.POST or None, instance=instance)
            context = {
                'form': form,
            }
            return render(request, 'posts/edit_element_template.html', context)
        if table == 'compositions':
            instance = get_object_or_404(Composition, composition_id=id)
            form = CompositionForm(request.POST or None, instance=instance)
            context = {
                'form': form,
            }
            return render(request, 'posts/edit_element_template.html', context)
    else:
        post_data = request.POST
        table = re.findall(r'/posts/(\w+)/change/\d+', request.path)[0]
        id = int(re.findall(r'/posts/\w+/change/(\d+)', request.path)[0])
        if table == 'genres':
            MusicGenre.objects.filter(genre_id=id).update(genre_name=post_data['genre_name'],
                                                          genre_description=post_data['genre_description'])
            context = {'queryset': MusicGenre.objects.all()}
            return render(request, 'posts/genres.html', context)
        if table == 'artists':
            Artist.objects.filter(artist_id=id).update(artist_name=post_data['artist_name'],
                                                       artist_start_career_date=post_data['artist_start_career_date'])
            context = {'queryset': Artist.objects.all()}
            return render(request, 'posts/artists.html', context)
        if table == 'albums':
            Album.objects.filter(album_id=id).update(album_name=post_data['album_name'],
                                                     album_desc=post_data['album_desc'],
                                                     album_release_date=post_data['album_release_date'])
            context = {'queryset': Album.objects.all()}
            return render(request, 'posts/albums.html', context)
        if table == 'compositions':
            Composition.objects.filter(composition_id=id).update(composition_title=post_data['composition_title'],
                                                                 composition_duration=post_data['composition_duration'],
                                                                 composition_text=post_data['composition_text'])
            context = {'queryset': Composition.objects.all()}
            return render(request, 'posts/compositions.html', context)
