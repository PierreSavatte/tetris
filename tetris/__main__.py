import time
import logging

import pygame

from tetris.components import Board
from tetris.constants import LOGGER_LEVEL, WINDOW_SIZE, WHITE, BOARD_SIZE
from tetris.exceptions import GameOver

logging.basicConfig(level=LOGGER_LEVEL)

KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    game_board = Board(size=BOARD_SIZE)

    game_continue = True

    while game_continue:
        screen.fill(WHITE)

        events = pygame.event.get(eventtype=pygame.KEYDOWN)
        keys_pressed = [e.key for e in events if e.key in KEYS]

        try:
            game_board.update(keys_pressed)
        except GameOver as e:
            logging.info(f"Game Over:{str(e)}")
            game_continue = False

        game_board.draw(screen)

        pygame.display.flip()
        time.sleep(0.15)
    time.sleep(3)
