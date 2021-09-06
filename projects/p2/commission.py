PRINTER_PRICE = 150
PAPER_PRICE = 10
PRINTER_COMMISION = 0.30
PAPER_COMMISION = 0.15
PAPER = "paper"
PRINTER = "printer"
PROMPT = PAPER + " or " + PRINTER + ": "
ADD_SALE = "Would you like to add a sale (y/n)?: "

total_commission = 0
total_sales = 0
print('Welcome to Dunder Mifflin!')

user_input = input(ADD_SALE)
while user_input.lower() == 'y':
    type_of_sale = input(PROMPT)
    if type_of_sale.lower() == PAPER:
        amount = int(input("# of paper piles: "))
        total_commission += PAPER_PRICE * amount * PAPER_COMMISION
        total_sales += 1
    elif type_of_sale.lower() == PRINTER:
        amount = int(input("# of printers: "))
        total_commission += PRINTER_PRICE * amount * PRINTER_COMMISION
        total_sales += 1
    else:
        print("You did neither type in", PAPER, "nor", PRINTER)
    
    print("You've made", round(total_commission), "today with", total_sales, "sales")
    user_input = input(ADD_SALE)
