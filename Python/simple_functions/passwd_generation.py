import string
import random


def generate_password(length):
    # Define the character set excluding 'W' and 'w'
    characters = string.ascii_letters + string.digits + string.punctuation
    characters = characters.replace("W", "").replace("w", "")

    # Generate the password
    password = "".join(random.choice(characters) for _ in range(length))
    return password


# Set the desired length for the password
password_length = 144
generated_password = generate_password(password_length)
print(f"Generated password: {generated_password}")
