'''
Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.
'''
num = int(input("Enter a number between (inclusive) 10 and 20: "))

if num > 9 and num < 21:
  print("Thank you!")
else:
  print("Incorrect answer.")
