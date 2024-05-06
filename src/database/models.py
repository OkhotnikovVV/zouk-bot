from datetime import datetime, timedelta

from sqlalchemy import BigInteger, Boolean, func, UniqueConstraint, PrimaryKeyConstraint, bindparam
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    first_name: Mapped[str] = mapped_column(String(64), default='')
    last_name: Mapped[str] = mapped_column(String(64), default='')
    username: Mapped[str] = mapped_column(String(32), default='')
    language_code: Mapped[str] = mapped_column(String(10), default='')
    is_premium_tg: Mapped[bool | None] = mapped_column(Boolean, default=None)
    photo_id: Mapped[str | None] = mapped_column(String(100), default=None)
    role: Mapped[str | None] = mapped_column(String(10), default=None)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now(), onupdate=func.now())

    def __str__(self):
        return f"<User:{self.tg_id}>"


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    # Позже добавить relationship


class UserGroup(Base):
    __tablename__ = 'user_groups'

    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    group: Mapped[int] = mapped_column(ForeignKey('groups.id'))

    __table_args__ = (
        PrimaryKeyConstraint('user', 'group'),
    )


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    country: Mapped[str] = mapped_column(String(32), default='')
    city: Mapped[str] = mapped_column(String(32), default='')
    school: Mapped[str] = mapped_column(String(32), default='')
    time_start: Mapped[datetime] = mapped_column(insert_default=func.now())
    time_end: Mapped[datetime] = mapped_column(default=datetime.now() + timedelta(hours=3))
    # Позже добавить relationship

    __table_args__ = (
        UniqueConstraint('name', 'country', 'city', 'school', 'time_start', 'time_end', name='unique_event'),
    )


class EventUserJoin(Base):
    __tablename__ = 'event_user_join'

    event: Mapped[int] = mapped_column(ForeignKey('events.id'))
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))

    __table_args__ = (
        PrimaryKeyConstraint('event', 'user'),
    )


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
