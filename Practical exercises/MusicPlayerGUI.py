try:
    import Tkinter as tkinter
except ModuleNotFoundError as msg:
    print(msg)
    import tkinter

from tkinter import ttk
from tkinter.filedialog import askopenfilename
import vlc
from mutagen.mp3 import MP3


class Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('360x240')
        self.title('Music Player')
        self.iconbitmap('play.ico')
        self.resizable(False, False)

    def setup(self):

        global player

        menu = tkinter.Menu(self)
        file_menu = tkinter.Menu(menu, tearoff=0)
        file_menu.add_command(label='Add Song...', command=player.load_songs)
        menu.add_cascade(label='File', menu=file_menu)

        screen.config(menu=menu)
        player.setup_player()

class Player(tkinter.Frame):
    BUTTON_HEIGHT = 1
    BUTTON_WIDTH = 11

    def __init__(self, playlist, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.playlist = playlist
        self.now_playing_label = tkinter.StringVar(self, 'Nothing plays')
        self.now_playing_song = None
        self.media_player = vlc.MediaPlayer()
        self.progress_bar = ttk.Scale(self, from_=0, to=100, value=0)
        self.seeking = False
        self.listbox = tkinter.Listbox(self)
        self.play_index = 0

    def setup_player(self):
        # Setup the frame on main screen
        self.grid(column=0, row=0, sticky='ewns')
        # Setup buttons
        play_button = tkinter.Button(self, text='Play', command=self.play,
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH)
        play_button.grid(column=0, row=2, sticky='ew')

        pause_button = tkinter.Button(self, text='Pause', command=self.pause,
                                      height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH)
        pause_button.grid(column=1, row=2, sticky='ew')

        next_button = tkinter.Button(self, text='Next song', command=self.next_song,
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH)
        next_button.grid(column=2, row=2, sticky='ew')

        prev_button = tkinter.Button(self, text='Previous song', command=self.prev_song,
                                     height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH)
        prev_button.grid(column=3, row=2, sticky='ew')

        # Setup the now playing label
        now_playing_label = tkinter.Label(self, textvariable=self.now_playing_label)
        now_playing_label.grid(column=0, row=0, columnspan=4, sticky='ew')

        # setup the progress bar
        self.progress_bar.grid(column=0, row=1, columnspan=4, sticky='ew')
        self.progress_bar.bind("<ButtonRelease-1>", self.seek)
        self.progress_bar.bind("<Button-1>", self.pause)
        # setup a listbox and scrollbar
        scrollbar = tkinter.Scrollbar(self)

        self.listbox.grid(column=0, row=3, columnspan=4, sticky='ew')
        scrollbar.grid(column=3, row=3, sticky='esn')

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.bind('<Double-Button>', self.select_song)

        # populate the listbox with our songs from self.playlist
        # Setup a menu bar

    def progress(self, t):
        if self.seeking:
            return

        self.progress_bar.config(value=t)
        self.progress_bar.after(1000, lambda: self.progress(self.media_player.get_time() // 1000))

    def play(self, song=None):
        self.seeking = False

        if self.playlist.is_empty():
            return

        if str(self.media_player.get_state()) == 'State.Paused':
            self.media_player.set_pause(0)
        else:
            song_artist, song_name, self.play_index = (song.artist, song.name, song.song_id) if song \
                else (playlist.songs[self.play_index].artist, playlist.songs[self.play_index].name, self.play_index)

            song_path = '../Music/' + ' - '.join((song_artist, song_name)) + '.mp3'

            media = vlc.Media(song_path)

            self.media_player.set_media(media)
            self.media_player.play()
            self.now_playing_song = self.playlist.songs[self.play_index]

            self.now_playing_label.set(' - '.join((song_artist, song_name)))

        length = self.now_playing_song.length
        current_timestep = self.media_player.get_time() // 1000
        self.progress_bar.config(to=length)
        self.progress_bar.after(1000, lambda: self.progress(current_timestep))

    def seek(self, event):
        self.seeking = False

        if not self.now_playing_song:
            self.progress_bar.config(value=0)
            return

        timestamp = event.widget['value'] / self.now_playing_song.length
        self.media_player.set_position(timestamp)
        self.play(self.now_playing_song)

    def pause(self, _=None):
        self.seeking = True
        self.media_player.set_pause(1)

    def prev_song(self):

        if self.play_index < 1:
            print('Beginning of the playlist.')
            return
        self.play_index -= 1

        self.play()

    def next_song(self):

        if self.play_index >= len(playlist.songs) - 1:
            print('End of the playlist.')
            return

        self.play_index += 1

        self.play()

    def show_song_list(self) -> list:
        song_list = []
        for song in self.playlist.songs:
            print(song.name)
            song_list.append(song.name)
        return song_list

    def select_song(self, event):
        song_name = event.widget.get(event.widget.curselection())
        # TODO: Use find_song function here
        for song in self.playlist.songs:
            if ' - '.join((song.artist, song.name)) == song_name:
                self.play(song)
                self.now_playing_song = song

    def load_songs(self):
        file_path = askopenfilename(initialdir="./",
                                    title="Select a file...",
                                    filetypes=(('MP3 files', 'mp3'), ('All files', '*.*')))
        length = MP3(file_path).info.length

        file_name = file_path.split('/')[-1]
        artist, name = file_name.split('.')[0].split(' - ')
        self.playlist.songs.append(Song(name, artist, length, self.playlist.song_id))
        self.listbox.insert(tkinter.END, f'{artist} - {name}')

        self.playlist.song_id += 1


class Playlist:
    # TODO: Might inherit from tkinter.Listbox
    def __init__(self):
        self.songs = []
        self.song_id = 0

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.pop(self.songs.index(song))

    def is_empty(self):
        if not self.songs:
            return True

class Song:
    def __init__(self, name, artist, length, song_id, album=None, year=None):
        self.name = name
        self.artist = artist
        self.length = length
        self.song_id = song_id
        self.album = album
        self.year = year


if __name__ == '__main__':
    screen = Screen()
    playlist = Playlist()
    player = Player(playlist, screen)

    screen.setup()
    tkinter.mainloop()







