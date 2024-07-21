from os import getenv

from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = getenv("REDDIS_HOST", "localhost")
REDIS_PORT = int(getenv("REDDIS_PORT", 6379))
REDIS_DB = int(getenv("REDDIS_DB", 0))

RATES_URL = getenv("RATES_URL")
