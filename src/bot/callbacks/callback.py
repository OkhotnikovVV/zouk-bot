from typing import List, Any, Optional
from aiogram.filters.callback_data import CallbackData

# cb = CallbackData()


class EventUsersCallback(CallbackData, prefix="Event users"):
    telegram_id: int
    name: str = ''
    telegram_link: str = ''
    photo_id: str = ''
