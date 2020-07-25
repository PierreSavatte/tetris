import pygame

from ..constants import RECT_SIZE
from . import Drawable


class CanNotMoveDown(Exception):
    pass


class Cell(Drawable):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    @property
    def future_position(self):
        (x, y) = self.position
        return x, y + 1

    def can_move_down(self, board):
        return board.position_is_inside(self.future_position) and (
            self.future_position
            not in board.get_positions_of_deactivated_cells()
        )

    def move_down(self, board):
        if not self.can_move_down(board):
            raise CanNotMoveDown("Cell can not move down.")
        else:
            self.position = self.future_position

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE)
        pygame.draw.rect(screen, self.color, rect)
