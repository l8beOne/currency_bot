from redis import Redis

from service_config import REDIS_DB, REDIS_HOST, REDIS_PORT


async def update_redis(rates):
    rds = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    for currency, rate in rates.items():
        rds.set(currency, rate)
    rds.set("RUB", 1)
