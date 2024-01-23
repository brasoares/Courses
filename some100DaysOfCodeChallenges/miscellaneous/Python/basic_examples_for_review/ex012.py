'''
Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second.
'''

num1 = float(input("Please, provide the first number: "))
num2 = float(input("Please, provide the second number: "))

if num1 > num2:
  print(f"{num2:.0f}, {num1:.0f}.")
else:
  print(f"{num1:.0f}, {num2:.0f}.")
