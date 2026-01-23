def serve_chai():
  yield "Cup 1: Masala Chai"
  yield "Cup 2: Ginger Chai"
  yield "Cup 3: Elaichi Chai"
  
  
stall = serve_chai()

for cup in stall:
  print(cup)
  
# getting one by one values
def get_chai_list():
  return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_get():
  yield "Cup 1"
  yield "Cup 2"
  yield "Cup 3"
  
chai = get_chai_get()
print(next(chai))
  