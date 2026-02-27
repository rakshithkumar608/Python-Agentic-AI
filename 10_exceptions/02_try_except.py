chai_menu = {"masala" : 30, "ginger": 40}

try:
  chai_menu["lemon"]

except KeyError:
  print("Key 'lemon' not found in chai_menu")

print("This will be printed regardless of the exception")