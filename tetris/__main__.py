import time

import pygame

from tetris.components import Board
from .constants import WINDOW_SIZE, WHITE, BOARD_SIZE

KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    game_board = Board(size=BOARD_SIZE)

    while True:
        screen.fill(WHITE)

        events = pygame.event.get(eventtype=pygame.KEYDOWN)
        keys_pressed = [e.key for e in events if e.key in KEYS]

        game_board.update(keys_pressed)
        game_board.draw(screen)

        pygame.display.flip()
        time.sleep(0.15)
