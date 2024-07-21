from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands_for_users = [
        BotCommand(
            command="start",
            description="Начало работы",
        ),
        BotCommand(
            command="/exchange",
            description=("Перевести из одной валюты "
                         "в другую."),
        ),
        BotCommand(
            command="/rates",
            description=("Актуальные курсы валют."),
        ),
    ]
    await bot.set_my_commands(
        commands_for_users,
        scope=BotCommandScopeDefault()
    )
