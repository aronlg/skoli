# Write a program that, given seconds (int) as input, calculates hours, minutes, and seconds.
# For example, given 80000 seconds as input, the program outputs:
# 22 hours, 13 minutes, and 20 seconds.
# Hint 1: use integer division (//) and remainder (%)

secs_str = input("Input seconds: ")
secs_int = int(secs_str)

hours = secs_int // 3600
remainder = secs_int % 3600
minutes = remainder // 60
seconds = remainder % 60

print(hours,":",minutes,":",seconds)