import time
import asyncio


async def make_coffee():
    print("Making coffee....")
    await asyncio.sleep(3)
    print("Coffee Ready.")


async def toast_bread():
    print("Toasting Bread...")
    await asyncio.sleep(2)
    print("Toast Ready.")


async def main():
    print("Making Breakfast...")
    s_time = time.time()
    batch = asyncio.gather(make_coffee(), toast_bread())
    coffee, toast = await batch
    e_time = time.time()
    print(f"Breakfast ready in {e_time-s_time:.2f}...")


if __name__ == "__main__":
    print("hello...")
    asyncio.run(main())


"""
Code without Asyncio
"""

# import time


# def make_coffee():
#     print("Making coffee....")
#     time.sleep(3)
#     print("Coffee Ready.")


# def toast_bread():
#     print("Toasting Bread...")
#     time.sleep(2)
#     print("Toast Ready.")


# def main():
#     print("Making Breakfast...")
#     s_time = time.time()
#     make_coffee()
#     toast_bread()
#     e_time = time.time()
#     print(f"Breakfast ready in {e_time-s_time}...")


# if True or __name__ == "main":
#     print("hello...")
#     main()