n = int(input("Input matrix size: "))

matrix = n * n

for i in range(1, matrix + 1):
    print(i, end=" ")
    
    if i % n == 0:
        print()
