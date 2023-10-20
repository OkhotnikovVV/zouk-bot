import asyncio
# import logging
from aiogram import Bot

from src.bot.utils.dispatcher import get_dispatcher
from src.db.create import create_database
from src.bot.settings import conf
#logging.basicConfig(level=logging.INFO)


async def my_coroutine() -> None:
    """ Your asynchronous task logic goes here """
    print("Executing my coroutine...")


async def start_bot():
    print('Бот запущен')


async def stop_bot():
    print('Бот остановлен')


async def main() -> None:
    """ Entry point """

    bot = Bot(token=conf.bot.token)
    dp = get_dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    async with asyncio.TaskGroup() as tg:


        # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
        #
        # scheduler.add_job(my_coroutine, trigger='date',
        #                   run_date=datetime.datetime.strptime('2023-10-09 22:59:33.066562', '%Y-%m-%d %H:%M:%S.%f'))
        # scheduler.start()

        tg.create_task(create_database())
        tg.create_task(dp.start_polling(bot, skip_updates=True))


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
        # logging.info("bot stopped by ctrl+c")
    # finally:
    #     storage_redis.close()
    #     storage_redis.redis.auto_close_connection_pool.
