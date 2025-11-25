# You run an online tea store.
# if the order amount is more than ₹300, delivary is free;
# otherwiss, it costs ₹30.

# Task:
# *Input: order_amount
# *Use ternary operator to decide delivary fee

order_amount = int(input("Enter the order amount: "))


# Turnary operator
delivary_fees = 0 if order_amount > 300 else 30

print(f"Delivary fees is : {delivary_fees}")

