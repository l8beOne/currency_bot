from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from redis import Redis

from bot_config import REDIS_DB, REDIS_HOST, REDIS_PORT

router = Router()
rds = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


@router.message(Command(commands=["exchange"]))
async def exchange_command(message: Message):
    """
    Показывает стоимость, указазанной первым аргументом,
    валюты через валюту, указанную вторым аргументом.
    """
    args = " ".join(message.text.split()[1:])
    if not args:
        await message.answer(
            "Instance: /exchange from_currency to_currency quantity"
        )
        return
    try:
        from_curr = message.text.split()[1]
        to_curr = message.text.split()[2]
        quantity = message.text.split()[3]
        from_value = float(rds.get(from_curr))
        to_value = float(rds.get(to_curr))
        quantity = float(quantity)
        result = from_value * quantity / to_value
        response = f"{result}"
    except Exception as error:
        response = "Instance: /exchange from_currency to_currency quantity"
    await message.reply(response)


@router.message(Command(commands=["rates"]))
async def rates_command(message: Message):
    """
    Отправляет пользователю актуальные курсы валют.
    """
    curr_rates = {}
    for key in rds.keys():
        curr_rates[key.decode("utf-8")] = float(rds.get(key))
    response = "\n".join(
        [
            f"{currency}: {rate} RUB" for currency, rate in curr_rates.items()
        ]
    )
    await message.answer(response)
