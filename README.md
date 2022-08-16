# [GUI] Guess the Number Game
Project made by PyAreSquare. Project took 2 hours to make, with 14 total attempts. This was made with the tkinter and random modules. 100% python.

## About 📝
This is a GUI (Graphical User Interface) version of the simple and well-known guess the number game. This was created in python and then converted into an exe format with the help of pyinstaller.

If you want to use pyinstaller, simple type
```
pip install pyinstaller
```
in cmd.exe to get pyinstaller on your windows system.

## Controls 🕹️
- Enter your guess on what the number is in the textbox. 
- Press 'reset the game.' to reset the game. (this will make the computer choose a different number)
- Press 'guess the number!' to submit your guess. Every time you press this with a integer in the textbox, the number of tires will increase by 1.

## Easter Eggs 🥚
Wich are basically hidden features that are for debugging and may be implemented in future updates.

if you create a file called 
```
max.txt in the assets directory
```
and give it an integer value like 1000, then 
the next time you start the game (or hit reset) the maximum value (the largest number that the computer caan randomly pick) will be set to that
amount. 

If you change the contents in 
```
max.txt in assets
```
to anything but an integer and then reset the game, the bottom line
will say 'stop messing with me.'
## Future Updates
I do plan on improving this project in the future - I really do! But, it gets kinda hard when all you have is a 250x110 pixel box, however, I will do my best to improve this and mayyybbee add a keypad? (perhaps?)
- I will make it so that if you enter the same text more than once, it will not count that as a 'try'
- I will make it so that there is a little counter on the top of the screen which tells you what range it is in. (I will elaborate on the next release)
- I might make it so that the program will ask the user what the maxium value should be. (RIP max.txt)
