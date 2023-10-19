from .transaction import transaction


@transaction
async def get_users(db):
    """ Возвращаем все записи из таблицы users """
    db.row_factory = lambda column, row: dict(zip([col[0] for col in column.description], row))
    cursor = await db.cursor()
    await cursor.execute("SELECT * FROM users")
    rows = await cursor.fetchall()
    return rows


@transaction
async def user_exists(telegram_id, db):
    """ Возвращаем True, если пользователь есть в базе данных """
    cursor = await db.execute(f"SELECT * FROM users WHERE telegram_id = {telegram_id}")
    rows = await cursor.fetchall()
    return bool(rows)


@transaction
async def get_event(db):
    """ Возвращаем все записи из таблицы event """
    db.row_factory = lambda column, row: dict(zip([col[0] for col in column.description], row))
    cursor = await db.cursor()
    await cursor.execute("SELECT * FROM events")
    rows = await cursor.fetchall()
    return rows

