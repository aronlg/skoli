'''
    A quadratic equation has the form ax^{2} + bx + c = 0  with value a, b, and c, where a and b is any value and c is constant.
    To check whether the equation has a solution or not, quadratic formula for discriminant is used.
    
    The formula is given is: b^{2}-4ac 
    
    1. if the discriminant is positive b^{2}-4ac > 0, then the quadratic equation has "2 solutions".
    2. if the discriminant is equal b^{2}-4ac = 0, then the quadratic equation has "1 solution".
    3. if the discriminant is negative b^{2}-4ac < 0, then the quadratic equation has "No solutions".
    
    Write a program that prompts for three integers in a quadratic equation. 
    Find how many solutions this quadratic equation has, and print the result
'''

val_a_int = int(input("Enter the value for a: ")) # Do not change this line
val_b_int = int(input("Enter the value for b: ")) # Do not change this line
val_c_int = int(input("Enter the value for c: ")) # Do not change this line
 
d = ((val_b_int * val_b_int) - (4 * val_a_int * val_c_int))

if d > 0:
    print("2 solutions.")

elif d == 0:
    print("1 solution.")

else:
    print("No solutions.")