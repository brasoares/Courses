'''
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
'''

print("All in lower case, please:")
name = input("Enter your name: ").title()
surname = input("Enter your surname: ").title()

full_name = name + " " + surname
print(full_name)
