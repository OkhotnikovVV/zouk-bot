from src import db
from aiogram import types
# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder


def form_btn(text: str | list) -> types.ReplyKeyboardMarkup:
    if isinstance(text, str):
        text = [text]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def find_kb(users) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [builder.row(types.InlineKeyboardButton(text=' '.join(filter(None, [user[1], user[2]])), callback_data='sdfg')) for user in users]
    return builder.as_markup()


