from .transaction import transaction


@transaction
async def add_user(message, db):
    """ Добавляем пользователя в базу данных """
    columns = {
        'telegram_id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'is_bot': message.from_user.is_bot,
        'is_premium': message.from_user.is_premium,
        'date_from_user': message.date,
    }

    col = ', '.join(list(columns.keys()))
    val = ', '.join(['?'] * len(columns))

    await db.execute(f"INSERT INTO users ({col}) VALUES ({val})", tuple(columns.values()))
    await db.commit()


@transaction
async def save_message(message, db):
    """ Сохраняем текст сообщения пользователя """
    columns = {
        'telegram_id': message.from_user.id,
        'message_id': message.message_id,
        'text': message.text,
        'language_code': message.from_user.language_code,
        'date_from_user': message.date,
    }

    col = ', '.join(list(columns.keys()))
    val = ', '.join(['?'] * len(columns))

    await db.execute(f"INSERT INTO messages ({col}) VALUES ({val})", tuple(columns.values()))
    await db.commit()


@transaction
async def create_event(message, db):
    """ Добавляем event в базу данных """
    columns = {
        'telegram_id': message.from_user.id,
        'event_name': message.from_user.username,  # Необходимо изменить
        'event_date': message.from_user.first_name,  # Необходимо изменить
        'event_description': message.from_user.last_name,  # Необходимо изменить
        'date_from_user': message.date,
    }

    col = ', '.join(list(columns.keys()))
    val = ', '.join(['?'] * len(columns))

    await db.execute(f"INSERT INTO events ({col}) VALUES ({val})", tuple(columns.values()))
    await db.commit()
