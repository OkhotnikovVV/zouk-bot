from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove


main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='sdgfsdgsfgs', callback_data='sfghf')]
])

rmk = ReplyKeyboardRemove()

