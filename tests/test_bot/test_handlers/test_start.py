from unittest.mock import AsyncMock

import pytest
import pytest_asyncio
from aiogram.handlers import MessageHandler

from bot.handlers.start import command_start
from conftest import memory_storage
from mocked_bot import MockedBot


@pytest.mark.asyncio()
async def test_start_handler(memory_storage):
    message = AsyncMock()
    db = memory_storage()
    await command_start(message)

    message.answer.assert_called_with("Welcome!")
