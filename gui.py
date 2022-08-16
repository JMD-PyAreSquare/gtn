import random
from tkinter import *

root = Tk()
root.title('guess the number')
try:
    root.iconbitmap('assets/q.ico')
except:
    pass
root.config(bg='lightblue')

root.geometry('250x110')
root.minsize(250, 110)
root.maxsize(250, 110)
guesses = []

def sizereset():
    global popupwindow
    global sizebox
    try:
        maxfile = open('assets/max.txt', 'w')
        maxfile.write(sizebox.get())
        maxfile.close()
    except FileNotFoundError:
        maxfile = open('assets/maxfile.txt', "x")
        maxfile.write(sizebox.get())
        maxfile.close()
    popupwindow.destroy()
    reset()

def popup():
    global popupwindow
    global sizebox
    popupwindow = Toplevel(root)
    popupwindow.title("Settings")
    popupwindow.geometry("200x75")
    popupwindow.maxsize(200,75)
    popupwindow.minsize(200,75)
    popupwindow.config(bg='lightblue')
    sizebox = Entry(popupwindow, width=30, bd=3,bg='skyblue')
    button1 = Button(popupwindow, text = "Ok",bg='skyblue', command = sizereset)
    sizebox.pack(padx=5,pady=5)
    button1.pack(padx=5,pady=5)
    popupwindow.mainloop()

def check():
    global tries
    global guesses
    global lower
    global higher

    guess = guessbox.get()

    try:
        guess = int(guess)
        if guess == number:
            lb1.config(text='You guessed correctly!')
            lb2.config(text=f'You took {tries} tries.')
        elif guess < number:
            lower = guess
            lb1.config(text=f'Guess a number between {lower} and {higher},')
            lb2.config(text=f'pick a number that is greater than {guess}')
        elif guess > number:
            higher = guess
            lb1.config(text=f'Guess a number between {lower} and {higher},')
            lb2.config(text=f'pick a number that is less than {guess}')
        if guess not in guesses:
            guesses.append(guess)
            tries += 1
    except:
        lb2.config(text='choose an INTEGER')
    guessbox.delete(0, END)

def reset():
    global maximum
    global number
    global tries
    global guesses
    global lower
    global higher

    guesses.clear()
    errorcheck = 0
    
    try:
        maxfile = open('assets/max.txt')
        maximum = int(maxfile.read())
        maxfile.close()
    except FileNotFoundError:
        maximum = 100
    except:
        maxfile = open('assets/max.txt', 'w')
        maxfile.write('100')
        maxfile.close()
        errorcheck = 1

    lower = 0   
    tries = 0
    number = random.randint(0, maximum)
    higher = maximum

    lb1.config(text=f'Guess a number between 0 and {maximum},')
    lb2.config(text='use the texbox and button to guess.')
    if errorcheck == 1:
        lb2.config(text='stop messing with me.')

maximum = 0
number = 0
tries = 0
lower = 0
higher = maximum

menubar = Menu(root)
root.config(menu=menubar)
options = Menu(menubar, tearoff=0)
menubar.add_cascade(label="options", menu=options)
options.add_command(label='change limit', command = popup)

lb1 = Label(root, text=f'Guess a number between 0 and {maximum},',bg='lightblue')
lb1.pack()
lb2 = Label(root, text='use the texbox and button to guess.',bg='lightblue')
lb2.pack()
guessbox = Entry(root, bd=3, width=30,bg='skyblue')
guessbox.pack(padx=3,pady=3)
enter = Button(root,bd=3, text='Guess the number!',bg='skyblue', command=check)
enter.pack(side='left', expand=True)
gamereset = Button(root,bd=3, text='Reset the game.',bg='skyblue', command=reset)
gamereset.pack(side='right', expand=True)

reset()
root.mainloop()
