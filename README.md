# spot

A simpel apple song filter. Requires python >= 3.9

## Environ

In the root folder of the project add the .env file with:

```
DEBUG=True
TOP100_SONGS_URL="https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json"
```

## First Steps

```
$ pip install pipenv  # only if you don't have it installed
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run python manage.py createsuperuser --username admin --email test@example.com
$ pipenv run python manage.py populate_songs
```

## Run

```
$ pipenv run python manage.py runserver
```

## Test

First you have to generate a token, it can be done by admin or by console:

```
$ pipenv run python manage.py drf_create_token admin
Loading .env environment variables...
Generated token 78fe64903711049129b94f7dd05e6d9cffae0da5 for user admin
```
### Search songs
```
$ curl "http://localhost:8000/songs/search/?q=<term to search>" -H "Authorization: Token <token>"
```

### Top50 songs
```
$ curl "http://localhost:8000/songs/top50/" -H "Authorization: Token <token>"
```

### Group by Genre
```
$ curl "http://localhost:8000/songs/by_genre/" -H "Authorization: Token <token>"
```

### Delete song
```
$ curl "http://localhost:8000/songs/<song_id>/" -X DELETE -H "Authorization: Token <token>"
```

### Add song
```
$ curl "http://localhost:8000/songs/" -X POST -H "Authorization: Token <token>" \
    -d "id=<song_id>&name=<sond name>&artist_id=<artist_id>&genres=<genre1>&genres=<genre2>&url=<url>&release_date=<date>&order=<order>"
```
