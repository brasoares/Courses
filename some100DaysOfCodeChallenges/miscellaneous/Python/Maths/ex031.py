'''
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius²).
'''
import math

radius = float(input("Please, provide the radius of a circle: "))
area = circle_radius = math.pi * pow(radius, 2)

print(f"Area: {area}.")
