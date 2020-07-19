from aiogram.utils.markdown import markdown_decoration


class Event:
    def __init__(self, name: str, link: str, start_date: str, finish_date: str, format: str, weight: str, id):
        # TODO: Refactor
        # https://ru.stackoverflow.com/questions/1154855/python3-%d0%bf%d1%80%d0%be%d0%b3%d0%bd%d0%b0%d1%82%d1%8c-%d0%b2%d1%81%d0%b5-%d1%81%d0%b2%d0%be%d0%b9%d1%81%d1%82%d0%b2%d0%b0-%d0%ba%d0%bb%d0%b0%d1%81%d1%81%d0%b0-%d1%87%d0%b5%d1%80%d0%b5%d0%b7-%d0%bc%d0%b5%d1%82%d0%be%d0%b4
        # map(func, (getattr(self, x) for x in dir(self)))
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
