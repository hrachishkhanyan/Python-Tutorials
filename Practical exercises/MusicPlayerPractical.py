import os


class Player:
    def __init__(self, playlist):
        self.playlist: Playlist = playlist
        self.now_playing = False

    def play(self):
        self.now_playing = True


class Playlist:
    def __init__(self):
        self.song_list: [Song] = []

    def load_songs(self, path):
        if not os.path.exists(path):
            return

        with open(path, 'r') as file:
            for song_info in file.readlines():
                artist, album, year, name = song_info.split('\t')

                song = Song(artist, album, year, name)
                self.song_list.append(song)

    def show_songs(self):
        for song in self.song_list:
            print(song)
            print('=' * 100)


class Song:
    def __init__(self, artist, album, year, song_name):
        self.artist = artist
        self.album = album
        self.year = year
        self.name = song_name

    def __str__(self):
        return f'Artist: {self.artist}\nAlbum: {self.album}\nYear: {self.year}\nSong name: {self.name}'


playlist = Playlist()

playlist.show_songs()
playlist.load_songs('./albums.txt')
playlist.show_songs()
