task1
import asyncio
from random import randint
import time
import datetime

start_time = time.time()

async def load_texture():
    random_time = randint(2, 3)
    await asyncio.sleep(random_time)
    return f"Texture loaded, time: {datetime.datetime.now().time()}"


async def load_sound():
    await asyncio.sleep(2)
    return f"Sound loaded, time: {datetime.datetime.now().time()}"

async def load_scripts():
    random_time2 = randint(2, 4)
    await asyncio.sleep(random_time2)

    return f"Scripts loaded, time: {datetime.datetime.now().time()}"

async def load_levels():
    random_time3 = randint(3, 5)
    await asyncio.sleep(random_time3)
    return f"Levels loaded, time: {datetime.datetime.now().time()}"

async def main():
    results = await asyncio.gather(load_texture(), load_sound(), load_scripts(), load_levels())
    for i in results:
        print(i)

asyncio.run(main())
end_time = time.time()
elapsed_time = round(end_time - start_time, 2)
print('All resources loaded in ', elapsed_time, 'seconds')


task2
import asyncio
import time
import random
import datetime


async def update_weather():
    for i in range(5):
        random_weather = random.SystemRandom().choice(["No cloud", "Drizzle(мелкий дождь)",
                                                       "Foggy",
                                                       "Breeze",
                                                       "Chilly(прохладно)",
                                                       "Muggy(тепло и влажно)"])

        print(f'weather: {random_weather}, {datetime.datetime.now().time()}')
        await asyncio.sleep(3)


async def player_actions():

    for i in range(6):
        random_action = random.SystemRandom().choice(["I’d better find a trader, I’ve got so much loot to sell",
                                                      "He’s camping the chest so we don’t steal it",
                                                      "Good Game",
                                                      "This gun is a real cheese-machine! Using it is just unfair",

                                                      "Continue", "Game over"])

        await asyncio.sleep(2)
        print(f'Action: {random_action}, {datetime.datetime.now().time()}')
        # if random_action == "Game over":
        #     break



async def main():
    task = asyncio.create_task(update_weather())
    await player_actions()
    await task


asyncio.run(main())






    
