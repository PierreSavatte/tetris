from unittest.mock import patch

import pytest

from tetris.components.board import Board
from tetris.components.cell import Cell, CanNotMove
from tetris.constants import RECT_SIZE


def test_cell_is_init_correctly():
    c = Cell(position=(3, 4), color=(0, 0, 0))

    assert c.position == (3, 4)
    assert c.color == (0, 0, 0)


def test_cell_can_move(direction):
    b = Board(size=(10, 24))
    c = Cell(position=(3, 4), color=(0, 0, 0))

    old_position = c.position
    c.move(b, direction)

    assert c.position == (
        old_position[0] + direction[0],
        old_position[1] + direction[1],
    )


def test_cell_can_not_move_if_exceed_limit(direction):
    b = Board(size=(10, 24))
    direction_x, direction_y = direction
    if direction_x:
        potential_values_of_x = {1: 9, -1: 0}
        initial_position = (potential_values_of_x[direction_x], 0)
    else:
        potential_values_of_y = {1: 23, -1: 0}
        initial_position = (0, potential_values_of_y[direction_y])
    c = Cell(position=initial_position, color=(0, 0, 0))

    with pytest.raises(CanNotMove):
        c.move(b, direction)

    assert c.position == initial_position


def test_cell_can_not_move_if_there_already_is_a_cell(direction):
    b = Board(
        size=(10, 24),
        deactivated_cells=[Cell(position=(4, 4), color=(0, 0, 0))],
    )
    direction_x, direction_y = direction
    potential_values = {1: 3, -1: 5, 0: 4}
    initial_position = (
        potential_values[direction_x],
        potential_values[direction_y],
    )
    c = Cell(position=initial_position, color=(0, 0, 0))

    with pytest.raises(CanNotMove):
        c.move(b, direction)

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
    "position, direction, can_actually_move",
    [
        ((0, 23), (0, 1), False),  # Can not go further the bottom limit
        ((0, 0), (0, -1), False),  # Can not go further the top limit
        ((0, 0), (-1, 0), False),  # Can not go further the left limit
        ((0, 23), (0, 1), False),  # Can not go further the right limit
        ((0, 22), (0, 1), False),  # There already a cell here
        ((0, 0), (0, 1), True),
    ],
)
def test_cell_says_if_can_move(position, direction, can_actually_move):
    b = Board(
        size=(10, 24),
        deactivated_cells=[Cell(position=(0, 23), color=(0, 0, 0))],
    )
    c = Cell(position=position, color=(0, 0, 0))

    assert c.can_move(b, direction) is can_actually_move
