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


def find_kb() -> types.InlineKeyboardMarkup:
    text = ['Иван'] * 5
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton("Кнопка 1", callback_data="button1"),
                 InlineKeyboardButton("Кнопка 2", callback_data="button2"))
    keyboard.add(InlineKeyboardButton("Кнопка 3", callback_data="button3"),
                 InlineKeyboardButton("Кнопка 4", callback_data="button4"))


    return keyboard
