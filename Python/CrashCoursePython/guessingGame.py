import sys
guessn = 33
guess = 0
while guess < guessn or guess > guessn:
    guess = int(input("Qual é o número? "))
    if guess == guessn:
        print("You're right! Your guess is correct! Congrats!")
        sys.exit()
    elif guess < guessn:
        print("Guess Higher")
    else:
        print("Guess Lower")
