import random
from collections import namedtuple
from enum import Enum

from . import Drawable
from .cell import Cell

PieceBlueprint = namedtuple(
    "PieceBlueprint", ["name", "spawning_cells", "rotation_cell", "color"]
)


class PieceBlueprints(Enum):
    I = PieceBlueprint(
        name="I",
        spawning_cells=[
            Cell((3, 0)),
            Cell((4, 0)),
            Cell((5, 0)),
            Cell((6, 0)),
        ],
        rotation_cell=1,
        color=(3, 155, 229),
    )
    J = PieceBlueprint(
        name="J",
        spawning_cells=[
            Cell((5, 0)),
            Cell((5, 1)),
            Cell((5, 2)),
            Cell((4, 2)),
        ],
        rotation_cell=1,
        color=(57, 73, 171),
    )
    L = PieceBlueprint(
        name="L",
        spawning_cells=[
            Cell((4, 0)),
            Cell((4, 1)),
            Cell((4, 2)),
            Cell((5, 2)),
        ],
        rotation_cell=1,
        color=(255, 179, 0),
    )
    O = PieceBlueprint(
        name="O",
        spawning_cells=[
            Cell((4, 0)),
            Cell((5, 0)),
            Cell((4, 1)),
            Cell((5, 1)),
        ],
        rotation_cell=0,
        color=(253, 216, 53),
    )
    S = PieceBlueprint(
        name="S",
        spawning_cells=[
            Cell((4, 0)),
            Cell((5, 0)),
            Cell((4, 1)),
            Cell((3, 1)),
        ],
        rotation_cell=0,
        color=(124, 179, 66),
    )
    T = PieceBlueprint(
        name="T",
        spawning_cells=[
            Cell((4, 0)),
            Cell((4, 1)),
            Cell((3, 1)),
            Cell((5, 1)),
        ],
        rotation_cell=1,
        color=(142, 36, 170),
    )
    Z = PieceBlueprint(
        name="Z",
        spawning_cells=[
            Cell((3, 0)),
            Cell((4, 0)),
            Cell((4, 1)),
            Cell((5, 1)),
        ],
        rotation_cell=1,
        color=(229, 57, 53),
    )

    @classmethod
    def get_random(cls):
        i = random.randint(0, len(cls))
        return list(cls)[i].value


class Piece(Drawable):
    def __init__(self, blueprint):
        if not isinstance(blueprint, PieceBlueprint):
            raise ValueError("Can not init a Piece without a blueprint.")

        self.name = blueprint.name
        self.cells = blueprint.spawning_cells
        self.id_rotation_cell = blueprint.rotation_cell
        self.color = blueprint.color

    def draw(self, screen):
        raise NotImplementedError()
