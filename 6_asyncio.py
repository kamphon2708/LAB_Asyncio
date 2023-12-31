#example of watting for all task to complete
from random import random
import asyncio
import time

#coroutine to execute in a new task
async def task_coro(arg):
    #generate a random value between 0 and 1
    value = 1 + random()
    #report message
    print(f'{time.ctime()} > task got {value}')
    #block for a moment
    await asyncio.sleep(value)
    #report the value
    print(f'{time.ctime()} >task done ')

#main coroutine
async def main():
    #create many tasks
    task = task_coro(1)
    #execute and wait for the task without a time out 
    try:
        await asyncio.wait_for(task,timeout=0.2)
    except asyncio.TimeoutError:
        print(f'{time.ctime()} Gave up waiting, task canceled')

#sstart the asyncio program
asyncio.run(main())