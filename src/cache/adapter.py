""" This file contains the cache adapter """
import asyncio
from typing import Any, List, Optional, TypeVar, final, overload

from redis.asyncio.client import Redis

from src.bot.settings import conf

KeyLike = TypeVar("KeyLike", str, int)


def build_redis_client():
    """Build redis client"""
    client = Redis.from_url(f'{conf.redis.host}:{conf.redis.port}/1')
    return client


class Cache:
    """Cache adapter"""

    def __init__(self, redis: Optional[Redis] = None):
        self.client = redis or build_redis_client()


cache = Cache()
