'''
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.
'''

users_name = input("Please, enter you first name: ")
times = int(input("Enter a number: "))
for i in range (0, times+1):
  print(users_name)
