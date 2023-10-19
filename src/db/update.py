from .transaction import transaction
import datetime

@transaction
async def edit_user(message, db):
    """ Редактируем данные пользователя """
    columns = {
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'photo_id': message.photo[-1].file_id,
        'is_bot': message.from_user.is_bot,
        'is_premium': message.from_user.is_premium,
        'date_from_user': message.date,
        'updated_at': datetime.datetime.now(),
    }

    set_values = zip(columns.keys(), ['?'] * len(columns))
    s = ', '.join([i[0] + ' = ' + i[1] for i in set_values])

    await db.execute(f"UPDATE users SET {s} WHERE telegram_id = {message.from_user.id}", tuple(columns.values()))
    await db.commit()
