import tkinter
# import kivy


# def hello(event):
#     play_button.configure(relief='raised')
#     text.set('I have been pressed!')
#
#
# def goodbye(event):
#     play_button.configure(relief='sunken')
#     text.set('Goodbye')
#     # print('Goodbye!')


# play_button = tkinter.Button(main_window, text='Play', font=("Helvetica", 16), width=10, height=1, relief='sunken')
#
# play_button.bind('<ButtonPress-1>', func=hello)
# play_button.bind('<ButtonRelease-1>', func=goodbye)
#
# play_button.grid(column=0, row=1)

# button_1 = tkinter.Button(main_window, text='Test', font=("Helvetica", 16), width=5, height=2, relief='flat')
# button_1.grid(column=1, row=0)
# button_2 = tkinter.Button(main_window, text='Test_2', font=("Helvetica", 16), width=5, height=2, relief='ridge')
# button_2.grid(column=2, row=0)
# button_3 = tkinter.Button(main_window, text='Test_3', font=("Helvetica", 16), width=5, height=2, relief='solid')
# button_3.grid(column=3, row=0)
#
# button_4 = tkinter.Button(main_window, text='Test_4', font=("Helvetica", 16), width=5, height=2, relief='sunken')
# button_4.grid(column=1, row=1, columnspan=2)
#
# button_5 = tkinter.Button(main_window, text='Test_5', font=("Helvetica", 16), width=5, height=2, background='#fc0f0f',
#                           foreground='#002fff')
# button_5.grid(column=0, row=1, rowspan=2)
#
# image = tkinter.PhotoImage(file='test_1.png')
# button_6 = tkinter.Button(main_window, image=image)  # width=100, height=100)
# button_6.grid(column=1, row=2)


def number_entry(event):
    existing_text = text.get()
    widget_text = event.widget['text']
    is_operator = False
    try:
        if existing_text[-1] in OPERATORS and widget_text in OPERATORS:
            # if widget_text in OPERATORS:
            #     return
            is_operator = True

    except IndexError:
        pass

    result = existing_text + widget_text if not is_operator else existing_text[:-1] + widget_text
    text.set(result)


def equals():
    expression = text.get()
    result = eval(expression)
    text.set(result)


main_window = tkinter.Tk()
main_window.title('Simplistic Calculator')
main_window.geometry('480x480')
main_window.configure(background='#b5b5b5')
main_window.resizable(width=False, height=False)

BUTTON_HEIGHT = 2
BUTTON_WIDTH = 10
OPERATORS = ['-', '+']

text = tkinter.StringVar()

display = tkinter.Entry(main_window, state='readonly', textvar=text)
display.grid(column=0, row=0, columnspan=3, sticky='ew', padx=100)

button_1 = tkinter.Button(main_window, text='1', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_1.grid(column=0, row=1)
button_1.bind('<Button-1>', func=number_entry)

button_2 = tkinter.Button(main_window, text='2', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_2.grid(column=1, row=1)
button_2.bind('<Button-1>', func=number_entry)

button_3 = tkinter.Button(main_window, text='3', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
button_3.grid(column=2, row=1)
button_3.bind('<Button-1>', func=number_entry)

plus_button = tkinter.Button(main_window, text='+', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
plus_button.grid(column=0, row=2)
plus_button.bind('<Button-1>', func=number_entry)

minus_button = tkinter.Button(main_window, text='-', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
minus_button.grid(column=1, row=2)
minus_button.bind('<Button-1>', func=number_entry)


equal_button = tkinter.Button(main_window, text='=', width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=equals)
equal_button.grid(column=2, row=2)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.rowconfigure(2, weight=1)

main_window.mainloop()
print('Program terminated')

# Grid geometry manager: https://tkdocs.com/tutorial/grid.html
