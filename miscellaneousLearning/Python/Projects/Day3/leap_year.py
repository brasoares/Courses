#Receives the year to be checked:
year = int(input("Enter the year you want to check: "))

if year % 4 == 0:
 if year % 100 != 0 or year % 400 == 0:
  print(f"The provided year of {year} is a leap year.")
 else:
  print(f"The year of {year} is not a leap year.")
else:
 print(f"The year of {year} is not a leap year.")
