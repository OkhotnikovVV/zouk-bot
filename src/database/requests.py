from typing import Coroutine, Any, Union

from aiogram import types
from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import update

from src.database.models import async_session, UserGroup, EventUserJoin
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


async def get_user(tg_id: int) -> Union[int, None]:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user.id


async def join_to_group(message: types.Message):
    async with async_session() as session:
        tg_id = message.from_user.id
        group = 'manager'
        user = await get_user(tg_id)
        user_groups = await session.scalar(select(UserGroup).where((UserGroup.user == tg_id) & (UserGroup.group == group)))  # Обратить внимание
        if not user_groups:
            session.add(UserGroup(user=user,
                                  group=group,
                                  ))
            await session.commit()


async def get_group(name: str) -> Union[int, None]:
    async with async_session() as session:
        group = await session.scalar(select(Group).where(Group.name == name))
        return group


async def is_user_in_group(user, group_name='manager') -> Union[bool, None]:
    async with async_session() as session:
        group = await get_group(group_name)
        user_in_group = await session.scalar(select(UserGroup).where((UserGroup.user == user) & (UserGroup.group == group)))
        return user_in_group


async def get_event(name: str) -> Union[int, None]:
    async with async_session() as session:
        event = await session.scalar(select(Event).where(Event.name == name))
        if event:
            return event.id


async def create_event(message: types.Message, name: str='Вечеринка'):
    async with async_session() as session:
        event = await get_event(name)
        tg_id = message.from_user.id
        user = await get_user(tg_id)
        if not event and await is_user_in_group(user):
            session.add(Event(name=name,
                              user=user,
                              ))
            await session.commit()


async def is_user_at_event(user: int, event: int) -> Union[bool, None]:
    async with async_session() as session:
        user_at_event = await session.scalar(select(EventUserJoin).where((EventUserJoin.event == event) & (EventUserJoin.user == user)))
        return user_at_event


async def join_event(message: types.Message, name: str='Вечеринка'):
    async with async_session() as session:
        event = await get_event(name)
        tg_id = message.from_user.id
        user = await get_user(tg_id)
        if not await is_user_at_event(user, event):
            session.add(EventUserJoin(event=event,
                                      user=user,
                                      ))
            await session.commit()
