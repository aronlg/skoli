par = int(input("Par for hole: "))
score = int(input("Score on hole: "))

BOGEY = par + 1
DOUBLE_BOGEY = par + 2
BIRDIE = par - 1
EAGLE = par - 2

if score > par:
    if score == BOGEY:
        print("Bogey")
    elif score == DOUBLE_BOGEY:
        print("Double bogey")
    else:
        print("Bad score")
elif score < par:
    if score == BIRDIE:
        print("Birdie")
    elif score == EAGLE:
        print("Eagle")
    else:
        print("Unbelievable!")
else:
    print("Par")
