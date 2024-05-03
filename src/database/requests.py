from typing import Coroutine, Any

from aiogram import types
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import update

from src.database.models import async_session, UserGroup
from src.database.models import Event
from src.database.models import Group
from src.database.models import User


async def create_user(message: types.Message) -> None:
    """Проверяем наличие данных о пользователе. При отсутствии - вносим в базу."""
    async with async_session() as session:
        tg_id = message.from_user.id
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            first_name = message.from_user.first_name
            last_name = message.from_user.last_name
            username = message.from_user.username
            language_code = message.from_user.language_code
            is_premium_tg = message.from_user.is_premium
            session.add(User(tg_id=tg_id,
                             first_name=first_name,
                             last_name=last_name,
                             username=username,
                             language_code=language_code,
                             is_premium_tg=is_premium_tg,
                             ))
            await session.commit()


async def get_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user


async def join_to_group(message: types.Message):
    async with async_session() as session:
        tg_id = message.from_user.id
        group = ['manager']
        user = 1
        user_groups = await session.scalar(select(UserGroup).where((UserGroup.user == tg_id) & (UserGroup.group == group)))
        if not user_groups:
            session.add(UserGroup(user=user,
                                  group=group,
                                  ))
            await session.commit()



async def create_event(tg_id):
    async with async_session() as session:
        # name
        # country
        # city
        # school
        # time_start
        time_end: Mapped[datetime] = mapped_column(insert_default=func.now() + timedelta(hours=3))
        event = await session.scalar(select(Event).where(Event.tg_id == tg_id))
