'''
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.
'''

total = 0
n = 0

for i in range(total):
  if i < 4:
    n = int(input("Enter a number: "))
    total += n
  elif i == 4:
    choice = input("Do you want to include the last input in the sum? (Y or N): ")
    if choice.lower() == 'y':
      total += n
      print(f"{total}")
else:
  print(total)
    
