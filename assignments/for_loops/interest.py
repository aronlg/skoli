initial_amount = float(input("Enter the initial amount: "))
interest = float(input("Enter the interest(%): "))
years = int(input("Enter for how many years: "))

current_amount = initial_amount
for _ in range(years):
    current_amount += current_amount * (interest/100)

print(f"Amount after {years} years: {round(current_amount, 2)}")
