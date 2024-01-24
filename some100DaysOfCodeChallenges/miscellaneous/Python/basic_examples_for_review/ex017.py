'''
Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn how to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick-
or-Treating”.
'''

age = 0

while age <= 0:
  age = int(input("How old are you? "))

if age >= 18:
  print("You can vote")
elif age == 17:
  print("You can learn how to drive")
elif age == 16:
  print("You can go to the movies!") # You can go to the movies!
else:
  print("You can go Trick-or-Treating!")
