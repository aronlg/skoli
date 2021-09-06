'''
    Heron's formula gives the area, A, of a triangle with sides a,b,c as:
    A=√(s(s−a)(s−b)(s−c))
    where s=½(a+b+c).

    Write a program that prompts for three floats, denoting the lengths of
    the sides of a triangle. 
    Calculate the area, and print the result.
    Hint: You can use the sqrt function in the math module.
'''

val_a_str = input("Enter the value for a: ") # Do not change this line
val_b_str = input("Enter the value for b: ") # Do not change this line
val_c_str = input("Enter the value for c: ") # Do not change this line

# Fill in the missing code below
# Import module
import math 
# Convert values to float
val_a_float, val_b_float, val_c_float = float(val_a_str), float(val_b_str), float(val_c_str)

s = (val_a_float + val_b_float + val_c_float) / 2
area = math.sqrt(s * (s - val_a_float) * (s - val_b_float) * (s - val_c_float))
print("The area of the triangle is", area) # Do not change this line