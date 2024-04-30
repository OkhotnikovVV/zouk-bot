from unittest.mock import AsyncMock

import pytest

from bot.handlers.start import command_start
from conftest import memory_storage


@pytest.mark.asyncio()
async def test_start_handler(memory_storage):
    message = AsyncMock()
    db = memory_storage
    await command_start(message)

    message.answer.assert_called_with("Welcome!")
