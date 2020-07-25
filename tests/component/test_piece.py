from unittest.mock import patch

import pytest

from tetris.components.cell import Cell
from tetris.components.piece import Piece, PieceBlueprints


@pytest.fixture
def piece_blueprint():
    return list(PieceBlueprints)[0].value


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
    p = Piece(piece_blueprint)

    assert p.name == piece_blueprint.name

    params = piece_blueprint._asdict()
    with pytest.raises(ValueError):
        Piece(params)


def test_piece_is_correctly_initialized(piece_blueprint):
    p = Piece(piece_blueprint)

    assert p.name == piece_blueprint.name
    assert p.cells == piece_blueprint.spawning_cells
    assert p.id_rotation_cell == piece_blueprint.rotation_cell


@patch("tetris.components.cell.Cell.draw")
def test_piece_can_be_drawn(cell_draw_mocked, piece_blueprint):
    p = Piece(piece_blueprint)

    p.draw(None)

    assert cell_draw_mocked.call_count == 4
