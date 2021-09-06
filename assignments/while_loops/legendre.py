import math 

n = int(input("Enter a number: "))
print("Primes in the range", n*n, "and", (n+1)*(n+1), "are:")

i = n*n
while i < ((n+1)*(n+1)):
    is_prime = True

    j = 2
    while j <= int(math.sqrt(i))+1:
        if i % j == 0:
            is_prime = False
            break
        j += 1

    if is_prime:
        print(i)
    i += 1