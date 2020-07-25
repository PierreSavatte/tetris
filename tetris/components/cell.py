import pygame

from ..constants import RECT_SIZE
from . import Drawable


class CanNotMoveDown(Exception):
    pass


class Cell(Drawable):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    @staticmethod
    def can_move(board, future_position):
        return board.position_is_inside(future_position) and (
            future_position not in board.get_positions_of_deactivated_cells()
        )

    def can_move_down(self, board):
        (x, y) = self.position
        future_position = x, y + 1
        return self.can_move(board, future_position)

    def move(self, board, future_position):
        if not self.can_move(board, future_position):
            raise CanNotMoveDown("Cell can not move down.")
        else:
            self.position = future_position

    def move_down(self, board):
        (x, y) = self.position
        future_position = x, y + 1
        self.move(board, future_position)

    def move_left(self, board):
        (x, y) = self.position
        future_position = x - 1, y
        self.move(board, future_position)

    def move_right(self, board):
        (x, y) = self.position
        future_position = x + 1, y
        self.move(board, future_position)

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE)
        pygame.draw.rect(screen, self.color, rect)
