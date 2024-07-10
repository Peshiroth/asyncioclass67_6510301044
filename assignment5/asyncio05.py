from random import random
import asyncio
from time import time,sleep

async def make_rice():
    value = random() + 1

    print(f'Rice Cooking Use {value} Sec')
    await asyncio.sleep(value)

    print(f'Rice Finish in {value} Sec')

async def make_noodle():
    value = random() + 1

    print(f'Noodle Cooking Use {value} Sec')
    await asyncio.sleep(value)

    print(f'Noodle Finish in {value} Sec')

async def make_curry():
    value = random() + 1
    print(f'Curry Cooking Use {value} Sec')
    await asyncio.sleep(value)

    print(f'Curry Finish in {value} Sec')

async def main():
    makeRice = asyncio.create_task(make_rice(), name= "Rice")
    makeNoodle = asyncio.create_task(make_noodle(), name= "Noodle")
    makeCurry = asyncio.create_task(make_curry(), name= "Curry")

    Menus = [makeRice, makeNoodle, makeCurry]
    #wait for all tasks to complete
    done,pending = await asyncio.wait(Menus,return_when= asyncio.FIRST_COMPLETED)
    #get the first task to complete
    print(f'Task Complete :{len(done)} ')
    first = done.pop()
    print(first)
    
    print(f'Task Uncomplete :{len(pending)} ')
#start the syncio program
asyncio.run(main())


