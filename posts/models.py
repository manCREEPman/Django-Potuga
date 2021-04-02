from django.db import models


# Create your models here.
class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True, verbose_name='ID')
    artist_name = models.CharField(max_length=100, verbose_name='Исполнитель')
    artist_start_career_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата старта карьеры')

    def __unicode__(self):
        return self.artist_name

    def __str__(self):
        return self.artist_name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class MusicGenre(models.Model):
    genre_id = models.AutoField(primary_key=True, verbose_name='ID')
    genre_name = models.CharField(max_length=50, verbose_name='Название жанра')
    genre_description = models.CharField(max_length=500, verbose_name='Описание')

    def __unicode__(self):
        return self.genre_name

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Album(models.Model):
    album_id = models.AutoField(primary_key=True, verbose_name='ID альбома')
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='ID артиста')
    album_name = models.CharField(max_length=100, verbose_name='Название альбома')
    album_desc = models.CharField(max_length=1000, verbose_name='Описание альбома')
    album_release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата выпуска')

    def __unicode__(self):
        return self.album_name

    def __str__(self):
        return self.album_name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Composition(models.Model):
    composition_id = models.AutoField(primary_key=True, verbose_name='ID композиции')
    genre_id = models.ForeignKey(MusicGenre, on_delete=models.CASCADE, verbose_name='ID жанра')
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='ID альбома')
    composition_title = models.CharField(max_length=50, verbose_name='Название композиции')
    composition_duration = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Длительность')
    composition_text = models.CharField(max_length=1000, verbose_name='Название композиции')

    def __unicode__(self):
        return self.composition_title

    def __str__(self):
        return self.composition_title

    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'
