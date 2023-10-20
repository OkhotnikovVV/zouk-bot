import asyncio
from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from src import db
from src.bot.keyboards import organizator


router = Router()


@router.message(Command('test'))
async def command_test(message: types.Message):
    print('Вывод всех пользователей')
    p = await asyncio.gather(db.select.get_users())
    # await message.answer(str(message.message_id))
    await message.answer(str(*p), reply_markup=organizator.event_kb)
    # await message.answer(message.message_id)


@router.message(Command('create_event'))#commands=['test'])
async def command_test(message: types.Message):
    print('Создание ивента')
    p = await asyncio.gather(db.insert.create_event(message))
    g = await asyncio.gather(db.select.get_event())
    await message.answer(str(g))
    # await message.answer(message.message_id)

# @other_router.message()
# async def save_message(message: types.Message):
#     print('Перехват сообщений')
#     await database.save_message(message)
