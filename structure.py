import random

try:
    maxfile = open('assets/max.txt')
    maximum = int(maxfile.read())
    maxfile.close()
except:
    maximum = 100

guess = -1
number = random.randint(0, maximum)

while guess != number:
    print(f'Guess a number between 0 and {str(maximum)}')
    guess = input()
    try:
        guess = int(guess)
        errorhandle = 0
    except:
        errorhandle = 1

    while errorhandle == 1:
        print('choose an INTEGER')
        guess = input()
        try:
            guess = int(guess)
            errorhandle = 0
        except:
            errorhandle = 1

    guess = int(guess)

    if guess == number:
        print('You guessed correctly!')
    elif guess < number:
        print(f'Pick a number that is greater than {guess}')
    elif guess > number:
        print(f'Pick a number that is less than {guess}')