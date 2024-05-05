import asyncio
# import logging
from aiogram import Bot

from src.bot.settings import conf
from src.bot.utils.dispatcher import get_dispatcher
from src.db.create import create_database
from database.models import async_main
#logging.basicConfig(level=logging.INFO)


async def main() -> None:
    """ Entry point """
    await async_main()
    bot = Bot(token=conf.bot.token)
    try:
        dp = get_dispatcher()
        async with asyncio.TaskGroup() as tg:
            tg.create_task(create_database())
            tg.create_task(dp.start_polling(bot, skip_updates=True))
    except* TypeError as te:
        for errors in te.exceptions:
            print(errors)
    except* Exception as ex:
        print(ex.exceptions)

if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        print('Цикл был прерван пользователем')

