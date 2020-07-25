import pygame

from ..constants import RECT_SIZE
from . import Drawable


class CanNotMoveDown(Exception):
    pass


class Cell(Drawable):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move_down(self, board):
        (x, y) = self.position
        future_position = (x, y + 1)
        if not board.position_is_inside(future_position):
            raise CanNotMoveDown("Can not go outside the board")
        elif future_position in board.get_positions_of_deactivated_cells():
            raise CanNotMoveDown("Can not override a deactivated cell")
        else:
            self.position = future_position

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE)
        pygame.draw.rect(screen, self.color, rect)
