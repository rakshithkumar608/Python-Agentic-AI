# Improving Readability

# You sell different chai size
# Instead of writing formulas everywhere. create a function.

# Task:
# * Write calculate_bill(cups, price_per_cup)
# * Return total bill
# * Use this function for multiple orders


def calculate_bill(cups, price_per_cup):
 return cups * price_per_cup

my_bills = calculate_bill(3, 45)
print(f"Total Bill:{my_bills}") # calling fuction 


# direct calling function iun one line
print("Order for tabel 2:", calculate_bill(4, 67))