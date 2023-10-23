from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поиск', callback_data='Поиск')]
])

rmk = ReplyKeyboardRemove()

