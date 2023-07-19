#example of an asynchrous context manager via async with
import asyncio
import time

import asyncio

#define an asynchronous context manager
class AsyncContextManager:
    #enter the async context manager
    async def __aenter__(self):
        #report a massage
        print(f'{time.ctime()} >entering the context manager')
        #block for a moment
        await asyncio.sleep(0.5)

    #exit the async context manager
    async def __aexit__(swlf, exc_type, exc, tb):
        #report a massage
        print(f'{time.ctime()} >entering the context manager')
        #block for a moment
        await asyncio.sleep(0.5)



#define a simple coroutine
async def custom_coroutine():
    #creat and use the asynchronous context manager
    async with AsyncContextManager() as manager:
        #report the result
        print(f'{time.ctime()} within the manager')
#start rhe asyncio program
asyncio.run(custom_coroutine())

# solution
# Wed Jul 19 13:47:24 2023 >entering the context manager
# Wed Jul 19 13:47:25 2023 within the manager
# Wed Jul 19 13:47:25 2023 >entering the context manager