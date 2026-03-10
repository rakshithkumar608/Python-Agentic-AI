import threading

chai_stock = 0

def check_stock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1
        
threads = [threading.Thread(target=check_stock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print(f"Stock after restocking: {chai_stock}")