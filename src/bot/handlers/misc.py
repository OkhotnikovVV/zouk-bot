import asyncio
from aiogram import F
from aiogram import Bot
from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from src import db
from src.bot.callbacks.callback import Agreement
from src.bot.callbacks.callback import EventUsersCallback
from src.bot.callbacks.callback import InviteUser
from src.bot.keyboards import organizator
from src.bot.keyboards.builders.user import show_user, invite, confirm_invitation
from src.bot.keyboards.builders.user import find_kb
from src.db.select import get_user

router = Router()


@router.message(Command('create_event'))#commands=['test'])
async def command_test(message: types.Message):
    print('Создание ивента')
    p = await db.insert.create_event(message)
    g = await db.select.get_event()
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
async def callbacks_show_users_fab(callback: types.CallbackQuery, callback_data: EventUsersCallback):
    """ Ловим Callback с telegram_id, чтобы вывести анкету участника. """
    # Необходимо добавить, кнопку <Назад>
    user = await get_user(callback_data.telegram_id)
    await callback.message.delete()
    await callback.message.answer_photo(
        photo='AgACAgIAAxkBAAILAWU4BQ4KDDFTIHEB9bY3MjHuWMt5AAJX1jEbY2bBSfT20KWwgEUNAQADAgADeAADMAQ',
        caption=f"<b>{user['name']}</b>",
        parse_mode="HTML",
        reply_markup=invite(callback.from_user.id, callback_data.telegram_id)
    )


@router.callback_query(InviteUser.filter())
async def callbacks_show(callback: types.CallbackQuery, callback_data: InviteUser, bot: Bot):
    """ После нажатия выведем кнопку у приглашённого. """

    print('приглашение', callback_data.from_user, callback_data.to_user)
    await bot.send_message(
        chat_id=callback_data.to_user,
        text=f'Вас пригласил {callback_data.from_user}',
        reply_markup=confirm_invitation(callback_data.from_user)
    )


@router.callback_query(Agreement.filter())
async def callbacks_agreement(callback: types.CallbackQuery, callback_data: Agreement, bot: Bot):
    """ После нажатия отправим 'Подтверждено' инициатору приглашения. """

    print('согласие', callback_data.back_to_user)
    await bot.send_message(
        chat_id=callback_data.back_to_user,
        text=f'Подтверждено {callback_data.back_to_user}'
    )
