import pytest

from tetris.components.board import Board
from tetris.components.cell import Cell


def test_board_is_init_correctly():
    deactivated_cells = [Cell((0, 24)), Cell((1, 24)), Cell((2, 24))]

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
        deactivated_cells=[Cell((0, 24)), Cell((1, 24)), Cell((2, 24))],
    )

    assert b.get_positions_of_deactivated_cells() == [
        (0, 24),
        (1, 24),
        (2, 24),
    ]
