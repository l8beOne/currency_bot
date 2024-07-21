import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from exchange_rates import get_exchange_rates, parser
from update_redis import update_redis


async def main():
    data = await get_exchange_rates()
    rates = parser(data)
    await update_redis(rates)


def apscheduler():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        main,
        trigger="cron",
        hour=0,
        minute=0
    )
    scheduler.start()


if __name__ == "__main__":
    apscheduler()
    asyncio.get_event_loop().run_forever()
