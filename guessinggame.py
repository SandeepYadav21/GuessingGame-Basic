import random

sysGuess = random.randint(0,100)

while True:
    userGuess = int(input("Guess a number between 0-100:"))
    if userGuess > sysGuess:
        print("Guess lower")
    elif userGuess < sysGuess:
        print("Guess higher")
    else:
        print("Congrats,you've guessed the correct number")
        break
