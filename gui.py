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

def check():
    global tries
    guess = guessbox.get()

    try:
        guess = int(guess)
        if guess == number:
            tries += 1
            lb1.config(text='You guessed correctly!')
            lb2.config(text=f'You took {tries} tries.')
        elif guess < number:
            tries += 1
            lb2.config(text=f'pick a number that is greater than {guess}')
        elif guess > number:
            tries += 1
            lb2.config(text=f'pick a number that is less than {guess}')
    except:
        lb2.config(text='choose an INTEGER')
    guessbox.delete(0, END)

def reset():
    global maximum
    global number
    global tries

    
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
        
    tries = 0
    number = random.randint(0, maximum)

    lb1.config(text=f'Guess a number between 0 and {maximum},')
    lb2.config(text='use the texbox and button to guess.')
    if errorcheck == 1:
        lb2.config(text='stop messing with me.')

maximum = 0
number = 0
tries = 0


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