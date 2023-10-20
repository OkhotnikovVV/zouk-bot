from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


event_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Смайлfdsgdfgsdfgsdddddddddddddddddddddddddddddddddddddddddddddfgsdfgsdfики'),
            KeyboardButton(text='Ссылки'),
        ],
        [
            KeyboardButton(text='Смайлики2'),
            KeyboardButton(text='Ссылки2'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective=True
)

