import asyncio
import passw 
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard
import time
import random


bot = Bot(passw.token)


@bot.on.message(text=["Привет", 'нет'])
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))
    await asyncio.sleep(20)
    xp = str(random.randint(1, 100))
    await message.answer('Я все! ' + xp)



@bot.on.message(text="скажи")
async def hi_handler(message: Message):
    await message.answer('Да!')

