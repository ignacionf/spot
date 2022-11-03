from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import Song
from artists.models import Artist
from .serializers import SongSerializer


class SongViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["get"])
    def search(self, request):

        q = request.GET.get("q", None)

        if q:
            q = f"%{q}%"
            query = 'SELECT * FROM songs_song as s INNER JOIN artists_artist ON (s.artist_id = artists_artist.id) WHERE (s.name LIKE %s OR artists_artist.name LIKE %s) ORDER BY s."order" ASC'
            qs = Song.objects.raw(query, [q, q])
        else:
            query = "SELECT * FROM songs_song as s INNER JOIN artists_artist ON (s.artist_id = artists_artist.id)"
            qs = Song.objects.raw(query)

        return Response(SongSerializer(qs, many=True).data)

    @action(detail=False, methods=["get"])
    def top50(self, request):

        query = 'SELECT * FROM songs_song as s INNER JOIN artists_artist ON (s.artist_id = artists_artist.id) WHERE (s."order" <=50) ORDER BY s."order" ASC '
        qs = Song.objects.raw(query)

        return Response(SongSerializer(qs, many=True).data)

    def destroy(self, request, pk):

        try:
            Song.objects.get(pk=int(pk)).delete()
        except (Song.DoesNotExist, ValueError):
            return Response(
                {"errors": ["Song invalid"]}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"action": "deleted"})

    def create(self, request):

        print(request.POST)
        try:
            song = Song(
                id=request.POST["id"],
                name=request.POST["name"],
                artist_id=int(request.POST["artist_id"]),
                url=request.POST["url"],
                release_date=request.POST["release_date"],
                order=int(request.POST["order"]),
            )
            song.save()
            song.genres.add(request.POST["genres"])
        except MultiValueDictKeyError as e:
            return Response(
                {"errors": [f"The {e} field is required"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(SongSerializer(song).data)
