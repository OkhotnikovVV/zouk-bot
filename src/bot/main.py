import asyncio
# import logging
from aiogram import Bot

from src.bot.settings import conf
from src.bot.utils.dispatcher import get_dispatcher
from src.db.create import create_database

#logging.basicConfig(level=logging.INFO)


async def my_coroutine() -> None:
    """ Your asynchronous task logic goes here """
    print("Executing my coroutine...")


async def main() -> None:
    """ Entry point """

    bot = Bot(token=conf.bot.token)
    # await cache.set('dfgdf', 'sdgfsdfgdf')
    # await bot.set_my_commands([
    #     types.BotCommand(command="/start", description="it is start command..."),
    #     types.BotCommand(command="/help", description="it is help command...")
    # ])

    try:
        dp = get_dispatcher()

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
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        print('Цикл был прерван пользователем')

