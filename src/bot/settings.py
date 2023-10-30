import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class DbConf:
    """ Database connection variables """

    path: str = os.environ.get("DATABASE_PATH", "../db/data/my_database.db")


@dataclass(frozen=True)
class RedisConf:
    """ Redis connection variables """

    host: str = os.environ.get("REDIS_HOST", "redis://127.0.0.1")
    port: int = int(os.environ.get("REDIS_PORT", 6379))
    db: str = int(os.environ.get("REDIS_DATABASE", 0))


@dataclass(frozen=True)
class CacheConf:
    """ Redis-cache connection variables """

    host: str = os.environ.get("REDIS_HOST", "redis://127.0.0.1")
    port: int = int(os.environ.get("REDIS_PORT", 6379))
    db: str = int(os.environ.get("REDIS_DATABASE", 1))


@dataclass(frozen=True)
class BotConf:
    """ Bot variables """
    token: str = os.environ.get("TOKEN")


@dataclass(frozen=True)
class Configs:
    """ All in one configuration's class """

    bot = BotConf()
    redis = RedisConf()
    db = DbConf()
    cache = CacheConf()


conf = Configs()
