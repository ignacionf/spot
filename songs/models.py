from django.db import models
from artists.models import Artist


class Genre(models.Model):
    name = models.CharField("Genre Name", max_length=50)
    url = models.URLField()

class Song(models.Model):
    name = models.CharField("Song Name", max_length=255)
    url = models.URLField()

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
