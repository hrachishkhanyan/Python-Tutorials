"""OOP ENCAPSULATION, INHERITANCE ETC."""

# 1. Coffee machine. Write a Coffee machine class. Details soon...

# 2. Remember our Music Player class? At this point it doesn't do much, as we can't really play music with it. Let's
# change that, and create a nice Music Player GUI with music playing functionality.
#    a) Let's create an interface. The way I've pictured it, is the song name at the top, then we'll have a seekbar,
#    then 4 buttons (play, pause, next, previous) and a listbox at the bottom that will contain our files. Feel free to
#    improvise, but I'll stick to this design.
#    b) Then we need some mechanism to play mp3 (or possibly other formats) files in our program. I've decided to use
#    python-vlc module for this as it provides much more useful stuff. Other options are pygame, playsound etc. Let's
#    just try to play an mp3 within our __main__. You can find a few music files provided with this project.
#    c) Great! We have a simple player at this point. Now, let's modify our Playlist class. More specifically the
#    load_songs method. Now it should contain the paths to the songs we have in a separate Music folder in our project.
#    d) So now we need to change the play method to actually play a song from the playlist.
#    e) Simple, isn't it? Now let's change the next_song and prev_song methods to actually go and play the next, or
#    previous songs in our Playlist.

