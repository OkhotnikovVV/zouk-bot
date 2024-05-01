from typing import Coroutine, Any

from aiogram import types
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import update

from src.database.models import async_session
from src.database.models import Event
from src.database.models import Group
from src.database.models import User


async def create_user(message: types.Message) -> None:
    async with async_session() as session:
        tg_id = message.from_user.id
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            session.add(User(tg_id=tg_id,
                             first_name=first_name,
                             last_name=last_name,
                             ))
            await session.commit()


async def get_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user
