# Constants
STONE_TO_KG = 6.3503
POUND_TO_KG = 0.454
FEET_TO_CM = 30.48
INCH_TO_CM = 2.54
DECIMAL_DIGITS = 1

stones = int(input("Weight in stones: "))
pounds = int(input("Extra pounds: "))
feet = int(input("Height in feet: "))
inches = int(input("Extra inches: "))

kg = stones * STONE_TO_KG + pounds * POUND_TO_KG
cm = feet * FEET_TO_CM + inches * INCH_TO_CM
m = cm / 100
bmi = kg / (m * m)

print()
print("kg:", round(kg, DECIMAL_DIGITS))
print("cm:", round(cm, DECIMAL_DIGITS))
print("BMI:", round(bmi,DECIMAL_DIGITS))