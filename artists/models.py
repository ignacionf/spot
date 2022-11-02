from django.db import models

class Artist(models.Model):
    name = models.CharField("Artist Name", max_length=255)
    url = models.URLField()
