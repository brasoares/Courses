"""
Using the song “10 green bottles”, display the lines “There are [num] green bottles
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
should accidentally fall”. Then ask the question “how many green bottles will be
hanging on the wall?” If the user answers correctly, display the message “There will be
[num] green bottles hanging on the wall”. If they answer incorrectly, display the
message “No, try again” until they get it right. When the number of green bottles gets
down to 0, display the message “There are no more green bottles hanging on the wall”.
"""

num = 10

while num > 0:
    print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if 1 green bottle should accidently fall")
    while True:
        how_many = int(input("How many green bottles will be hanging on the wall? "))
        if how_many == num - 1:
            print(f"There will be {how_many} green bottles hanging on the wall.")
            break
        else:
            print("No, try again")
        if how_many == 0:
            print("There are no more green bottles hanging on the wall.")
            break
        else:
            num = how_many
