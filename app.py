from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import *
import sys


# file: app.py

from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def _show(self, message):
        sys.stdout.write(message + "\n")

    def _prompt(self, message):
        sys.stdout.write(message + "\n")
        return sys.stdin.readline().strip()

    def run(self):
        # "Runs" the terminal application.
        # It might:
        #   * Ask the user to enter some input
        #   * Make some decisions based on that input
        #   * Query the database
        #   * Display some output
        # We're going to print out the artists!
        self._show('Welcome to the music library manager!')
        self._show('What would you like to do?')
        self._show(' 1 - List all albums')
        self._show(' 2 - List all artists')
        choice = self._prompt('Enter your choice:')

        if choice == '1':
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            print('Here is the list of albums:')
            for album in albums:
                print(f" * {album.id} - {album.title}")
        elif choice == '2':
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            print('Here is the list of artists:')
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        else:
            print('option not valid')

    
    

if __name__ == '__main__':
    app = Application()
    app.run()






