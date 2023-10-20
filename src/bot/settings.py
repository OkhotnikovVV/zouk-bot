import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class RedisConf:
    """ Redis connection variables """

    host: str = os.environ.get("REDIS_HOST", "redis://127.0.0.1")
    port: int = int(os.environ.get("REDIS_PORT", 6379))
    db: str = int(os.environ.get("REDIS_DATABASE", 0))


@dataclass
class BotConf:
    """ Bot connection variables """
    token: str = os.environ.get("TOKEN")


@dataclass
class Configs:
    """ All in one configuration's class """

    bot = BotConf()
    redis = RedisConf()


conf = Configs()
