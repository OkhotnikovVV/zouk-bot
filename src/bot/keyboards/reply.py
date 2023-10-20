from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поиск"),
            KeyboardButton(text="Статистика")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True,
)

rmk = ReplyKeyboardRemove()

