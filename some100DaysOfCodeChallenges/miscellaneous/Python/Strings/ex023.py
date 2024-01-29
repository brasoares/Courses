'''
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).
'''

'''
Example of one:
"Mary had a little lamb,
Its fleece was white as snow;
And everywhere that Mary went,
The lamb was sure to go."
'''

# Ask the user to type in the first line of a nursery rhyme
nursery_rhyme = input("Please, type in the first line of a nursery rhyme: ")

# Display string's length
print(f"The length of the string is {len(nursery_rhyme)}.")

# Ask for a starting number and an ending number
start = int(input("Please, enter a starting number: "))
end = int(input("Please, enter an ending number: "))

# Display just that section of the text
print(f"The requested section is: {nursery_rhyme[start:end]}.")

'''
"{nursery_rhyme[start:end]}" is a string slicing operation in Python.
For example, if nursery_rhyme is "Mary had a little lamb" and start is 18 and end is 22,
then "{nursery_rhyme[start:end]}" will return: "lamb."
'''
