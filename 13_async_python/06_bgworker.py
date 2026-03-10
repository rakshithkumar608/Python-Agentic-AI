import threading
import asyncio
import time

def background_task():
    while True:
        time.sleep(2)
        print(f"Logging the system health 🕰️")
        
async def fetch_order():
    await asyncio.sleep(5)
    print("Order fetched 🛒")
    
threading.Thread(target=background_task, daemon=True).start()
asyncio.run(fetch_order())