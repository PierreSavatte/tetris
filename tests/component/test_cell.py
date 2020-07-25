from unittest.mock import patch

import pytest

from tetris.components.board import Board
from tetris.components.cell import Cell, CanNotMoveDown
from tetris.constants import RECT_SIZE


def test_cell_is_init_correctly():
    c = Cell(position=(3, 4), color=(0, 0, 0))

    assert c.position == (3, 4)
    assert c.color == (0, 0, 0)


def test_cell_can_move_down():
    b = Board(size=(10, 24))
    c = Cell(position=(3, 4), color=(0, 0, 0))

    c.move_down(b)

    assert c.position == (3, 5)


def test_cell_can_not_move_down_if_exceed_limit():
    b = Board(size=(10, 24))
    initial_position = (0, 24)
    c = Cell(position=initial_position, color=(0, 0, 0))

    with pytest.raises(CanNotMoveDown):
        c.move_down(b)

    assert c.position == initial_position


def test_cell_can_not_move_down_if_there_already_is_a_cell():
    b = Board(
        size=(10, 24),
        deactivated_cells=[Cell(position=(0, 24), color=(0, 0, 0))],
    )
    initial_position = (0, 23)
    c = Cell(position=initial_position, color=(0, 0, 0))

    with pytest.raises(CanNotMoveDown):
        c.move_down(b)

    assert c.position == initial_position


@patch("pygame.draw.rect")
def test_cell_can_be_printed(draw_rect_mocked):
    color = (0, 0, 0)
    c = Cell(position=(5, 10), color=color)
    screen = None

    c.draw(screen=screen)

    draw_rect_mocked.assert_called_once_with(
        screen, color, (5 * RECT_SIZE, 10 * RECT_SIZE, RECT_SIZE, RECT_SIZE)
    )


@pytest.mark.parametrize(
    "position, can_move_down",
    [((0, 23), False), ((0, 24), False), ((0, 0), True)],
)
def test_cell_says_if_can_move_down(position, can_move_down):
    b = Board(
        size=(10, 24),
        deactivated_cells=[Cell(position=(0, 24), color=(0, 0, 0))],
    )
    c = Cell(position=position, color=(0, 0, 0))

    assert c.can_move_down(b) is can_move_down
