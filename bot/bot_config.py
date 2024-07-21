from os import getenv
from typing import List

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")

ADMIN_IDS: List[int] = list(map(int, str(getenv("ADMIN_IDS")).split(",")))

REDIS_HOST = getenv("REDDIS_HOST", "localhost")
REDIS_PORT = int(getenv("REDDIS_PORT", 6379))
REDIS_DB = int(getenv("REDDIS_DB", 0))

RATES_URL = getenv("RATES_URL")
