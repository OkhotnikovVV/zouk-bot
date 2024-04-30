from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy import update

from src.database.models import async_session
from src.database.models import Event
from src.database.models import Group
from src.database.models import User

async def create_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()