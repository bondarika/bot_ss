import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv 
import os
from handlers import user_commands

load_dotenv()
# Запуск бота
async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(user_commands.router)
    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())