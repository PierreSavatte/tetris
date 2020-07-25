from dotenv import load_dotenv
from smart_getenv import getenv

load_dotenv()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (
    getenv("WINDOW_WIDTH", type=int, default=650),
    getenv("WINDOW_HEIGHT", type=int, default=850),
)
RECT_SIZE = getenv("RECT_SIZE", type=int, default=33)

BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = (
    getenv("BOARD_WIDTH", type=int, default=10),
    getenv("BOARD_HEIGHT", type=int, default=24),
)

FPS = getenv("FPS", type=int, default=60)
