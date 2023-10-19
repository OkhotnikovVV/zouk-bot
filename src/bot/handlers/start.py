import asyncio
from aiogram import types
from aiogram import Router

from src import db
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message):
    print('Start')
    p = await asyncio.gather(db.select.user_exists(message.from_user.id))
    if p[0]:
        print(*p, 'Есть такой')
    else:
        print('Регистрация')
        await db.insert.add_user(message)
