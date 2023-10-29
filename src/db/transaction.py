import aiosqlite

from src.bot.settings import conf


# Implementing a decorator for a secure database connection
def transaction(function):
    async def wrapper(*args, **kwargs):
        async with aiosqlite.connect(conf.db.path) as db:
            return await function(*args, db=db, **kwargs)
    return wrapper
