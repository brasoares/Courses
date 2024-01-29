'''
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
'''

name = input("Enter your name: ")
surname = input("Enter your surname: ")

full_name = name + " " + surname

print(f"Hi,{full_name}! Your name has {len(full_name)-1} characters!")
