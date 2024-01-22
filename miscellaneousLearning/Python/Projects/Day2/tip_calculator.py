#Welcome prompt
print("Welcome to this tip calculator!\n")

#Request the total amount of the meal
price = input("How much is your meal? $")

#Requests the number of people to split the check into
persons = input("How many people will share the bill? " )
persons = int(persons)

#Requests the tip percentage on top of the bill
prctg = input("How much tip will you pay? 10%, 12% or 15%? " )

#Convert the value into percentage (decimals actually)
prctg = int(prctg) / 100

#Calculates the tip base amount
tip_percentage = float(price) * prctg

#Calculates the tip amount per person
tip_per_person = round (tip_percentage / persons, 2)

#Calculates the total bill amount per person
total_per_person = round((float(price) + tip_percentage)  / persons, 2)

#Displays the results
print(f"The tip amount to pay per person: ${tip_per_person}, while the total amount per person is of ${total_per_person}")
