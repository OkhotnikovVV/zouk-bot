from datetime import datetime

from sqlalchemy import BigInteger, Boolean, func
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
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    username: Mapped[str] = mapped_column(String(32))
    language_code: Mapped[str] = mapped_column(String(10))
    is_premium_tg: Mapped[bool | None] = mapped_column(Boolean, default=None)
    photo_id: Mapped[str | None] = mapped_column(String(100), default=None)
    role: Mapped[str | None] = mapped_column(String(10), default=None)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    def __str__(self):
        return f"<User:{self.tg_id}>"


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    # Позже добавить relationship


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    # Позже добавить relationship


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
