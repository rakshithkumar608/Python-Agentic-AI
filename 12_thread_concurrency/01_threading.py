import threading
import time

# creating function
def car_names(name):
    for name in range(1,4):
        print(f"Car names #{name}")
        time.sleep(1)


def car_colors(color):
    for color in range(1,4):
        print(f"Car colors #{color}")
        time.sleep(2)

# creating thread
t1 = threading.Thread(target=car_names, args=("name",))
t2 = threading.Thread(target=car_colors, args=("color",))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"All cars names and colors are given")
        