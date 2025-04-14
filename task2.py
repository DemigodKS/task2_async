var 1
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
    task = asyncio.create_task(update_weather())

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

    await task

asyncio.run(player_actions())

var 2

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

   task = asyncio.create_task(update_weather())

   while True:
    random_action = random.SystemRandom().choice(["I’d better find a trader, I’ve got so much loot to sell",
                                                  "He’s camping the chest so we don’t steal it",
                                                  "Good Game",
                                                  "This gun is a real cheese-machine! Using it is just unfair",

                                                  "Continue", "Game over"])

    await asyncio.sleep(2)
    print(f'Action: {random_action}, {datetime.datetime.now().time()}')
    if random_action == "Game over":
        break

   await task




asyncio.run(player_actions())



