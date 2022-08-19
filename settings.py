import os
import ctypes
from PIL import Image
ctypes.windll.user32.SetProcessDPIAware()
SCREEN_SIZE = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
# Window
#WIDTH, HEIGHT = SCREEN_SIZE ##Uncomment to fullscreen
WIDTH, HEIGHT = 1200, 600

# Rendering
FPS = 10

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

ROTATION_SPEED = 6

MAIN_FOLDER = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(MAIN_FOLDER, 'img\\')
BUBBLES_FOLDER = os.path.join(MAIN_FOLDER, 'img\\bubble\\')
BG_IMAGE = 'bg_water.jpg'

_image = Image.open(BUBBLES_FOLDER+'bubble_0.png')
need = False
BUBBLES_IMG = ['bubble_0.png']
for i in range(1, 360):
    img = _image.rotate(i)
    if need:
        img.save(f'{BUBBLES_FOLDER}bubble_{i}.png')
    BUBBLES_IMG.append(f'bubble_{i}.png')

BUBBLE_IMAGE = 'soap-bubbles_1.png'
