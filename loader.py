from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = '6979979883:AAEZJPdxMb5_AY-szgsXGlC2pRQiBEZjtr4'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)