from core import dp
from aiogram import types
from source.handlers.ctftime_api.rss.rssHandler import get_upcoming_events
from aiogram.utils.markdown import markdown_decoration


def generate_calendar() -> str:
    template = '''*\\#\\#\\#*
    
{eventTitle}: \\[{fromDate} \\- {toDate}\\]
•Format: {format}
•Weight: {weight}
•ID: {id}

'''

    calendar = 'Calendar of upcoming events:\n'


    for event in get_upcoming_events():
        calendar += template.format(eventTitle=markdown_decoration.link(event.name, event.link),
                                    fromDate=event.start_date,
                                    toDate=event.finish_date,
                                    format=event.format,
                                    weight=event.weight,
                                    id=event.id
                                    )

    return calendar



@dp.message_handler(commands=['calendar'])
async def command_calendar(message: types.Message):
    await message.reply(text=generate_calendar() ,parse_mode='MarkdownV2', disable_notification=True)

@dp.message_handler(commands=['fool'])
async def fool_handler(message: types.Message):  # Haha
    await message.reply('Семен \(@Frovy\) сегодня гандон\.\nКаждый день избирается новый гандон\. Может быть им станешь именно ты\!', parse_mode='MarkdownV2', disable_notification=True)