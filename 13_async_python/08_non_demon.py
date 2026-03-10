import threading
import time

def moniter_system():
    while True:
        print("Monitering the system health 🕰️")
        time.sleep(2)

t = threading.Thread(target=moniter_system)
t.start()
print("Main thread is doing other work... 🧑‍💻")