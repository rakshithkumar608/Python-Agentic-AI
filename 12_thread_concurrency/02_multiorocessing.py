from multiprocessing import Process
import time

def car_names(name):
    print(f"car name {name} is running")
    time.sleep(2)
    print(f"car name {name} has finished")


if __name__ == "__main__":
    car_makers = [
        Process(target=car_names, args=(f"Car Maker #{car+1}",))
        for car in range(3)
    ]

    for cars in car_makers:
        cars.start()

    for cars in car_makers:
        cars.join()

    print("All cars have finished")
    