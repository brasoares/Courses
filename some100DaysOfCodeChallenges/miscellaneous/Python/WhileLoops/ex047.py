'''
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total.
'''

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter a second integer: "))

total = n1 + n2

choice = input("Do you wish to sum a new number? (Y/N) ").lower()
