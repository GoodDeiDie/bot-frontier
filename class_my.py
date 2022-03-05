from vkbottle import ABCRule, BaseStateGroup, VKAPIError
import asyncpg
from vkbottle.bot import Bot, Message
import passw 


class New_player_exam(ABCRule[Message]):
    def __init__(self, lt: bool):
        self.lt = lt

    async def connect_id(self, event: Message):
        conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
        values = await conn.fetchrow(f'SELECT status_player FROM maintable WHERE id_player=$1', str(event.peer_id))
        await conn.close()
        if not values:
            return True
        else:
            return False
        
    async def check(self, event: Message) -> bool:
        return await self.connect_id(event)

class New_player_registration(ABCRule[Message]):
    def __init__(self, lt: bool):
        self.registration = 'registration'

    async def connect_id(self, event: Message):
        conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
        values = await conn.fetchrow(f'SELECT status_player FROM maintable WHERE id_player=$1', str(event.peer_id))
        await conn.close()
        return(values['status_player'])
        
    async def check(self, event: Message) -> bool:
        return await self.connect_id(event) == self.registration

class player_in_city(ABCRule[Message]):
    def __init__(self, lt: bool):
        self.registration = 'in_city'

    async def connect_id(self, event: Message):
        conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
        values = await conn.fetchrow(f'SELECT status_player FROM maintable WHERE id_player=$1', str(event.peer_id))
        await conn.close()
        return(values['status_player'])
        
    async def check(self, event: Message) -> bool:
        return await self.connect_id(event) == self.registration

class player_in_the_country(ABCRule[Message]):
    def __init__(self, lt: bool):
        self.registration = 'in_the_country'

    async def connect_id(self, event: Message):
        conn = await asyncpg.connect(user=passw.user_bd, password=passw.pas_bd, database= passw.database, host= passw.host_bd)
        values = await conn.fetchrow(f'SELECT status_player FROM maintable WHERE id_player=$1', str(event.peer_id))
        await conn.close()
        return(values['status_player'])
        
    async def check(self, event: Message) -> bool:
        return await self.connect_id(event) == self.registration