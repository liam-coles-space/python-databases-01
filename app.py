from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

# Retrieve all artists
album_repository = AlbumRepository(connection)
albums = album_repository.all()

# List them out
for album in albums:
    print(album)

# Find specific album
album_repository = AlbumRepository(connection)
album = album_repository.find(5)

#print it out
print(album)


