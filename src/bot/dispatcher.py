from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage   # Не рекомендуется использовать этот Storage. Так как данные из него пропадут при перезагрузке
from handlers import routers
from aiogram.fsm.strategy import FSMStrategy
from aiogram.fsm.storage.redis import RedisStorage
# from aioredis.client import Redis
from src.bot.middlewares.mw import ThrottlingMiddleware


def get_dispatcher(
        storage: BaseStorage = MemoryStorage(),
        fsm_strategy: FSMStrategy | None = FSMStrategy.USER_IN_CHAT,
        ):
    dp = Dispatcher(storage=storage, fsm_strategy=fsm_strategy)  # bot)#, storage=storage)
    storage_redis = RedisStorage.from_url('redis://127.0.0.1:6379/0')
    dp.update.middleware.register(ThrottlingMiddleware(storage=storage_redis))

    for router in routers:
        dp.include_router(router)

    return dp
