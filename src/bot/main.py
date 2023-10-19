import os
import asyncio
# import logging
from aiogram import Bot
from dotenv import load_dotenv

from src.bot.dispatcher import get_dispatcher
from src.db.create import create_database


#logging.basicConfig(level=logging.INFO)

load_dotenv()

token = os.environ.get('TOKEN')


async def my_coroutine() -> None:
    """ Your asynchronous task logic goes here """
    print("Executing my coroutine...")



async def main() -> None:
    """ Entry point """
    bot = Bot(token=token)
    dp = get_dispatcher()

    async with asyncio.TaskGroup() as tg:
        # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
        #
        # scheduler.add_job(my_coroutine, trigger='date',
        #                   run_date=datetime.datetime.strptime('2023-10-09 22:59:33.066562', '%Y-%m-%d %H:%M:%S.%f'))
        # scheduler.start()

        tg.create_task(create_database())
        tg.create_task(dp.start_polling(bot))


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
        # logging.info("bot stopped by ctrl+c")
