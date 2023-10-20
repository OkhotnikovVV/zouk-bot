from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def form_btn(text: str | list) -> types.ReplyKeyboardMarkup:
    if isinstance(text, str):
        text = [text]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def find_kb() -> types.ReplyKeyboardMarkup:
    text = 'abcdef'
    builder = ReplyKeyboardBuilder()
    [builder.button(text=txt) for txt in text]
    builder.row(types.KeyboardButton(text="Назад"))
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
