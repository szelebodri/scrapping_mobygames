class Game:
    def __init__(self, name=None, categories=None, date=None):
        self.name = name
        self.categories = categories
        self.date = date


class BannedException(Exception):
    def __init__(self, message="Too many requests"):
        self.message = message

