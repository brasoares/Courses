
print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L?")
add_pepperoni = input("Do you want pepperoni? Y or N?")
extra_cheese = input("Do you want extra cheese? Y or N?")

add_for_small = 2 
add_for_else = 3
add_extra_cheese = 1
small = 15
medium = 20
large = 25
bill = 0

if size[0] == 'S':
 bill = small
 if add_pepperoni[0] == 'Y':
  bill += add_for_small
 if extra_cheese[0] == 'Y':
  bill += add_extra_cheese
elif size[0] == 'M':
 bill = medium
 if add_pepperoni[0] == 'Y':
  bill += add_for_else
 if extra_cheese[0] == 'Y':
  bill += add_extra_cheese
else:
 bill += large
 if add_pepperoni[0] == 'Y':
  bill += add_for_else
 if extra_cheese[0] == 'Y':
  bill += add_extra_cheese 

print(f"Your final bill is: ${bill}.")
