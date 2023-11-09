from typing import Dict
import json
from aiogram.fsm.storage.redis import RedisStorage

from src.bot.utils.parser import parser
from src.cache import cache
from src.db.transaction import transaction


@transaction
async def refer_to_db(db, user):
    db.row_factory = lambda column, row: dict(zip([col[0] for col in column.description], row))
    cursor = await db.cursor()
    await cursor.execute(f"""
        SELECT
            telegram_id,
            username,
            first_name,
            last_name,
            photo_id
        FROM users
        WHERE telegram_id = {user}
        """)
    return await cursor.fetchone()


async def get_user(user: int, storage: cache = cache) -> Dict:
    """ Возвращаем данные анкеты user. """
    data = await storage.client.get(name='telegram_id:' + str(user))
    if data:
        profile = json.loads(data)
    else:
        row = await refer_to_db(user)
        telegram_id = row['telegram_id']
        profile = await parser(row)
        await storage.client.set(name='telegram_id:' + str(telegram_id), value=json.dumps(profile))
    return profile


@transaction
async def get_users(db):
    """ Возвращаем все записи из таблицы users. """
    db.row_factory = lambda column, row: dict(zip([col[0] for col in column.description], row))
    cursor = await db.cursor()
    await cursor.execute("""SELECT
                                    telegram_id,
                                    username,
                                    first_name,
                                    last_name,
                                    photo_id
                                    FROM users""")
    rows = await cursor.fetchall()
    users = []
    for row in rows:
        telegram_id = row['telegram_id']
        name = ' '.join(filter(None, (row['first_name'], row['last_name'])))
        username = ' '.join(filter(None, ('@' + row['username'],)))
        photo = row['photo_id']
        users.append({'telegram_id': telegram_id, 'name': name, 'username': username, 'photo': photo})
    return users


@transaction
async def user_exists(telegram_id, db):
    """ Возвращаем True, если пользователь есть в базе данных. """
    cursor = await db.execute(f"SELECT * FROM users WHERE telegram_id = {telegram_id}")
    rows = await cursor.fetchall()
    return bool(rows)


@transaction
async def get_event(db):
    """ Возвращаем все записи из таблицы event. """
    db.row_factory = lambda column, row: dict(zip([col[0] for col in column.description], row))
    cursor = await db.cursor()
    await cursor.execute("SELECT * FROM events")
    rows = await cursor.fetchall()
    return rows

