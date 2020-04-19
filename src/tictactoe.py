import json
from pathlib import Path


computation_resource_path = Path(__file__).parent / "resources/tictactoe-computation.json"
file = open(computation_resource_path)
computation_resource = json.loads(file.read())["wins"]
init_player = 1


class Game:
    def __init__(self):
        self.grid = Grid()
        self.current_player = toggle(init_player)
        self.started = False

    def start(self):
        self.grid = Grid()
        self.current_player = toggle(init_player)
        self.started = True

    def compute(self, position):
        if not self.started:
            raise Exception("Game not started")
        self.current_player = toggle(self.current_player)
        computation = self.grid.compute_move(position, self.current_player)
        if computation["win"]:
            self.started = False
        return computation


class Grid:
    def __init__(self):
        self.squares = [
            Square(), Square(), Square(),
            Square(), Square(), Square(),
            Square(), Square(), Square()
        ]

    def compute_move(self, position, player):
        self.squares[position].player = player
        valid_wins = list(filter(lambda x: position in x, computation_resource))
        win = True in list(all(self.squares[z].player == player for z in y) for y in valid_wins)
        return dict(win=win, player=player)


class Square:
    def __init__(self):
        self.player = 0


def toggle(player):
    player = 1 if player == 2 else 2
    return player
