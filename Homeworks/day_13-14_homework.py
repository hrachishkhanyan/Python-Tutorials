"""OOP, GUI WITH TKINTER"""

# 1. Music Player:
# Okay, time to get our music player working!
#    a) Now, lets incorporate all of our GUI stuff into our Player class. Create a method named setup, which will
#    take care of placing all of the widgets on the main window. So you will need to create your widgets, grid them
#    and bind them inside of this method. After this, in our if __name__ == '__main__' clause, we'll have something like
#    this:
#
# main_window = tkinter.Tk()
# main_window.title('Music Player')
# main_window.geometry('360x240')
# main_window.iconbitmap('./Practical exercises/play.ico')
# main_window.resizable(width=False, height=False)
#
# playlist = Playlist()
# player = Player(playlist)
#
# main_window.mainloop()
#
#    and voila! The player will appear along with its widgets.
#    b) Install the vlc module (or any other similar library you prefer). Using this module, we should be able to
#    play a song whenever we press the play button. Implement the play and stop methods to play and stop a real song.
#    c) Now, create a folder named Music and put your favourite mp3-s in there. With the load_songs method in our
#    playlist class you should read the titles of the songs and add them to the listbox. You can bind a command to the
#    listbox using the bind method. Bind a method on double-click. This method should play the song that was clicked.
#    d) Modify next_song and prev_song methods, which will now look into the listbox and go to the next song and the
#    previous song respectively.
#    e) (Optional) Create a seeker. Seeker will be a ttk.Scale object. When we slide the seeker and place it somewhere,
#    the song should continue to play from there. This may be hard to implement at first...
#    f) (Optional) Finally, you can create a new class called Screen, which will take care of the setup in a) e.g.
#    it will define the geometry, thhe icon, the title, resizability and so on. After this, your mainprogram will look
#    like this:
#
# screen = Screen()
# playlist = Playlist()
# player = Player(playlist, screen)
# screen.setup()
# screen.mainloop()
#
#    Pay attention that the Screen class has the mainloop() method as it inherits from tkinter.Tk class.
#
# Again, feel free to do everything in a way you want to do it as these are just guidelines for you.
# Good luck and have fun!


# 1. Music Player:
# Վերջապես փոփոխենք մեր նվագարկիչը, որպեսզի այն աշխատի ինչպես պետք է․
#    a) Առաջին քայլով, փորձեք ամբողջ GUI-ն դարձնել մեր Player կլասի պատասխանատվությունը. Ստեղծեք setup մեթոդ, որը
#    պատասխանատու կլինի մեր բոլոր widget-ները main_window-ին կցելու համար։ Հետևաբար պետք է բոլոր widget-ները,
#    grid-ով դրանց կցելը և մեթոդ փոխանցելը պետք է արվի setup-ում։ Այս քայլից հետո մեր if __name__ == '__main__'-ի մեջ,
#    մենք կունենանք նման կոդ:
#
# main_window = tkinter.Tk()
# main_window.title('Music Player')
# main_window.geometry('360x240')
# main_window.iconbitmap('./Practical exercises/play.ico')
# main_window.resizable(width=False, height=False)
#
# playlist = Playlist()
# player = Player(playlist)
#թղթապանակ
# main_window.mainloop()
#
#    և մեր նվագարկիչը կհայտնվի էկրանին իր բոլոր կոճակներով։
#    b) Ներբեռնեք vlc մոդուլը (կամ նմանատիպ այլ գրադարան, եթե ցանկանում եք)։ Այս գրադարանի միջոցով մենք կկարողանանք
#    միացնել mp3 ֆորմատով երգեր։ Մոդիֆիկացրեք play ու stop մեթոդները, որպեսզի դրանք սեղմելուց միանան իսկական երգեր։
#    c) Այժմ ստեղծեք Music անունով պանակ և դրա մեջ ավելացրեք ձեր սիրած mp3 ֆայլերը։ Playlist կլասի load_songs մեթոդը
#    պետք է կարդա այդ ֆայլերի անունները և դրանք տեղադրի listbox-ի մեջ։ listbox-ին կարող ենք bind անել մեթոդ։
#    Double-click event-ի համար bind արեք մեթոդ, որը կվերցնի սեղմված երգի անունը և կմիացնի այդ երգը։
#    d) Մոդիֆիկացրեք next_song և prev_song մեթոդները, որոնք արդեն կփնտրեն listbox-ում հաջորդ և նախորդ երգերը և կմիացնեն
#    դրանք։
#    e) (Լրացուցիչ) Ստեղծեք seeker. Seeker-ը կարող է լինել ttk.Scale օբյեկտ։ Երբ seeker-ը սահեցնենք որոշակի հատվածի վրա,
#    երգը պետք է շարունակվի այդ մասից (եթե բերեցինք 30 տոկոսի վրա, պետք է հաշվենք երգի տևողության 30 տոկոսը և երգը
#    շարունակենք այդտեղից։
#    f) (Լրացուցիչ) Վերջապես կարող եք ստեղծել Screen կլաս, որը կհոգա player-ի առաջնային setup-ի մասին։ Այսինքն
#    կսահմանի երկրաչափությունը, ծրագրի նկարը, վերնագիրը և այլն։ Դրանից հետո մեր աշխատացնող կոդը կունենա հետևյալ տեսքը։
#
# screen = Screen()
# playlist = Playlist()
# player = Player(playlist, screen)
# screen.setup()
# screen.mainloop()
#
#    Ուշադրություն դարձրեք, որ Screen()-ը ունի mainloop() մեթոդը։ Հետևաբաև այն ժառանգում է tkinter.Tk կլասից։
#
# Այս քայլերն ընդամենը ուղեցույց են։ Կարող եք այս ամենը սարքել ինչպես կամենաք։ Բոլորիդ հաջողությու՛ն :)



