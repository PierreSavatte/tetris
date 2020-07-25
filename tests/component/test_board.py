from unittest.mock import patch

import pytest

from tetris.components.board import Board
from tetris.components.cell import Cell
from tetris.components.piece import Piece, PieceBlueprints


def test_board_is_init_correctly():
    deactivated_cells = [
        Cell((0, 24), color=(0, 0, 0)),
        Cell((1, 24), color=(0, 0, 0)),
        Cell((2, 24), color=(0, 0, 0)),
    ]

    b = Board(size=(10, 24), deactivated_cells=deactivated_cells)

    assert b.size == (10, 24)
    assert b.active_piece is None
    assert b.deactivated_cells == deactivated_cells


@pytest.mark.parametrize(
    "position_to_test, result",
    [
        ((10, 24), True),
        ((11, 24), False),
        ((10, 25), False),
        ((0, 0), True),
        ((-1, 0), False),
        ((0, -1), False),
    ],
)
def test_board_says_if_position_is_inside_its_limits(position_to_test, result):
    b = Board(size=(10, 24))

    assert b.position_is_inside(position_to_test) is result


def test_board_gives_positions_of_deactivated_cells():
    b = Board(
        size=(10, 24),
        deactivated_cells=[
            Cell((0, 24), color=(0, 0, 0)),
            Cell((1, 24), color=(0, 0, 0)),
            Cell((2, 24), color=(0, 0, 0)),
        ],
    )

    assert b.get_positions_of_deactivated_cells() == [
        (0, 24),
        (1, 24),
        (2, 24),
    ]


@patch("tetris.components.cell.Cell.draw")
@patch("tetris.components.piece.Piece.draw")
@patch("pygame.draw.rect")
def test_piece_can_be_drawn(
    draw_rect_mocked, piece_draw_mocked, cell_draw_mocked
):
    b = Board(
        size=(10, 24),
        deactivated_cells=[
            Cell((0, 24), color=(0, 0, 0)),
            Cell((1, 24), color=(0, 0, 0)),
            Cell((2, 24), color=(0, 0, 0)),
        ],
    )
    b.active_piece = Piece(PieceBlueprints.get_random())

    b.draw(None)

    piece_draw_mocked.assert_called_once()
    assert cell_draw_mocked.call_count == 3
    assert draw_rect_mocked.call_count == b.size[0] * b.size[1]
