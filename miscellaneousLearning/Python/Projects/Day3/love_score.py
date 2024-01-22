print("The Love Calculator is calculating your score...")
first_name = input("What's your name? ")
second_name = input("What's their name? ")

combines = first_name + second_name
converted_case = combines.lower()
t = converted_case.count("t")
r = converted_case.count("r")
u = converted_case.count("u")
e = converted_case.count("e")
first_digit = t + r + u + e

l = converted_case.count("l")
o = converted_case.count("o")
v = converted_case.count("v")
e = converted_case.count("e")
second_digit = l + o + v + e

#🚨 Along we follow!
score = first_digit + second_digit

print(f"Your score is {first_digit}{second_digit}")
