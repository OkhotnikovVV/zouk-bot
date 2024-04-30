from unittest.mock import AsyncMock

import pytest

from bot.handlers.start import command_start


@pytest.mark.asyncio()
async def test_start_handler():
    message = AsyncMock()
    await command_start(message)

    message.answer.assert_called_with("Welcome!")
