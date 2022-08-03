import pygame

from GameObject import GameObject


class Ball(GameObject):
    def __init__(self, x, y, r, color, speed):
        params = dict(
        {
            'pos':dict(
                {
                    'x':x - r,
                    'y':y - r,
                    }),
            'size':dict(
                {
                    'w':r * 2,
                    'h':r * 2,
                    }),
            'speed':speed
            }
        )
        GameObject.__init__(self,params)
        self.radius = r
        self.diameter = r * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, 
                           self.color, 
                           self.center, 
                           self.radius)