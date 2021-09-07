INPUT_NUMBER = "Input an integer (0 to quit): "

sum_even = 0
sum_odd = 0
count_even = 0
count_odd = 0

num = int(input(INPUT_NUMBER))

while num != 0:
    if num >= 0:
        if num % 2 == 0:
            sum_even += num
            count_even += 1

        else:
            sum_odd += num
            count_odd += 1

    else:
        print("Ignoring this negative number!")

    num = int(input(INPUT_NUMBER))

print("Sum of even:", sum_even)
print("Sum of odd:", sum_odd)
print("Even count:", count_even)
print("Odd count:", count_odd)
