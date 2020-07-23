import pytest

from tetris.components.board import Board
from tetris.components.cell import Cell, CanNotMoveDown


def test_cell_is_init_correctly():
    c = Cell(position=(3, 4))

    assert c.position == (3, 4)


def test_cell_can_move_down():
    b = Board(size=(10, 24))
    c = Cell(position=(3, 4))

    c.move_down(b)

    assert c.position == (3, 5)


def test_cell_can_not_move_down_if_exceed_limit():
    b = Board(size=(10, 24))
    initial_position = (0, 24)
    c = Cell(position=initial_position)

    with pytest.raises(CanNotMoveDown):
        c.move_down(b)

    assert c.position == initial_position


def test_cell_can_not_move_down_if_there_already_is_a_cell():
    b = Board(size=(10, 24), deactivated_cells=[Cell(position=(0, 24))])
    initial_position = (0, 23)
    c = Cell(position=initial_position)

    with pytest.raises(CanNotMoveDown):
        c.move_down(b)

    assert c.position == initial_position
