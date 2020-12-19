from aiogram.utils.markdown import markdown_decoration


class Event:
    def __init__(self, name: str, link: str, start_date: str, finish_date: str, format: str, weight: str, id):
        self.name = markdown_decoration.quote(name)
        self.link = link
        self.start_date = markdown_decoration.quote(start_date)
        self.finish_date = markdown_decoration.quote(finish_date)
        self.format = markdown_decoration.quote(format)
        self.weight = markdown_decoration.quote(weight)
        self.id = id.replace('https://ctftime.org/event/', '')

    def __iter__(self):
        yield 'name', self.name
        yield 'link', self.link
        yield 'start_date', self.start_date
        yield 'finish_date', self.finish_date
        yield 'format', self.format
        yield 'weight', self.weight
        yield 'id', self.id

    def __repr__(self):
        return f'<Event name={self.name}>'
