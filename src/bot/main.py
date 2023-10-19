# import logging
import asyncio
from aiogram import Bot
from src.bot.dispatcher import get_dispatcher
# from keyboards import organizator
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# import datetime
from src.db.create import create_database
import os
from dotenv import load_dotenv

#logging.basicConfig(level=logging.INFO)

load_dotenv()

token = os.environ.get('token')


async def my_coroutine():
    # Your asynchronous task logic goes here
    print("Executing my coroutine...")
bot = Bot(token=token)
dp = get_dispatcher()

async def main() -> None:
    """Entry point
    """


    async with asyncio.TaskGroup() as tg:
        # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
        #
        # scheduler.add_job(my_coroutine, trigger='date',
        #                   run_date=datetime.datetime.strptime('2023-10-09 22:59:33.066562', '%Y-%m-%d %H:%M:%S.%f'))
        # scheduler.start()

        # And the run events dispatching
        tg.create_task(create_database())
        tg.create_task(dp.start_polling(bot))
        # await database.create_database()
        # await database.get_users(path_database)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
        # logging.info("bot stopped by ctrl+c")
