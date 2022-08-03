import pygame

from GameObject import GameObject


class Brick(GameObject):
    def __init__(self, x, y, w, h, color, special_effect=None):
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
        self.special_effect = special_effect

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)