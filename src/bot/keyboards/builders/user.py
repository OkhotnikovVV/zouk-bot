from src import db
from aiogram import types
# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder
from src.bot.callbacks.callback import EventUsersCallback


def form_btn(text: str | list) -> types.ReplyKeyboardMarkup:
    if isinstance(text, str):
        text = [text]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def find_kb(users) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    print(users)
    [builder.row(types.InlineKeyboardButton(text=' '.join(filter(None, [user[1], user[2]])), callback_data=EventUsersCallback(telegram_id=user[0], name=user[1], telegram_link=user[2], photo_id=user[3]).pack())) for user in users]
    return builder.as_markup()


def show_event_user(callback_data) -> types.InlineKeyboardMarkup:
    print(callback_data)
    builder = InlineKeyboardBuilder()
    builder.button('')
    # [builder.row(types.InlineKeyboardButton(text=' '.join(filter(None, [user[1], user[2]])), callback_data=EventUsersCallback(action="change", value=user[0]).pack())) for user in users]
    return builder.as_markup()

