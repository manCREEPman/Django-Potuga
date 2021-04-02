"""Music_genres URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from posts.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', posts_home),


    # url(r'posts/\w+/update/?item=', 'posts.views.update_element'),
    #
    url(r'^posts/genres/$', genres_page),
    # url(r'posts/genres/?item=', 'posts.views.genre'),
    #
    url(r'posts/artists/$', artists_page),
    # url(r'posts/artists/?item=', 'posts.views.artist'),
    #
    url(r'posts/albums/$', albums_page),
    # url(r'posts/albums/?item=', 'posts.views.album'),
    #
    url(r'posts/compositions/$', compositions_page),
    # url(r'posts/compositions/?item=', 'posts.views.composition'),
]
