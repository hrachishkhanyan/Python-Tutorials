import tkinter
import os
import random
from tkinter import ttk
import vlc  # pygame
# from mutagen.mp3 import MP3


class Player:
    def __init__(self, playlist):
        self.playlist: Playlist = playlist
        self.is_playing = False
        self.now_playing_song = ''
        self.media_player = vlc.MediaPlayer()
        # self.now_playing_index = 0

    def __str__(self):
        return f'This player has a playlist containing {len(self.playlist.song_list)} songs'

    def play(self, play_index=0):
        if play_index > len(self.playlist.song_list):
            print(f'No song at index {play_index}')
            return

        if not self.is_playing:
            # self.now_playing_index = play_index
            media = vlc.Media('./Music/Faun - Von Den Elben.mp3')

            self.media_player.set_media(media)
            self.media_player.play()

            self.is_playing = True
            # self.now_playing_song = self.playlist.song_list[play_index]
            # print('=' * 50)
            # print(f'Now playing:\n{self.now_playing_song}')
            # print('=' * 50)
        else:
            print('The player is already active')

    def stop(self):
        if not self.is_playing:
            print('The player is not active')
        else:
            self.is_playing = False
            self.media_player.set_pause(1)
            print('The player has been stopped')

    def show_current_song_info(self):
        print('=' * 50)
        print(self.now_playing_song)
        print('=' * 50)

    def next_song(self):
        index = self.playlist.song_list.index(self.now_playing_song)
        if index < len(self.playlist.song_list) - 1:
            self.is_playing = False
            self.play(index + 1)
        else:
            print('We have reached the end of our playlist')

    def prev_song(self):
        index = self.playlist.song_list.index(self.now_playing_song)
        if index > 0:
            self.is_playing = False
            self.play(index - 1)
        else:
            print('We have reached the beginning of our playlist')

    def shuffle(self):
        shuffled = self.playlist.song_list.copy()
        shuffled.remove(self.now_playing_song)

        random.shuffle(shuffled)
        shuffled.insert(0, self.now_playing_song)

        self.playlist.song_list = shuffled


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

    def add_song(self, artist, album, year, name):
        for song in self.song_list:
            if song.name == name and song.artist == artist and song.year == year and song.album == album:
                print('The song is already in playlist')
                return

        self.song_list.append(Song(artist, album, year, name))

    def remove_song(self, artist, album, year, name):
        for song in self.song_list:
            if song.name == name and song.artist == artist and song.year == year and song.album == album:
                self.song_list.remove(song)
                break
        else:
            print('Song is not in playlist')

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


if __name__ == '__main__':
    # Setting up some constants
    BUTTON_HEIGHT = 1
    BUTTON_WIDTH = 11

    playlist = Playlist()
    player = Player(playlist)

    # Setting up the main window
    main_window = tkinter.Tk()
    main_window.title('Music Player')
    main_window.geometry('346x240')
    main_window.iconbitmap('./Practical exercises/play.ico')
    main_window.resizable(width=False, height=False)
    # Setting up the label
    status = tkinter.StringVar(value='Nothing plays')
    label = tkinter.Label(main_window, textvar=status)
    label.grid(column=0, row=0, columnspan=4, sticky='ew')

    # Creating the seeker
    seeker = ttk.Scale(main_window)
    seeker.grid(column=0, row=1, columnspan=4, sticky='ew')

    # Setting up the buttons
    play_button = tkinter.Button(main_window, text='Play', height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                 command=player.play)
    play_button.grid(column=0, row=2, sticky='ew')

    pause_button = tkinter.Button(main_window, text='Pause', height=BUTTON_HEIGHT, width=BUTTON_WIDTH,
                                  command=player.stop)
    pause_button.grid(column=1, row=2, sticky='ew')

    next_button = tkinter.Button(main_window, text='Next song', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    next_button.grid(column=2, row=2, sticky='ew')

    prev_button = tkinter.Button(main_window, text='Previous song', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    prev_button.grid(column=3, row=2, sticky='ew')

    # Setting up the listbox with its scrollbar
    listbox = tkinter.Listbox(main_window)
    listbox.grid(column=0, row=3, columnspan=4, sticky='ew')

    scrollbar = tkinter.Scrollbar(main_window)
    scrollbar.grid(column=3, row=3, sticky='esn')

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # with open('./Homeworks/random_words.txt') as words:
    #     for index, word in enumerate(words.readlines()):
    #         listbox.insert(index, word)

    # media_player = vlc.MediaPlayer()
    # media = vlc.Media('Music/Faun - Von Den Elben.mp3')
    #
    # media_player.set_media(media)
    # media_player.play()

    main_window.mainloop()


# pip install --upgrade pip
