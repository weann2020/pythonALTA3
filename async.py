import asyncio

async def add(a,b):
    c = a+b
    await asyncio.sleep(5)
    print(f"The sum is: {c}. First job done.")

async def multiply(a,b):
    c = a *b
    await asyncio.sleep(1)
    print(f"The product is: {c}. Second job done.")


async def main():
    task1 = asyncio.create_task(add(3,5))

    task2 = asyncio.create_task(multiply(3, 5))
    
    await asyncio.gather(task1, task2)
    print("All jobs done!")


if __name__ == "__main__":
   asyncio.run(main())


