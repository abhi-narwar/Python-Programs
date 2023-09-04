import math

# Ask the user for the radius and height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the volume of the cylinder
volume = math.pi * radius**2 * height

# Display the result
print(f"The volume of the cylinder is {volume:.2f}")
