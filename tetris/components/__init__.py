from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self, screen):
        pass


from .board import Board
from .cell import Cell
from .piece import Piece, PieceBlueprints
