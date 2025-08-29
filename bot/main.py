import asyncio
from aiogram import Bot, Dispatcher
import os

from app.handlers import router

async def main():
    tgbot_token = os.getenv('TGBOT_TOKEN_APIKEY')
    bot = Bot(token=tgbot_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
