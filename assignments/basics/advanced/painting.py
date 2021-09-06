import math
length_cm = 50
degrees_str = input("Roof's angle in degrees: ")
degrees = int(degrees_str)
radians = math.radians(degrees)
radius = length_cm / math.cos(radians)
height_cm = math.sin(radians) * radius
print("To make the platform level, the height must be", round(height_cm, 1), "cm")