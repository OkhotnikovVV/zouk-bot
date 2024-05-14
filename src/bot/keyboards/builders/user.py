from src import db
from aiogram import types, Bot
# from aiogram.types import KeyboardButton
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder

from src.bot.callbacks.callback import Agreement
from src.bot.callbacks.callback import EventUsersCallback
from src.bot.callbacks.callback import InviteUser


def form_btn(text: str | list) -> types.ReplyKeyboardMarkup:
    if isinstance(text, str):
        text = [text]

    builder = ReplyKeyboardBuilder()
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def find_kb(users) -> types.InlineKeyboardMarkup:
    """ Клавиатура найденных участников ивента.
    В тексте каждой кнопки - first_name, last_name, username.
    После нажатия выводится анкета участника.
    """
    builder = InlineKeyboardBuilder()
    print(users)
    [
        builder.row(types.InlineKeyboardButton(
            text=' '.join(filter(None, [user['name'], user['username']])),
            callback_data=EventUsersCallback(
                foo='id',
                telegram_id=user['telegram_id']
            ).pack())
        ) for user in users
    ]
    return builder.as_markup()


def kb_show_participants():
    buttons = [
        [
            types.InlineKeyboardButton(text="Пригласить", callback_data="invite"),
            types.InlineKeyboardButton(text="Пропустить", callback_data="skip")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def kb_create_event():
    buttons = [
        [
            types.InlineKeyboardButton(text="Создать", callback_data="create_event"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def invite(from_user, to_user) -> types.InlineKeyboardMarkup:
    """ Кнопка приглашения участника. """
    builder = InlineKeyboardBuilder()
    builder.button(text='Пригласить', callback_data=InviteUser(
        from_user=from_user,
        to_user=to_user
        ).pack())
    return builder.as_markup()


def confirm_invitation(back_to_user) -> types.InlineKeyboardMarkup:
    """ Кнопка согласия на приглашение. """
    builder = InlineKeyboardBuilder()
    builder.button(text='Подтвердить', callback_data=Agreement(
        exist=True,
        back_to_user=back_to_user
        ).pack())
    return builder.as_markup()
