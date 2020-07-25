import random
from collections import namedtuple
from enum import Enum

from . import Drawable
from .cell import Cell, CanNotMoveDown

PieceBlueprint = namedtuple(
    "PieceBlueprint", ["name", "spawning_cells", "rotation_cell"]
)


class PieceBlueprints(Enum):
    I = PieceBlueprint(
        name="I",
        spawning_cells=[
            Cell((3, 0), color=(3, 155, 229)),
            Cell((4, 0), color=(3, 155, 229)),
            Cell((5, 0), color=(3, 155, 229)),
            Cell((6, 0), color=(3, 155, 229)),
        ],
        rotation_cell=1,
    )
    J = PieceBlueprint(
        name="J",
        spawning_cells=[
            Cell((5, 0), color=(57, 73, 171)),
            Cell((5, 1), color=(57, 73, 171)),
            Cell((5, 2), color=(57, 73, 171)),
            Cell((4, 2), color=(57, 73, 171)),
        ],
        rotation_cell=1,
    )
    L = PieceBlueprint(
        name="L",
        spawning_cells=[
            Cell((4, 0), color=(255, 179, 0)),
            Cell((4, 1), color=(255, 179, 0)),
            Cell((4, 2), color=(255, 179, 0)),
            Cell((5, 2), color=(255, 179, 0)),
        ],
        rotation_cell=1,
    )
    O = PieceBlueprint(
        name="O",
        spawning_cells=[
            Cell((4, 0), color=(253, 216, 53)),
            Cell((5, 0), color=(253, 216, 53)),
            Cell((4, 1), color=(253, 216, 53)),
            Cell((5, 1), color=(253, 216, 53)),
        ],
        rotation_cell=0,
    )
    S = PieceBlueprint(
        name="S",
        spawning_cells=[
            Cell((4, 0), color=(124, 179, 66)),
            Cell((5, 0), color=(124, 179, 66)),
            Cell((4, 1), color=(124, 179, 66)),
            Cell((3, 1), color=(124, 179, 66)),
        ],
        rotation_cell=0,
    )
    T = PieceBlueprint(
        name="T",
        spawning_cells=[
            Cell((4, 0), color=(142, 36, 170)),
            Cell((4, 1), color=(142, 36, 170)),
            Cell((3, 1), color=(142, 36, 170)),
            Cell((5, 1), color=(142, 36, 170)),
        ],
        rotation_cell=1,
    )
    Z = PieceBlueprint(
        name="Z",
        spawning_cells=[
            Cell((3, 0), color=(229, 57, 53)),
            Cell((4, 0), color=(229, 57, 53)),
            Cell((4, 1), color=(229, 57, 53)),
            Cell((5, 1), color=(229, 57, 53)),
        ],
        rotation_cell=1,
    )

    @classmethod
    def get_random(cls):
        i = random.randint(0, len(cls) - 1)
        return list(cls)[i].value


class Piece(Drawable):
    def __init__(self, blueprint):
        if not isinstance(blueprint, PieceBlueprint):
            raise ValueError("Can not init a Piece without a blueprint.")

        self.name = blueprint.name
        self.cells = blueprint.spawning_cells
        self.id_rotation_cell = blueprint.rotation_cell

    def move_down(self, board):
        if all(c.can_move_down(board) for c in self.cells):
            for c in self.cells:
                c.move_down(board)
        else:
            raise CanNotMoveDown("Piece can not move down.")

    def draw(self, screen):
        for c in self.cells:
            c.draw(screen)
