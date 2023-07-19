#example of getting the currrent task from the main corotine
import asyncio
import time

#define a main corotine 
async def task_coro(value):
    #report a message
    print (f'{time.ctime()}task{value} executing')
    #block for moment
    await asyncio.sleep(0.1)

#definr a main corotine
async def main():
    #report a message
    print (f'{time.ctime()} main started')
    #create corotine 
    coros = [task_coro(i) for i in range (100000)]
    #run the tasks
    await asyncio.gather(*coros)
    #report a message
    print(f'{time.ctime()} main done')

 

asyncio.run(main())