from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy

from src.bot.handlers import routers
from src.bot.middlewares.mw import ThrottlingMiddleware
from src.bot.settings import conf
from aiogram.types.bot_command_scope_default import BotCommandScopeDefault


async def on_startup(bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Принять участие..."),
        types.BotCommand(command="go", description="Поехали..."),
        types.BotCommand(command="help", description="Что мы умеем..."),
    ], scope=BotCommandScopeDefault())


def get_dispatcher(fsm_strategy: FSMStrategy | None = FSMStrategy.USER_IN_CHAT) -> Dispatcher:
    """ This function set up dispatcher with routers, filters and middlewares. """

    storage = RedisStorage.from_url(f'{conf.redis.host}:{conf.redis.port}/{conf.redis.db}')

    dp = Dispatcher(storage=storage, fsm_strategy=fsm_strategy)
    dp.startup.register(on_startup)

    dp.update.middleware.register(ThrottlingMiddleware(storage=storage))

    for router in routers:
        dp.include_router(router)

    return dp
