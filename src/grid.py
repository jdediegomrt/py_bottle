

class Grid:
    def __init__(self):
        self.rows = [Row(0), Row(1), Row(2)]


class Row:
    def __init__(self, position):
        self.position = position
        self.squares = [Square(0), Square(1), Square(2)]


class Square:
    def __init__(self, position):
        self.position = position
        self.player = 0

