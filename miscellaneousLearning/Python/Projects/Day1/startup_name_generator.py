#Greets the user
print("Hello, welcome to this startup name generator!\n")

#Records user's hometown
upbringing = input("What is your city of upbringing? ")

#Records user's chosen career field
career_field = input("What is your chosen career filed? ")

#Generates the startup name and prints it
startup_name = upbringing + " " +  career_field

#Delivers the Startup name
print(f'Your startup name is: "{startup_name}"')
