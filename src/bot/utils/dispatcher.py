from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy

from src.bot.handlers import routers
from src.bot.middlewares.mw import ThrottlingMiddleware
from src.bot.settings import conf


def get_dispatcher(fsm_strategy: FSMStrategy | None = FSMStrategy.USER_IN_CHAT) -> Dispatcher:
    """ This function set up dispatcher with routers, filters and middlewares. """

    storage = RedisStorage.from_url(f'{conf.redis.host}:{conf.redis.port}/{conf.redis.db}')

    dp = Dispatcher(storage=storage, fsm_strategy=fsm_strategy)

    dp.update.middleware.register(ThrottlingMiddleware(storage=storage))

    for router in routers:
        dp.include_router(router)

    return dp
