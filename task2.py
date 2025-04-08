import asyncio
import time
import random

async def update_weather():

        random_weather = random.SystemRandom().choice(["No cloud", "Drizzle(мелкий дождь)",
                                                "Foggy",
                                                "Breeze",
                                                "Chilly(прохладно)",
                                                "Muggy(тепло и влажно)"])
        await asyncio.sleep(3)
        print("weather:",random_weather)

async def player_actions():

    while True:

     task = asyncio.create_task(update_weather())

     random_action = random.SystemRandom().choice(["I’d better find a trader, I’ve got so much loot to sell",
                                                  "He’s camping the chest so we don’t steal it",
                                                  "Good Game",
                                                  "This gun is a real cheese-machine! Using it is just unfair",
                                                  "Continue", "Game over"])
     if random_action != "Game over":
        await asyncio.sleep(1)
        print(random_action)
        await task
     else:
         task.cancel()
         break

loop = asyncio.new_event_loop()
loop.run_until_complete(player_actions())
loop.close()
