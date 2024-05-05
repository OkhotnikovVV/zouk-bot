from unittest.mock import AsyncMock

import pytest
import pytest_asyncio
from aiogram.handlers import MessageHandler

from bot.handlers.start import command_start, command_help
from conftest import memory_storage
from database.requests import create_user
from mocked_bot import MockedBot


@pytest.mark.asyncio()
async def test_start_handler():
    message = AsyncMock()

    await command_start(message)
    message.answer.assert_called_with("Welcome!")


@pytest.mark.asyncio()
async def test_help_handler():
    message = AsyncMock()

    await command_help(message)
    message.answer.assert_called_with("It is help!")
