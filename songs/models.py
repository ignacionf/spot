from django.db import models
from artists.models import Artist


class Genre(models.Model):
    name = models.CharField("Genre Name", max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Song(models.Model):
    name = models.CharField("Song Name", max_length=255)
    url = models.URLField()

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField("Release Date", null=True)

    order = models.PositiveSmallIntegerField("Order in the Top100 list", null=True)

    def __str__(self):
        return f"{self.artist} : {self.name}"

    class Meta:
        ordering = ["order", "release_date", "name"]
