sequence_length = int(input("Length of sequence: "))
step_size = int(input("Step size: "))

interval = 0
count = 0

while count < sequence_length:
    interval += step_size
    count += 1

    print(interval)
