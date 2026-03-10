import asyncio

async def main():
    print("Main function started ✅")
    await asyncio.sleep(2)
    print("Main function ended 🚀")
    
asyncio.run(main())