#examole of runing a coroutine
import asyncio

#define a coroutine
async def custo_coro():
    #wait for a tak to be done
    #await another coroutine
    await asyncio.sleep(1)

#main coroutine
async def main():
    # excute my custom coroutine
    await custom_coro()

# start the coroutine programs
asyncio.run(main())