#example of an asynchrous iterator with async loop
import asyncio
import time

#defin an asynchrois itertor
class AsyncItertor():
    #constructor, define some state
    def __init__(self):
        self.counter = 0
    
    #creat an instance of some state
    def __aiter__(self):
        return self
    
    #return the next awaitable
    async def __anext__(self):
        #check for no furture item
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the counter
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        #return the counter value
        return self.counter
    
#main coroutine
async def main():
    #loop over async iterator with async for loop
    async for item in AsyncItertor():
        print(f'{time.ctime()} {item}')

#excute the asyncio program
asyncio.run(main())

# solution
# Wed Jul 19 13:52:45 2023 1
# Wed Jul 19 13:52:46 2023 2
# Wed Jul 19 13:52:47 2023 3
# Wed Jul 19 13:52:48 2023 4
# Wed Jul 19 13:52:49 2023 5
# Wed Jul 19 13:52:50 2023 6
# Wed Jul 19 13:52:51 2023 7
# Wed Jul 19 13:52:52 2023 8
# Wed Jul 19 13:52:53 2023 9
# Wed Jul 19 13:52:54 2023 10