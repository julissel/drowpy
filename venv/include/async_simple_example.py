import asyncio


# 1
# @asyncio.coroutine / yield from

@asyncio.coroutine
def print_hi():
    while True:
        print("Hi!")
        yield from asyncio.sleep(1.0)

loop = asyncio.get_event_loop()
loop.run_until_complete(print_hi())
loop.close()


# 2
# async / await

async def say_hello():
    while True:
        print("Hello!")
        await asyncio.sleep(1.0)

loop1 = asyncio.get_event_loop()
loop1.run_until_complete(say_hello())
loop1.close()
