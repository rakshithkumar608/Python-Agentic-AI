def process_order(item, quantity):
  try:
    price = {"masala": 20, "ginger" : 25}["masala"]
    cost = price * quantity
    print(f"The cost of {quantity} {item} chai is: {cost}")
  except KeyError:
    print(f"Sorry, we don't have {item} chai on the menu.")
  except TypeError:
    print("Quantity must be a number.")
    
    
process_order("ginger", 2)
process_order("masala", "two")
