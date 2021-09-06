n = int(input("Enter how many numbers you want to input(>0): "))


min_num = float("inf")  # Everything is lower than this
max_num = float("-inf") # Everything is higher than this
for i in range(n):
    number = int(input("Enter an integer: "))
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number

print("Highest number from input:", max_num)
print("Lowest number from input:", min_num)