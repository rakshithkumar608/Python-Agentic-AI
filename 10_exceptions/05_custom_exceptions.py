def brew_chai(flavor):
  if flavor not in ["masala", "ginger", "elaichai"]:
    raise ValueError(f"Sorry, we don't have {flavor} chai on the menu.")
  print(f"Brewing {flavor} chai for you!")
  
  
brew_chai("mint")