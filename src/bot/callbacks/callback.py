from typing import List, Any, Optional
from aiogram.filters.callback_data import CallbackData

# cb = CallbackData()


class EventUsersCallback(CallbackData, prefix="Event users"):
    """ Передаём telegram_id через Callback """
    foo: str
    telegram_id: int
    # name: str = ''
    # telegram_link: str = ''
    # photo_id: str = ''


