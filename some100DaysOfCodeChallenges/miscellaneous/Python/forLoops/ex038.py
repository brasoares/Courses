'''
Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.
'''
name = input("Please, enter your name: ")
times = int(input("Enter the number of time you want to see your name letter by letter: "))

for char in name:
  print(char)
