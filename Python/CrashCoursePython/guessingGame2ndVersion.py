import sys
import random
guessn = random.randint(1,99)
userNum = 0
while userNum < guessn or userNum > guessn:
    userNum = int(input("Qual é o número? "))
    if userNum == guessn:
        print("You're right! Your guess is correct! Congrats!")
        sys.exit()
    elif userNum < guessn:
        print("Guess Higher")
    else:
        print("Guess Lower")
