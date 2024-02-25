'''
Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program.
'''
n = 0

while n < 6:
  n = int(input("Enter a number: "))

print(f"The last number you entered was a {n}.")
