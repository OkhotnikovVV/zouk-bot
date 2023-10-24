import asyncio
from aiogram import F
from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from src import db
from src.bot.keyboards.reply import main_kb
from src.bot.keyboards.builders.user import find_kb


router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message) -> None:
    p = await asyncio.gather(db.select.user_exists(message.from_user.id))
    if p[0]:
        print(*p, 'Есть такой')
    else:
        print('Регистрация')
        await db.insert.add_user(message)


@router.message(Command("help"))
async def command_help(message: types.Message) -> None:
    await message.answer("It is help!")


@router.message(Command('go'))
async def command_inside_event(message: types.Message, db: db = db) -> None:
    pass
    # print(*p)

    # await message.answer('Hello', reply_markup=main_kb)
    # await message.answer(str(p))


@router.message(F.text.lower() == 'поиск')
async def command_inside_event(message: types.Message) -> None:
    users = await db.select.get_users()
    await message.answer_photo(photo='AgACAgIAAxkBAAILAWU4BQ4KDDFTIHEB9bY3MjHuWMt5AAJX1jEbY2bBSfT20KWwgEUNAQADAgADeAADMAQ', reply_markup=find_kb(users))
    # await message.answer(' f' * 30, reply_markup=find_kb(users))
    # p = await asyncio.gather(db.select.get_users())
    # await message.answer(str(*p))
