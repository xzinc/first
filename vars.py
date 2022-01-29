from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 7326452 #config("API_ID", default=None, cast=int)
API_HASH = a865401e13d06664d7ffa3558f8e2940 #config("API_HASH", default=None)
BOT_TOKEN = 2137176477:AAGg7HO6ocUL3fauzemTe1CqP0_XInP1bos#config("BOT_TOKEN", default=None)

midway = TelegramClient('midwayx', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
