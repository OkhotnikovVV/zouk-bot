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














from aiogram import types


async def main() -> None:
    """ Entry point """

    bot = Bot(token=conf.bot.token)
    await bot.set_my_commands([
        types.BotCommand(command="/start", description="it is start command..."),
        types.BotCommand(command="/help", description="it is help command...")
    ])


    try:
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
    except* TypeError as te:
        for errors in te.exceptions:
            print(errors)
    except* Exception as ex:
        print(ex.exceptions)

if __name__ == '__main__':
    # asyncio.run(main())
    try:
        # loop = asyncio.run(main())
        # loop = asyncio.get_running_loop()
        # loop.run_until_complete(main())
        # loop.run_until_complete(main())
        # asyncio.get_event_loop().run_until_complete(main())

        asyncio.run(main())

        # logging.info("bot stopped by ctrl+c")
    except KeyboardInterrupt:
        print('Цикл был прерван пользователем')
    # finally:
    #     storage_redis.close()
    #     storage_redis.redis.auto_close_connection_pool.
