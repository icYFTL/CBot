from aiogram.utils.markdown import markdown_decoration


class Event:
    def __init__(self, name: str, link: str, start_date: str, finish_date: str, format: str, weight: str, id):
        self.name = name
        self.link = link
        self.start_date = start_date
        self.finish_date = finish_date
        self.format = format
        self.weight = weight
        self.id = id.replace('https://ctftime.org/event/', '')
        self.markdown_beautify()

    def markdown_beautify(self):
        for x in filter(lambda el: not el.startswith('__') and
                                   not callable(getattr(self, el) and
                                   el not in ['link', 'id']),
                        dir(self)
                        ):
            print([x for x in filter(lambda el: not el.startswith('__') and
                                   not callable(getattr(self, el) and
                                   el not in ['link', 'id']),
                        dir(self))])
            print(getattr(self, x))
            setattr(self, x, markdown_decoration.quote(getattr(self, x)))

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

Event("lol","kek","n1ce","aaa","bbb.*","ф","-")