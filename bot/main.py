import asyncio

from aiogram import Bot, Dispatcher

import bot_config
import command_processing
import commands


async def start_bot(bot: Bot):
    await commands.set_commands(bot)
    for admin_id in bot_config.ADMIN_IDS:
        await bot.send_message(admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    for admin_id in bot_config.ADMIN_IDS:
        await bot.send_message(admin_id, text="Бот завершил работу!")


async def main():
    bot = Bot(token=bot_config.BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.include_router(command_processing.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
