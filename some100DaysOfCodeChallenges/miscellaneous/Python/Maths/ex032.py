'''
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
'''
from decimal import Decimal, ROUND_HALF_UP
import math

radius = Decimal(input("Enter the cylinder's radius: "))
depth = Decimal(input("Enter the cylinder's depth: "))

circle_area = math.pi * radius ** 2
volume = circle_area * depth

# Rounding the volume
round_volume = volume.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

print(f"Total volume: {round_volume:.3f}")
