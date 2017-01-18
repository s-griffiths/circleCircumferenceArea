# Circles.py
# Prints the circumference and area of a circle based off of an input diameter

# Imports math library
import math

# Prompts the user for the diameter
diameter = float(input("Enter the diameter of a circle: "))

# Computes the radius of the circle
radius = diameter / 2

# Computes the circumference of the circle
circumference = 2 * math.pi * radius

# Computes the area of the circle
area = math.pi * math.pow(radius, 2)


# Prints the circumference and area of the circle
print("The circle's circumference is {:.2f}.".format(circumference))
print("The circle's area is {:.2f}.".format(area))
