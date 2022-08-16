# [GUI] Guess the Number Game 2
The second release of the GUI version of guess the number. 100% python.

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
- Use the 'change limit' in the options menu to change the 'limit' (the highest or largest number that the computer can pick)

## Future Updates ↗️
- Add more options in the options menu
- Make the game more customizable
- Add a keypad (visualize the game)

## Updates 📰
- The program tells you the range that the number is in, this updates whenever you guess.
- Now you can change the limit without manually editing max.txt in assets.
- Whenever you guess the same number twice, or when you put a non-integer in the textbox, it will not count it as a try.
