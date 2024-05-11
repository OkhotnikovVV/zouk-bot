from aiogram import F
from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from database.requests import create_user, join_to_group, create_event, join_event, get_event_participants, show_photo
from src.bot.keyboards.reply import main_kb
from src.bot.keyboards.builders.user import show_user_menu

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
    await create_event(message)


@router.message(Command('join_event'))
async def command_join_event(message: types.Message) -> None:
    await join_event(message)


@router.message(Command('meow'))
async def command_meow(message: types.Message) -> None:
    """ Поиск участников по базе. Только тех, кто зарегистрирован на данный ивент. """
    participants = await get_event_participants(message)


@router.message(Command('show_photo'))
async def command_show_photo(message: types.Message) -> None:
    photo = await show_photo(message)
    await message.answer_photo(photo=photo)


@router.message(Command('go'))
async def command_go(message: types.Message) -> None:
    photo = await show_photo(message)
    await message.answer_photo(photo=photo, reply_markup=show_user_menu())
