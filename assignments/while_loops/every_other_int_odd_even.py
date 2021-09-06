num_int = int(input("Enter a number: ")) # Do not change this line

# Fill in the missing code below
if num_int < 1:
    print("The number is too small.")
else:
    if num_int % 2 == 0:
        c = 2
    else:
        c = 1
        
    while c <= num_int:
        print(c)
        c += 2