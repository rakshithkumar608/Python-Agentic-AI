# value = 13
# reminder = value % 5

# if reminder:
#   


# value = 13

# if (remainder := value % 5):
#   print(f"Not divisible, reminder is {remainder}")



# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size:")) in available_sizes:
#   print(f"serving {requested_size}")
# else:
#   print(f"Size is unavailable - {requested_size}")



flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors:", flavors)

while (flavor := input("Choose your flavour:")) not in flavors:
  print(f"Sorry, {flavor} is not available")


  print(f"You choose {flavor} chai")