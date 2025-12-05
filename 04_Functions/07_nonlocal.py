def update_order():
  chai_type = "Elachi"
  def kitchen():
    nonlocal chai_type
    chai_type = "keasr"
  kitchen()
  print("After kitchn update", chai_type)

update_order()