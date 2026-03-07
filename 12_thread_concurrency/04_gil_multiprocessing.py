from  multiprocessing import Process
import time

def bike_names():
    print(f"Bike is running....")
    
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Bike has finished....")
    
    
if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=bike_names, name="Yamaha")
    p2 = Process(target=bike_names, name="Honda")


    p1.start(   )
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print(f"The total time taken is {end - start: .2f} seconds")