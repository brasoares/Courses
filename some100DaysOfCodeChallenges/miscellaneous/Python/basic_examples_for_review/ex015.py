'''Ask the user to enter their favourite colour. 
If they enter “red”, “RED” or
“Red” display the message “I like red too”, 
otherwise display the message
“I don’t like [colour], I prefer red”.'''

colour = input("Enter your favourite colour: ")

entered_colour = colour.lower()

if entered_colour == 'red':
  print("I like red, too! :)")
else:
  print("I prefer red!") # Bit of a change, here.
