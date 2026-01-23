from functools import wraps

def my_decorators(func):
  @wraps(func)
  def wrapper():
    print("Before function runs")
    func()
    print("After function runs")
  return wrapper

@my_decorators # this function which calls decorators
def greet():
  print("Hello from decorators class from chaicode")
    
greet()
print(greet.__name__)