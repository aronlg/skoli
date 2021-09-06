k = int(input("Enter value for k: "))

current_sum = 0

previous_sum = 0

while current_sum <= k:
    term = int(input("Enter a value: "))
    previous_sum = current_sum
    current_sum += term
current_sum = previous_sum
print("Sum:", current_sum)