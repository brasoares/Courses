'''
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.
'''

n_count = int(input("How many people will be invited to the party? "))

if n_count < 10:
  for i in range(1, n_count+1):
    name = input(f"Tell me each name, person {i}: ")
    print(name)
else:
  print("Too many people")
