import feedparser
from datetime import datetime
from core import config
import logging
from source.abstract.Event import Event


def get_upcoming_events() -> list:
    d = feedparser.parse(config['ctftime']['upcoming_events_url'])
    data = list()
    logging.getLogger('RSS')

    for x in d['entries'][:5]:
        try:
            data.append(Event(name=x['title'],
                              link=x['link'],
                              start_date=datetime.strftime(datetime.strptime(x['start_date'], '%Y%m%dT%H%M%S'), '%m/%d %H:%M'), # ISO 8601
                              finish_date=datetime.strftime(datetime.strptime(x['finish_date'], '%Y%m%dT%H%M%S'), '%m/%d %H:%M'), # ISO 8601
                              format=x['format_text'],
                              weight=x['weight'] if float(x['weight']) != 0.00 else 'Undefined',
                              id=x['id']
                              ))
        except Exception as e:
            logging.error(str(e))
    return data
