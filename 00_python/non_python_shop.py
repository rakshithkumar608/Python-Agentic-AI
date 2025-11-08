class chai: #this is a class to make chai
  def __init__(self, sweetness_level, milk_level):# initializing the class 
    self.sweetness_level = sweetness_level
    self.milk_level = milk_level

  def sip(self): # method to sip chai
    print(f"Sipping the chai with sweetness level {self.sweetness_level}")
     

  def add_sugar(self, amount): # method to add sugar
    self.sweetness_level += amount
    print(f"Adding {amount} sugar to the chai; new sweetness level is {self.sweetness_level}")

# create an instance of chai
my_chai = chai(sweetness_level=3, milk_level=2)

my_chai.add_sugar(amount=2)