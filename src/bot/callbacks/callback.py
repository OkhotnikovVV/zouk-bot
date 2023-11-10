from typing import List, Any, Optional
from aiogram.filters.callback_data import CallbackData

# cb = CallbackData()


class EventUsersCallback(CallbackData, prefix="Event users"):
    """ Передаём telegram_id через Callback. """
    foo: str
    telegram_id: int


class InviteUser(CallbackData, prefix="Invite user"):
    """ Передаём telegram_id через Callback. """
    from_user: int
    to_user: int


class Agreement(CallbackData, prefix="Agreement"):
    """ Если True, значит второй участник принял приглашение. """
    exist: bool
