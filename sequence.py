n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_1 = 0
num_2 = 1
num_3 = 2
count = 0

sum = num_1 + num_2 + num_3

while count < n:
    sum = num_1 + num_2 + num_3

    num_1 = num_2
    num_2 = num_3
    num_3 = sum

    count += 1

    print(num_1)
