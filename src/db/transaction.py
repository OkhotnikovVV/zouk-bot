import aiosqlite


# Реализация декоратора для безопасного соединения с базой данных
def transaction(function):
    async def wrapper(*args, **kwargs):
        async with aiosqlite.connect('../db/data/my_database.db') as db:
            return await function(*args, db=db, **kwargs)
    return wrapper
