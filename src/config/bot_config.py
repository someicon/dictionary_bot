import os
import dotenv

from aiogram import Bot, Dispatcher

dotenv.load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
