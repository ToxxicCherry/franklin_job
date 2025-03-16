import asyncio
from aiogram import Dispatcher
from bot import bot
from client import tg_client
from database import init_db


dp = Dispatcher()


async def main():
    await init_db()
    await tg_client.start()
    await tg_client.run_until_disconnected()
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

