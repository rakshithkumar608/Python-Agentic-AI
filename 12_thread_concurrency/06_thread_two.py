import threading
import time


def f_names(type_, wait_time):
    print(f"{type_} is running....")
    time.sleep(wait_time)
    print(f"{type_} has finished....")
    
f1 = threading.Thread(target=f_names, args=["Car", 2])
f2 = threading.Thread(target=f_names, args=["Bike", 3])

f1.start()
f2.start()

f1.join()
f2.join()

