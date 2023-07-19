#examole of runing a coroutine
import asyncio
import time


#define a coroutine
async def main():
    #report a message
    print(f'{time.ctime()} main coroutine started') 
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(f'{time.ctime()}{task}')
    
   
# start the coroutine programs
asyncio.run(main())