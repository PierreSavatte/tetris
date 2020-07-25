import pygame

from ..constants import BLACK, RECT_SIZE
from . import Drawable


class Board(Drawable):
    def __init__(self, size, deactivated_cells=None):
        self.size = size

        self.active_piece = None
        self.deactivated_cells = deactivated_cells or []

    def position_is_inside(self, position):
        x_max = self.size[0]
        y_max = self.size[1]
        (x, y) = position
        return x in range(x_max + 1) and y in range(y_max + 1)

    def get_positions_of_deactivated_cells(self):
        return [c.position for c in self.deactivated_cells]

    def draw(self, screen):
        self.active_piece.draw(screen)
        for deactivated_cell in self.deactivated_cells:
            deactivated_cell.draw(screen)

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE),
                    1,
                )
