import asyncio
from aiogram import F
from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from database.requests import create_user, join_to_group, create_event
from src import db
from src.bot.keyboards.reply import main_kb
from src.bot.keyboards.builders.user import find_kb


router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message) -> None:
    """Создаёт нового пользователя при нажатии кнопки "Start"."""
    await message.answer("Welcome!")
    await create_user(message)


@router.message(Command("help"))
async def command_help(message: types.Message) -> None:
    await message.answer("It is help!")


@router.message(Command("join_to_group"))
async def command_join_to_group(message: types.Message) -> None:
    await message.answer("Присоединиться к группе организаторов")
    await join_to_group(message)


@router.message(Command('create_event'))
async def command_create_event(message: types.Message) -> None:
    # user = str(message.from_user.id)
    await create_event(message)
    # await message.answer(str(profile))
    # print(*p)

    # await message.answer('Hello', reply_markup=main_kb)
    # await message.answer(str(p))


@router.message(Command('meow'))
async def command_meow(message: types.Message) -> None:
    """ Поиск участников по базе. Только тех, кто зарегистрирован на данный ивент. """
    await message.delete()
    users = await db.select.get_users()
    await message.answer_photo(photo='AgACAgIAAxkBAAILAWU4BQ4KDDFTIHEB9bY3MjHuWMt5AAJX1jEbY2bBSfT20KWwgEUNAQADAgADeAADMAQ', reply_markup=find_kb(users))

