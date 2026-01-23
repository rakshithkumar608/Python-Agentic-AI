def chai_customer():
  print("Welcome ! What chai would you like ?")
  order = yield
  while True:
    print(f"Preparing: {order}")
    order = yield # if not there the loop will continue infinite times
    
stall = chai_customer()
next(stall) # starting point of the generators

stall.send("Masala chai")
stall.send("Lemon Chai")