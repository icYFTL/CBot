from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import json
import logging

logging.basicConfig(filename='cbot.log', level=logging.INFO,
                    format='%(asctime)-15s | [%(name)s] %(levelname)s => %(message)s')

config = json.load(open('config.json', 'r'))
text = config['msg_en']

bot = Bot(token=config['tg_token'])
dp = Dispatcher(bot)