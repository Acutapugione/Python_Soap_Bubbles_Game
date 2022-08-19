import os
import ctypes
import pygame as pg
from PIL import Image
ctypes.windll.user32.SetProcessDPIAware()
SCREEN_SIZE = ctypes.windll.user32.GetSystemMetrics(
    0), ctypes.windll.user32.GetSystemMetrics(1)
# Window
# WIDTH, HEIGHT = SCREEN_SIZE ##Uncomment to fullscreen
WIDTH, HEIGHT = 1200, 600

# Rendering
FPS = 60

# Ball sizing
B_WIDTH = int((WIDTH+HEIGHT)/50)
B_HEIGHT = B_WIDTH

INIT_BUBBLES_CNT = int((WIDTH + HEIGHT)/B_WIDTH)
ACCELERATION_VARIABLES = [
    -2, -1.75, -1.5, -1, -0.5,
    0.5, 1, 1.5, 1.75, 2
]
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND = RED

ROTATION_SPEED = .3
ROTATION_REVERSE = -1
GROWING_STEP = 1

MAIN_FOLDER = os.path.dirname(__file__) 
IMAGES_FOLDER = os.path.join(MAIN_FOLDER, 'img\\')
BUBBLES_FOLDER = os.path.join(MAIN_FOLDER, 'img\\bubble\\')
BG_IMAGE = 'bg_water.jpg'

_image = Image.open(BUBBLES_FOLDER+'bubble_0.png')

BUBBLES_IMG = []


def init_images(start: int = 0, finish: int = 360, step: int = 5) -> None:
    """This func initialize BUBBLES_IMG (list)

    Args:
        start (int, optional): start from degrees. Defaults to 0.
        finish (int, optional): finish on degrees. Defaults to 360.
        step (int, optional): step degrees. Defaults to 5.
    """

    for i in range(0, 360, 5):
        file_path = os.path.join(BUBBLES_FOLDER, f'bubble_{i}.png')
        if not os.path.isfile(file_path):
            img = _image.rotate(i)
            img.save(file_path)
        BUBBLES_IMG.append(pg.image.load(file_path))


init_images()
