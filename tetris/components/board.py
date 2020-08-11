import pygame

from . import Drawable
from .piece import Piece, PieceBlueprints
from ..constants import BLACK, RECT_SIZE
from ..exceptions import CanNotMove


class Board(Drawable):
    def __init__(self, size, deactivated_cells=None):
        self.size = size

        self.active_piece = None
        self.deactivated_cells = deactivated_cells or []

    def position_is_inside(self, position):
        x_max = self.size[0]
        y_max = self.size[1]
        (x, y) = position
        return x in range(x_max) and y in range(y_max)

    @property
    def positions_of_deactivated_cells(self):
        return [c.position for c in self.deactivated_cells]

    def draw(self, screen):
        if self.active_piece:
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

    def set_random_active_piece(self):
        self.active_piece = Piece(PieceBlueprints.get_random())

    def update(self, keys_pressed):
        if not self.active_piece:
            self.set_random_active_piece()
        else:
            if pygame.K_UP in keys_pressed:
                print(
                    "Should go directly at the bottom, but not implemented yet."
                )
            else:
                try:
                    self.active_piece.move_down(self)
                except CanNotMove:
                    self.deactivated_cells.extend(self.active_piece.cells)
                    self.set_random_active_piece()

            if pygame.K_LEFT in keys_pressed:
                self.active_piece.move_left(self)
            if pygame.K_RIGHT in keys_pressed:
                self.active_piece.move_right(self)
