import asyncio
from aiogram import Dispatcher
from .create_bot import bot
from database import init_db


dp = Dispatcher()


async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

