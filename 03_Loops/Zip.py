# You're preparing an order summery with customer names and theri total bill.
# Task:
# * Use two lists: one for names and one for bills.
# * Print: "[Name] paid [amount]"


names = ["RK", "JK", "AJ", "RJ"]
bills = [400, 500, 700, 900]

for name, amount in zip(names, bills):
  print(f"{name} Paid {amount} ruppess")