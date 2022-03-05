import asyncio
from cgitb import text
import asyncpg
from urllib3 import Retry
import passw 
from vkbottle.bot import Bot, Message
from vkbottle import ABCRule, BaseStateGroup, VKAPIError
from vkbottle import Keyboard, KeyboardButtonColor, Text
import time
import random
import keyboard as kb
import class_my as my_rl


bot = Bot(passw.token)


bot.labeler.custom_rules["new_player"] = my_rl.New_player_exam
bot.labeler.custom_rules["registration_player"] = my_rl.New_player_registration
bot.labeler.custom_rules["player_in_city"] = my_rl.player_in_city
bot.labeler.custom_rules["player_in_the_country"] = my_rl.player_in_the_country

@bot.on.message(text="/start", new_player = False)
async def start_handler(message: Message):
    conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
    await conn.execute('INSERT INTO maintable (id_player) VALUES ($1)', str(message.peer_id))
    await conn.close()
    await message.answer('Выберете рассу', keyboard=kb.KEYBOARD_SELECT_RACE)

@bot.on.message(text = ['Человек','Эльф','Демон'], registration_player = True)
async def race_handler(message: Message):
    race_dict = {'Эльф':'elf', 'Демон':'demon', 'Человек':'human','elf': 800, 'demon': 1200, 'human': 1000}
    race = race_dict[message.text]
    hp = race_dict[race]
    conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
    await conn.execute('UPDATE maintable SET race_player = $1, hp_player = $2 WHERE id_player = $3', race, hp ,str(message.peer_id))
    await conn.close()
    await message.answer('Выберети тип воина', keyboard=kb.KEYBOARD_SELECT_ROLE)
    
@bot.on.message(text = ['Танк','Хил','ДД'], registration_player = True)
async def type_handler(message: Message):
    race_dict = {'Танк':[30,40], 'Хил':[40,30], 'ДД':[50,20]}
    attack = race_dict[message.text][0]
    deffence = race_dict[message.text][1]
    conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
    await conn.execute('UPDATE maintable SET attack_player = $1, defferrence_player = $2, status_player = $3 WHERE id_player = $4', attack, deffence , 'in_city',str(message.peer_id))
    await conn.close()
    await message.answer('Вы вышли в просторный город... ', keyboard=kb.KEYBOARD_CITY)

@bot.on.message(text = ['Воевать с монстрами'],  player_in_city = True)
async def type_handler(message: Message):
    conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
    await conn.execute('UPDATE maintable SET status_player = $1 WHERE id_player = $2', 'in_the_country',str(message.peer_id))
    await conn.close()
    await message.answer('Чем займемся путник?.. ', keyboard=kb.KEYBOARD_IN_THE_COUNTRY)


@bot.on.message(text = ['В город'],  player_in_the_country = True)
async def type_handler(message: Message):
    conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
    await conn.execute('UPDATE maintable SET status_player = $1 WHERE id_player = $2', 'in_city',str(message.peer_id))
    await conn.close()
    await message.answer('Чем займемся путник?.. ', keyboard=kb.KEYBOARD_CITY)
bot.run_forever()