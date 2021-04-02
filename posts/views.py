from django.shortcuts import render

# Create your views here.


def posts_home(request):
    return render(request, 'posts/index.html', {'title': 'Главная', 'content': 'adsf'})


def genres_page(request):
    return render(request, 'posts/genres.html', {'title': 'Жанры', 'content': 'Жанры'})


def artists_page(request):
    return render(request, 'posts/artists.html', {'title': 'Исполнители', 'content': 'Исполнители'})


def albums_page(request):
    return render(request, 'posts/albums.html', {'title': 'Альбомы', 'content': 'Альбомы'})


def compositions_page(request):
    return render(request, 'posts/compositions.html', {'title': 'Композиции', 'content': 'Композиции'})
