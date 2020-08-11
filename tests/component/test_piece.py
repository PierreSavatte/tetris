from unittest.mock import patch

import pytest

from tetris.components.board import Board
from tetris.components.cell import Cell
from tetris.components.piece import Piece, PieceBlueprints
from tetris.exceptions import CanNotMove


@pytest.fixture(
    params=list(PieceBlueprints),
    ids=[
        f"PieceBlueprints.{blueprint.name}"
        for blueprint in list(PieceBlueprints)
    ],
)
def piece_blueprint(request):
    return request.param.value


def test_piece_blueprints_holds_correct_data(piece_blueprint):
    assert isinstance(piece_blueprint.name, str)

    assert isinstance(piece_blueprint.spawning_cells, list)
    assert len(piece_blueprint.spawning_cells) == 4
    assert isinstance(piece_blueprint.spawning_cells[0], Cell)

    assert isinstance(piece_blueprint.rotation_cell, int)


@patch("random.randint")
def test_set_piece_can_give_random_piece(randint_mock):
    randint_mock.return_value = 3

    piece_blueprint = PieceBlueprints.get_random()

    assert piece_blueprint is list(PieceBlueprints)[3].value


def test_piece_can_only_can_be_init_with_a_blueprint(piece_blueprint):
    # Initialize piece with a blueprint
    p = Piece(piece_blueprint)
    assert p.name == piece_blueprint.name

    # Initialize piece with the values of the blueprint
    params = piece_blueprint._asdict()
    with pytest.raises(ValueError):
        Piece(params)


def test_piece_is_correctly_initialized(piece_blueprint):
    p = Piece(piece_blueprint)

    assert p.name == piece_blueprint.name

    cells_position = [c.position for c in p.cells]
    spawning_cells_position = [
        c.position for c in piece_blueprint.spawning_cells
    ]
    assert cells_position == spawning_cells_position
    assert p.id_rotation_cell == piece_blueprint.rotation_cell


@patch("tetris.components.cell.Cell.draw")
def test_piece_can_be_drawn(cell_draw_mocked, piece_blueprint):
    p = Piece(piece_blueprint)

    p.draw(None)

    assert cell_draw_mocked.call_count == 4


def test_piece_can_move(piece_blueprint, direction):
    b = Board(
        size=(10, 24), deactivated_cells=[Cell((0, 24), color=(0, 0, 0))],
    )
    p = Piece(piece_blueprint)
    # Overwrite piece's cells
    p.cells = [Cell((1, 1), (0, 0, 0)), Cell((1, 2), (0, 0, 0))]

    p.move(b, direction)

    if direction == (1, 0):
        new_positions = [(2, 1), (2, 2)]
    elif direction == (-1, 0):
        new_positions = [(0, 1), (0, 2)]
    elif direction == (0, 1):
        new_positions = [(1, 2), (1, 3)]
    else:
        new_positions = [(1, 0), (1, 1)]
    assert [c.position for c in p.cells] == new_positions


def test_piece_can_not_move_if_one_cell_has_obstacle(
    piece_blueprint, direction
):
    b = Board(
        size=(10, 24),
        deactivated_cells=[
            Cell((2, 1), (0, 0, 0)),
            Cell((4, 2), (0, 0, 0)),
            Cell((1, 3), (0, 0, 0)),
            Cell((3, 4), (0, 0, 0)),
        ],
    )
    p = Piece(piece_blueprint)
    # Overwrite piece's cells
    p.cells = [
        Cell((2, 2), (0, 0, 0)),
        Cell((3, 2), (0, 0, 0)),
        Cell((2, 3), (0, 0, 0)),
        Cell((3, 3), (0, 0, 0)),
    ]

    with pytest.raises(CanNotMove):
        p.move(b, direction)

    # Assert piece hasn't moved
    assert [c.position for c in p.cells] == [(2, 2), (3, 2), (2, 3), (3, 3)]


def test_piece_can_not_move_if_one_cell_is_on_the_border(
    piece_blueprint, direction
):
    b = Board(size=(2, 2))
    p = Piece(piece_blueprint)
    # Overwrite piece's cells
    p.cells = [
        Cell((0, 0), (0, 0, 0)),
        Cell((1, 0), (0, 0, 0)),
        Cell((0, 1), (0, 0, 0)),
        Cell((1, 1), (0, 0, 0)),
    ]

    with pytest.raises(CanNotMove):
        p.move(b, direction)

    # Assert piece hasn't moved
    assert [c.position for c in p.cells] == [(0, 0), (1, 0), (0, 1), (1, 1)]
