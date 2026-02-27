def serve_chai(flavor):
  try:
    print(f"Serving {flavor} chai for you!")
    if flavor == "unknown":
      raise ValueError("Sorry, we don't have that flavor of chai.")
  except ValueError as e:
    print(e)
  else:
    print(f"{flavor} chai served successfully!")
    
  finally:
    print("Thank you for visiting our chai shop!")
    
serve_chai("masala")
serve_chai("unknown")