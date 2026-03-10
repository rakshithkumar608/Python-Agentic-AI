
import threading
import time

def car_names():
    print(f"{threading.current_thread().name} is running....")
    
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} has finished....")
    
thread1 = threading.Thread(target=car_names, name="Volvo")
thread2 = threading.Thread(target=car_names, name="Mercedes")\
    
start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"The total time taken is {end - start: .2f} seconds")