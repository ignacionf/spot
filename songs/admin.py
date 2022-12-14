from django.contrib import admin
from .models import Song, Genre


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "name", "artist", "release_date")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
