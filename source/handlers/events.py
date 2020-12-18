from core import dp
from aiogram import types
from source.handlers.rss.rssHandler import get_upcoming_events
from aiogram.utils.markdown import markdown_decoration
from source.handlers.api.ctftime_api import get_event
from datetime import datetime


def generate_calendar() -> str:
    template = '\\#\\#\\#\n{eventTitle}: \\[{fromDate} \\- {toDate}\\] \n•Format: {format} \n•Weight: {weight}\n•ID: {id}\n'

    calendar = 'Calendar of upcoming events:\n'


    for event in get_upcoming_events():
        calendar += template.format(eventTitle=markdown_decoration.link(event.name, event.link),
                                    fromDate=event.start_date,
                                    toDate=event.finish_date,
                                    format=event.format,
                                    weight=event.weight,
                                    id=event.id
                                    )

    return calendar + "\\#\\#\\#"



@dp.message_handler(commands=['calendar'])
async def command_calendar(message: types.Message):
    await message.reply(text=generate_calendar() ,parse_mode='MarkdownV2')

@dp.message_handler(commands=['fool'])
async def fool_handler(message: types.Message):
    await message.reply('Семен \(@Frovy\) сегодня гандон\.\nКаждый день избирается новый гандон\. Может быть им станешь именно ты\!', parse_mode='MarkdownV2')

# @dp.message_handler(commands=['join'])
# async def command_join(message: types.Message):
#     await message.reply('This function not implemented yet')
#     return
#
#     import re
#     import pytz
#     try:
#         id = int(message.text.split()[1])
#     except:
#         await message.reply('Bad ID passed')
#         return
#
#     event = get_event(id)['finish']
#     event = re.sub(r'\+.*', '', event)
#
#
#     if datetime.strptime(get_event(id)['finish'], '%Y-%m-%dT%H:%M%S') <= datetime.now(pytz.timezone('Europe/Moscow')): # ISO 8601
#         await message.reply('CTF with this ID already finished.')
#         return