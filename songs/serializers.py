from rest_framework import serializers

from .models import Song, Genre


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
        depth = 1


class GenreSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ["id", "name", "songs"]

    def get_songs(self, obj):

        query = 'SELECT * FROM songs_song as s INNER JOIN songs_song_genres ON (s.id = songs_song_genres.song_id) WHERE songs_song_genres.genre_id = %s ORDER BY s."order" ASC'
        qs = obj.song_set.raw(query, [obj.id])
        return SongSerializer(qs, many=True).data
