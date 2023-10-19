from .transaction import transaction


@transaction
async def create_database(db):
    await db.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                        telegram_id BIGINT UNSIGNED PRIMARY KEY NOT NULL,
                        username VARCHAR(32),
                        first_name VARCHAR(64),
                        last_name VARCHAR(64),
                        photo_id VARCHAR(100),
                        is_bot BOOL DEFAULT False,
                        role BOOL,
                        is_premium BOOL DEFAULT False,
                        date_from_user DATETIME,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
                        )
                        ''')
    await db.execute('''
                        CREATE TABLE IF NOT EXISTS messages (
                        telegram_id BIGINT NOT NULL,
                        message_id MEDIUMINT NOT NULL,
                        text TEXT,
                        language_code VARCHAR(8),
                        date_from_user DATETIME,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        PRIMARY KEY (telegram_id, message_id),
                        FOREIGN KEY (telegram_id) REFERENCES users (telegram_id) ON DELETE CASCADE ON UPDATE NO ACTION
                        )
                        ''')
    await db.execute('''
                        CREATE TABLE IF NOT EXISTS events (
                        event_id INTEGER PRIMARY KEY,
                        telegram_id BIGINT NOT NULL,
                        event_name VARCHAR(64) DEFAULT `Party`,
                        event_date DATETIME,
                        event_description TEXT,
                        event_completed BOOL DEFAULT FALSE,
                        event_is_now BOOL DEFAULT FALSE,
                        date_from_user DATETIME,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        FOREIGN KEY (telegram_id) REFERENCES users (telegram_id) ON DELETE CASCADE ON UPDATE NO ACTION
                        )
                        ''')
    await db.commit()
    print('Database создана')