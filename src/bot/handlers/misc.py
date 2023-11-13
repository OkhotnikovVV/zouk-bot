from aiogram import types
from aiogram import Router
from aiogram.filters import Command

from src import db

router = Router()


@router.message(Command('create_event'))#commands=['test'])
async def command_test(message: types.Message):
    print('Создание ивента')
    p = await db.insert.create_event(message)
    g = await db.select.get_event()
    await message.answer(str(g))
    # await message.answer(message.message_id)





