'''
Set the total to 0 to start with. While the total is 50 or less, ask
the user to input a number. Add that number to the total and
print the message “The total is… [total]”. Stop the loop when
the total is over 50.
'''

number = 0

while number <= 50:
  number = int(input("Input a positive number: "))
  print(f"The total is... [{number}]")
