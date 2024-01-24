'''
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.
'''

num = float(input("Enter a number: "))

if num < 10:
  print("Too low")
elif num < 21:
  print("Correct")
else:
  print("Too high")
