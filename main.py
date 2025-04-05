import asyncio
import logging

from src.config.bot_config import bot, dp
from src.handlers.user import user_router

logging.basicConfig(level=logging.INFO)

dp.include_router(user_router)


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот остановлен')
