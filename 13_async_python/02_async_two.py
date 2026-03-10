import asyncio
import time

async def print_names(name):
    print(f"👾 Hello Welcome {name}")
    # await asyncio.sleep(2)
    time.sleep(2)
    print(f"🙌 Goodbye {name}")
    
    
async def main():
    await asyncio.gather(
        print_names("🪱 Alice"),
        print_names("🧑‍💻 Bob"),
        print_names("😊 Charlie")
    )
    
asyncio.run(main())