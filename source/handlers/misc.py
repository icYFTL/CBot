from core import dp, text
from aiogram import types
from source.handlers.api.ctftime_api import *

def generate_a_commands():
    return '\n'.join([f"{x[0] + 1}. {x[1]}" for x in enumerate(text['available_commands'].split('\n'))])

def generate_position(repl: dict):
    template = '''Our statistic for {year}:
• World place: {wPlace}
• {country} place: {cPlace}
• PTS: {pts}'''

    year = list(repl['rating'][0])[0]
    world_place = repl['rating'][0][year]['rating_place']
    pts = repl['rating'][0][year]['rating_points']
    country_place = repl['country_place']
    country = repl.get('country', 'Country')

    return template.format(year=year,
                           wPlace=world_place,
                           country=country,
                           cPlace=country_place,
                           pts=pts
                           )

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply(text=text['start_msg'].format(commands=generate_a_commands()))

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(text='Available commands:\n' + generate_a_commands())

@dp.message_handler(commands=['pos'])
async def command_pos(message: types.Message):
    repl = get_team(config['ctftime']['team_id'])
    await message.reply(text=generate_position(repl))




