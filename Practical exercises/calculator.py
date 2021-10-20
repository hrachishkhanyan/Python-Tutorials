import tkinter
import re
# from simpleeval import simple_eval

BUTTON_HEIGHT = 3
BUTTON_WIDTH = 5
FONT_SIZE = 10
SIGNS = ['*', '/', '+', '-']
there_is_dot = False


def number_entry(event):
    if text.get() == 'nan':
        clear()

    new_text = text.get()

    new_text += event.widget['text']

    text.set(new_text)


def sign_entry(event):
    global there_is_dot

    new_text = text.get()

    if not new_text and event.widget['text'] == '-':
        pass
    elif not new_text or new_text[-1] in SIGNS:  # re.match(r'\+|-|\*|\\', new_text[-1])
        return

    new_text += event.widget['text']
    text.set(new_text)
    # is_dot = not is_dot
    there_is_dot = False


def remove_zeros(exp):
    pattern = r'(\d+|[^ 0-9])'
    lst = re.split(pattern, exp)
    result = ''

    for element in lst:
        result += element.lstrip('0')

    return result


def evaluate():

    new_text = remove_zeros(text.get())

    # try:
    #     result = simple_eval(new_text)
    #     text.set(result)
    #
    # except ZeroDivisionError:
    #     text.set('nan')
    # except SyntaxError:
    #     return
    try:
        result = eval(new_text)
        text.set(result)
    except ZeroDivisionError:
        text.set('nan')
    except SyntaxError:
        return


def backspace():
    global there_is_dot

    new_text = text.get()

    if new_text[-1] in SIGNS:
        there_is_dot = True

    new_text = new_text[:-1]
    text.set(new_text)


def clear():
    text.set('')


def dot(event):
    global there_is_dot

    if there_is_dot:
        return
    print(event.widget['text'])
    new_text = text.get()

    new_text += event.widget['text']
    text.set(new_text)
    there_is_dot = True


main_window = tkinter.Tk()
main_window.title('Calculator')
main_window.geometry('360x480')
main_window.configure(background='#cbd6d6')
main_window.resizable(width=False, height=False)
text = tkinter.StringVar()
display = tkinter.Entry(main_window, width=40, textvariable=text, state='readonly')  # demonstrate eval problems
display.grid(row=0, column=0, columnspan=3, sticky='e')

buttons = {}
placement = ['en', 'n', 'wn']

for i in range(9, -1, -1):
    buttons[f'button_{i}'] = tkinter.Button(main_window, font=("Helvetica", FONT_SIZE), text=f'{i}', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
    buttons[f'button_{i}'].grid(row=i // 3 + 1, column=i % 3, sticky='n')

for button in buttons.values():
    button.bind('<Button-1>', lambda event: number_entry(event))

plus_button = tkinter.Button(main_window, text='+', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
plus_button.grid(column=3, row=1, sticky='n')
plus_button.bind('<Button-1>', lambda event: sign_entry(event))

minus_button = tkinter.Button(main_window, text='-', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
minus_button.grid(column=3, row=2, sticky='n')
minus_button.bind('<Button-1>', lambda event: sign_entry(event))

mult_button = tkinter.Button(main_window, text='*', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
mult_button.grid(column=3, row=3, sticky='n')
mult_button.bind('<Button-1>', lambda event: sign_entry(event))

div_button = tkinter.Button(main_window, text='/', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
div_button.grid(column=3, row=4, sticky='n')
div_button.bind('<Button-1>', lambda event: sign_entry(event))

equal_button = tkinter.Button(main_window, text='=', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=evaluate)
equal_button.grid(column=2, row=4, sticky='n')

clear_button = tkinter.Button(main_window, text='C', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=clear)
clear_button.grid(column=1, row=4, sticky='n')

backspace_button = tkinter.Button(main_window, text='<-', font=("Helvetica", FONT_SIZE), height=1, width=2, command=backspace)
backspace_button.grid(column=3, row=0, sticky='e')

dot_button = tkinter.Button(main_window, text='.', font=("Helvetica", FONT_SIZE), height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
dot_button.grid(row=5, column=1, columnspan=2)
dot_button.bind('<Button-1>', lambda event: dot(event))


main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)
main_window.rowconfigure(4, weight=1)
main_window.rowconfigure(5, weight=1)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)


main_window.mainloop()

# tkinter.Scrollbar
# tkinter.Listbox
