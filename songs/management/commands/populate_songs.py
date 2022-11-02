import sys
import requests

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from songs.models import Song, Genre
from artists.models import Artist

class Command(BaseCommand):
    help = 'Populate Songs, Genres and Artists db'

#    def add_arguments(self, parser):
#        parser.add_argument('purge', nargs='+', type=int)

    def handle(self, *args, **options):

        r = requests.get(settings.TOP100_SONGS_URL)

        if r.status_code == requests.codes.ok:
            self.stdout.write(self.style.SUCCESS('Successfully get songs'))
        else:
            self.stdout.write(self.style.ERROR(f'I cant get songs... status_code={r.status_code}'))
            sys.exit(1)

        data = r.json()
        Artist.objects.all().delete()
        for song in data['feed']['results']:
            print(song)

            instance = Song(
                id=song['id'],
                name=song['name'],
                url=song['url']
            )

            # defaults prevents diff names of artists, like: {'id': 1276656483, 'name': 'Lil Baby'}
            # and {'id': 1276656483, 'name': 'Lil Baby & Young Thug'}
            instance.artist,_ = Artist.objects.get_or_create(
                id=song['artistId'],
                defaults={"name":song['artistName'],
                          "url":song['artistUrl']}
            )

            instance.save()

            genres =[Genre.objects.get_or_create(
                                id=genre['genreId'],
                                name=genre['name'],
                                url=genre['url']
                            ) for genre in song['genres']]

            instance.genres.add(*[x[0] for x in genres])
