# Import the sqrt function from the math module
from math import sqrt

# Prompt the user to enter the length of side A
a = float(input("What is the length of side A? "))

# Prompt the user to enter the length of side B
b = float(input("What is the length of side B? "))

# Calculate the length of side C using the Pythagorean theorem (C^2 = A^2 + B^2)
c = sqrt((a**2)+(b**2))

# Round the calculated length of side C to 2 decimal places
c2 = round(c, 2)

# Print the calculated length of side C
print("The length of side C is: ", c2)
