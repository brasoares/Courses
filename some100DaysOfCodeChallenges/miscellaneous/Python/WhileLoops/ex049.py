'''
Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.
'''
copnum = 50
number = 0
i = 0

while True:
    number = int(input("Enter a number: "))
    i += 1
    
    if number == copnum:
        print(f"Well done, you took {i} attempts")
        break
    elif number < copnum:
        print("Too low")
    else:
        print("Too high")
