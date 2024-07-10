from random import random
import asyncio
from time import time,sleep

async def task_coro(arg):
    #Menu
    Menu = ["Rice","Curry","Noodle"]
    #generate a random value between 0 and 1
    value = random() + 1
    #block for a moment 
    await asyncio.sleep(value)
    #report the value
    print(f'>task {Menu[arg]} done with {value:.3f} sec')
async def main():
    #create many task
    tasks = [asyncio.create_task(task_coro(i)) for i in range(3) ]
    #wait for all tasks to complete
    done,pending = await asyncio.wait(tasks,return_when= asyncio.FIRST_COMPLETED)
    #get the first task to complete
    first = done.pop()
    print(first)
#start the syncio program
asyncio.run(main())


