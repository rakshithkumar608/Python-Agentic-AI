import threading
import time

def car_names():
    print(f"Car is running....")
    time.sleep(2)
    print(f"Car has finished....")
    
def bike_names():
    print(f"Bike is running....")
    time.sleep(3)
    print(f"Bike has finished....")
    
    
start = time.time()

t1 = threading.Thread(target=car_names, name="Car")
t2 = threading.Thread(target=bike_names, name="Bike")

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"The total time taken is {end - start: .2f} seconds")