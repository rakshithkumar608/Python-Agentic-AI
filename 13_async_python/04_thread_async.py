import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
    print(f"Checking items in store...")
    time.sleep(3) # Blocking operation
    return f"{item} is in stock: 42"

async def main():
    asyncio_loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await asyncio_loop.run_in_executor(pool, check_stock, "laptop")
    
    print(result)
    
asyncio.run(main())
    