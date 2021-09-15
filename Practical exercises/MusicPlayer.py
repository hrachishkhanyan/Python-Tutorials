class Player:
    def __init__(self, playlist):
        self.playlist = playlist
        self.now_playing = None
        self.play_index = 0

    def play(self, song=None):
        self.now_playing = self.playlist.songs[self.play_index]
        print('Now playing "{}" by "{}"'.format(self.now_playing.name, self.now_playing.artist))

    def show_song_info(self):
        if not self.now_playing:
            print('No song is being played.')
            return

        name, artist, album, year = self.now_playing.name, self.now_playing.artist,\
                                    self.now_playing.album, self.now_playing.year
        print('=' * 100)
        print('Artist: {:<10}\nName: {:<10}\nAlbum: {:<10}\nYear: {:<10}'.format(artist, name, album, year))
        print('=' * 100)

    def pause(self):
        pass

    def prev_song(self):
        self.play_index -= 1

        if self.play_index < 0:
            print('Beginning of the playlist.')
            return

        self.play()

    def next_song(self):
        self.play_index += 1

        if not self.playlist[self.play_index]:
            print('End of the playlist.')
            return

        self.play()

    def show_song_list(self) -> list:
        song_list = []
        for song in self.playlist.songs:
            print(song.name)
            song_list.append(song.name)
        return song_list

    def find_song(self, name, artist=None):
        if name not in self.show_song_list():
            print(f'No song named "{name}"')
            return
#         TODO:  complete this shit




class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.pop(self.songs.index(song))

    def load_songs(self, path):
        with open(path, 'r') as file:
            song_list = file.readlines()

            for song in song_list:
                artist, album, year, song_name = song.strip('\n').split('\t')
                self.songs.append(Song(song_name, artist, album, year))

class Song:
    def __init__(self, name, artist, album, year):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year


if __name__ == '__main__':

    import sys
    playlist = Playlist()
    playlist.load_songs('albums.txt')

    player = Player(playlist)
    # player.show_song_list()
    player.play()
    player.show_song_info()
    player.next_song()
    player.show_song_info()

    print(sys.version)