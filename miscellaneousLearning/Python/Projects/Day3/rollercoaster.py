print("Welcome to the rollercoaster!")
height = int(input("So, tell me your height in cm? "))

if height >= 120:
 print("You can ride the rollercoaster!")
 age = int(input("What is your age? "))
 if age < 12:
  print("Please, pay $5.")
 elif age <= 18:
  print("Please, pay $7.")
 else:
  print("Please, pay $12.")
else:
 print("Oh, you gotta grow taller first; see yah!")
