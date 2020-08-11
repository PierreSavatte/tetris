import logging

import pygame

from . import Drawable
from .piece import Piece, PieceBlueprints
from ..constants import LOGGER_LEVEL, BLACK, RECT_SIZE, DOWN, RIGHT, LEFT
from ..exceptions import CanNotMove, GameOver

logging.basicConfig(level=LOGGER_LEVEL)


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
        for deactivated_cell in self.deactivated_cells:
            deactivated_cell.draw(screen)
        if self.active_piece:
            self.active_piece.draw(screen)

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
            if not self.active_piece.can_move(self, DOWN):
                raise GameOver("Spawning piece can not move down.")
        else:
            if pygame.K_UP in keys_pressed:
                self.active_piece.go_at_the_bottom(self)

            try:
                self.active_piece.move(self, DOWN)
            except CanNotMove:
                self.deactivated_cells.extend(self.active_piece.cells)
                self.set_random_active_piece()
                if not self.active_piece.can_move(self, DOWN):
                    raise GameOver("Spawning piece can not move down.")

            if pygame.K_LEFT in keys_pressed:
                try:
                    self.active_piece.move(self, LEFT)
                except CanNotMove as e:
                    logging.debug(e)
            if pygame.K_RIGHT in keys_pressed:
                try:
                    self.active_piece.move(self, RIGHT)
                except CanNotMove as e:
                    logging.debug(e)
