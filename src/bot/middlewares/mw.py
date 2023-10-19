from typing import Any, Awaitable, Callable, Dict, cast
from aiogram import BaseMiddleware
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.storage.redis import RedisStorage

from aiogram.types import Message, TelegramObject
from aiogram.enums.parse_mode import ParseMode
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender







class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, storage: RedisStorage):
        # super().__init__()
        self.storage = storage
        self.counter = 0


    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ) -> Any:

        user = event.message.from_user.id

        check_user = await self.storage.redis.get(name=user)
        print(self.counter)
        if check_user:
            self.counter += 1

            self.ttl_counter = await self.storage.redis.ttl(name=user)
            if self.ttl_counter > 50:
                self.ttl_counter = 50
            await self.storage.redis.set(name=user, value=self.counter, ex=self.ttl_counter + self.counter)

            if int(check_user) > 10:
                return await event.message.answer(f"""
                Мы обнаружили повышенную активность.
                Вы сможете отправлять сообщения вновь через {await self.storage.redis.ttl(name=user)} секунд.
                """)
        else:
            self.counter = 1
            await self.storage.redis.set(name=user, value=1, ex=10)





        return await handler(event, data)





class ChatActionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        long_operation_type = get_flag(data, "long_operation")

        # Если такого флага на хэндлере нет
        if not long_operation_type:
            return await handler(event, data)

        # Если флаг есть
        async with ChatActionSender(
                action=long_operation_type,
                chat_id=event.chat.id
        ):
            return await handler(event, data)

# Соответственно, чтобы флаг был прочитан, его надо где-то указать.
# Вариант: @dp.message(<тут ваши фильтры>, flags={"long_operation": "upload_video_note"})