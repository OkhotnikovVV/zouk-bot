import asyncio
from aiogram import F
from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from src import db
from src.bot.callbacks.callback import EventUsersCallback
from src.bot.keyboards import organizator
from src.bot.keyboards.builders.user import show_user

router = Router()


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


# @router.callback_query()
# async def callback_main_keyboard(callback_query: types.CallbackQuery, user) -> None:
#     print(user)
#     await callback_query.answer('Callback')


@router.callback_query(EventUsersCallback.filter())
async def callbacks_num_change_fab(
        callback: types.CallbackQuery,
        callback_data: EventUsersCallback
):

    user = callback_data.telegram_id
    print(user, 'cd')
    await callback.message.edit_reply_markup(reply_markup=show_user(user))

