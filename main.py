import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

from handlers.routers import router as start_router
from handlers.language import router as lang_router
from handlers.db import init_db

load_dotenv()

bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(lang_router)


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())