from lib.album_repository import *
from lib.album import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    albums = repository.all()

    assert albums == [
        Album(1,'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]


#When i call the find method with an ID i get a album object back based on the row in the albums table that has the matching ID

def test_find_record_method(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    album = repository.find(3)

    assert album == Album(3, 'Waterloo', 1974, 2)

