import sys
import random

while True:
    guessn = random.randint(1,99)
    userNum = 0
    while userNum < guessn or userNum > guessn:
        userNum = int(input("Qual é o número? "))
        if userNum == guessn:
            print("You're right! Your guess is correct! Congrats!\n")
            ctrl = input("Do you want to play again? Type 'yes' or 'no'\n")
            if ctrl == 'yes':
                break
            else:
                print("Thanks for playing! You rock!")
                sys.exit()
        if userNum < guessn:
            print("Guess Higher")
        else:
            print("Guess Lower")
