def serve_chai():
  chai_type = "Masala" # local scope
  print(f"Inside function : {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
  chia_order = "lemon" #Enclosing scope
  def print_order():
    chai_order = "ginger"
    print("Inner:", chai_order)
  print_order()
  print("Outer:", chai_order)

chai_order = "Tulasi" # global
chai_counter()
print("Global:", chai_order)


def dummy():
  i = 0
  print(i)
  i += 1

def foo():
    x = 3
    x = x + 1
    print(x)