import pygame

from . import Drawable
from ..constants import RECT_SIZE
from ..exceptions import CanNotMove


class Cell(Drawable):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def compute_future_position(self, direction):
        return (
            self.position[0] + direction[0],
            self.position[1] + direction[1],
        )

    def can_move(self, board, direction):
        future_position = self.compute_future_position(direction)
        return board.position_is_inside(future_position) and (
            future_position not in board.positions_of_deactivated_cells
        )

    def move(self, board, direction):
        if not self.can_move(board, direction):
            raise CanNotMove("Cell can not move.")
        else:
            self.position = self.compute_future_position(direction)

    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE)
        pygame.draw.rect(screen, self.color, rect)
