#example of getting the currrent task from the main corotine
import asyncio
import time

#define a main corotine 
async def task_coroutine(value):
    #report a message
    print (f'{time.ctime()}task{value} is running')
    #block for moment
    await asyncio.sleep(0.1)

#definr a main corotine
async def main():
    #report a message
    print (f'{time.ctime()} main coroutine started')
    #start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    #allow some of the tasks time to starts
    await asyncio.sleep(1)
    #get all task
    tasks = asyncio.all_tasks()
    #report all task
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()},{task.get_coro()}')
#wait for all task to complete
    for task in started_tasks:
        await task
    #start the asyncio prograne 

asyncio.run(main())