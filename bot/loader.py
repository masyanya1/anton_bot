from aiogram import Bot, Dispatcher
from config import *

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

from handlers import start

dp.include_routers(
        start.router
        )

