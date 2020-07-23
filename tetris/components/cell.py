from . import Drawable


class CanNotMoveDown(Exception):
    pass


class Cell(Drawable):
    def __init__(self, position):
        self.position = position

    def move_down(self, board):
        (x, y) = self.position
        future_position = (x, y + 1)
        if not board.position_is_inside(future_position):
            raise CanNotMoveDown("Can not go outside the board")
        elif future_position not in board.get_positions_of_deactivated_cells():
            raise CanNotMoveDown("Can not override a deactivated cell")
        else:
            self.position = future_position
