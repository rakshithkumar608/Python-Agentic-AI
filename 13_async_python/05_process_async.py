import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt_data(data):
    return f"🔒 Encrypted data: {data[::-1]}"  


async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt_data, "Credit_card_no_1234")
    print(f"{result}")  

if __name__ == "__main__":
    asyncio.run(main())