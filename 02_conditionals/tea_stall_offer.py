# A tea stall offers different prices for diffderent cup sizes.
# Write a program that calculates the price based on size.

# Task:
# * Input: "small", "medium", "large"
# * Small -> 10, medium->15, Large->20
# * if invalid: show "Unknown cup size"


cup = input("Choose your cup size (small/medium/large): ").lower()


if cup == "small":
  print("Price is ₹10")
elif cup == "medium":
  print("Price is ₹15")
elif cup == "large":
  print("Price is ₹20")
else:
  print("Unkown cup size")