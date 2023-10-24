from .transaction import transaction


@transaction
async def get_users(db):
    """ Возвращаем все записи из таблицы users """
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
    result = []
    for row in rows:
        id = row['telegram_id']
        name = ' '.join(filter(None, (row['first_name'], row['last_name'])))
        username = ' '.join(filter(None, ('@' + row['username'],)))
        photo = row['photo_id']
        result.append((id, name, username, photo))
    return result


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

