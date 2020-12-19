from core import dp, text, config
from aiogram import types
from source.handlers.ctftime_api.ctftime_api import *
from source.utils import toFixed

def generate_a_commands():
    return '\n'.join([f"{x[0] + 1}. {x[1]}" for x in enumerate(text['available_commands'].split('\n'))])

def generate_position(repl: dict):
    template = '''Our statistic for {year}:
• World place: {wPlace}
• {country} place: {cPlace}
• PTS: {pts}'''

    year = list(repl['rating'][0])[0]
    world_place = repl['rating'][0][year]['rating_place']
    pts = toFixed(repl['rating'][0][year]['rating_points'], 2)
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
    await message.reply(text=text['start_msg'].format(commands=generate_a_commands()), disable_notification=True)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(text='Available commands:\n' + generate_a_commands(), disable_notification=True)

@dp.message_handler(commands=['pos'])
async def command_pos(message: types.Message):
    sub_mes = await message.reply('Calculating...', disable_notification=True)
    repl = get_team(config['ctftime']['team_id'])
    await sub_mes.edit_text(text=generate_position(repl))




