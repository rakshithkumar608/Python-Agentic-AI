class OutOfIngredientsError(Exception):
    """Custom exception for when ingredients are out of stock."""
    pass
  
def make_chai(milk, sugar):
  if milk == 0 or sugar == 0:
    raise OutOfIngredientsError("Sorry, we're out of ingredients to make chai.")
  print("Your chai is ready!")
  
  
make_chai(0, 1)
