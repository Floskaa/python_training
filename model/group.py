from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # representation - стандартная функция - определяет как будет выглядеть объект при выводе на консоль
    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    # equels - функция принимающая в качестве второго параметра обьект с которым мы должны сравнить текущий обьект self
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
