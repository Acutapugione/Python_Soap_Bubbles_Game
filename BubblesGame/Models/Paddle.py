import pygame

import config as c
from GameObject import GameObject


class Paddle(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        params = dict(
        {
            'pos':dict(
                {
                    'x':x,
                    'y':y,
                    }),
            'size':dict(
                {
                    'w':w,
                    'h':h,
                    }),
            'speed':0
            }
        )
        GameObject.__init__(self, params)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def update(self):
        if self.moving_left:
            dx = -(min(self.offset, self.left))
        elif self.moving_right:
            dx = min(self.offset, c.screen_width - self.right)
        else:
            return

        self.move(dx, 0)