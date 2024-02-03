'''
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
'''

import math

radius = float(input("Enter the cylinder's radius: "))
depth = float(input("Enter the cylinder's depth: "))

circle_area = math.pi * pow(radius, 2)
volume = circle_area * depth

print(f"Total volume: {volume:.3f}")
