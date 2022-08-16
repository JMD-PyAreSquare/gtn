# [GUI] Guess the Number Game
Project made by PyAreSquare.

## About 📝
This is a GUI (Graphical User Interface) version of the simple and well-known guess the number game. This was created in python and then converted into an exe format with the help of pyinstaller.

If you want to use pyinstaller, simple type
```
pip install pyinstaller
```
in cmd.exe to get pyinstaller on your windows system.

## Controlls 🕹️
Press 'reset the game.' to reset the game. (this will make the computer choose a different number)

Press 'guess the number!' to submit your guess. every time you press this, the number of tires will increase by 1.

## Easter Eggs 🥚
Some hidden features for debugging and may be implemented in future updates.

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
