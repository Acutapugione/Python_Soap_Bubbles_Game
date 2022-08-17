import pygame as pg
from Settings import *

#bg_img = pg.image.load(IMAGES_FOLDER+BUBBLE_IMAGE)
class Bubble:
    """docstring for Bubble."""

    def __init__(self,
                 init_size: tuple,
                 final_size: tuple,
                 growing_step: int,
                 parent: pg.Surface,
                 pos: tuple)->None:
        self.width, self.height = init_size
        self.g_width, self.g_height = final_size
        self.grow_step = growing_step
        self.parent = parent
        self.image = pg.image.load(IMAGES_FOLDER+BUBBLE_IMAGE)
        self.background = pg.transform.scale(
            self.image,
            (self.width, self.height)
            )
        self.coords = pos

    def move(self, pos: tuple = (0, 0))->None:
        self.coords = pos

    def __resize(self):
        self.background = pg.transform.scale(
            self.image,
            (self.width, self.height)
        )

    def __grow(self):
        """Grow up or down and resize background image"""

        if self.width + self.grow_step < self.g_width:
            self.width+=self.grow_step

        if self.height + self.grow_step < self.g_height:
            self.height+=self.grow_step

        if (
            self.width + self.grow_step<=0
            or self.width + self.grow_step>=self.g_width
            or self.height + self.grow_step<=0
            or self.height + self.grow_step>=self.g_height
            ):
            self.grow_step *= -1
            self.__grow()
        self.__resize()

    def logic(self):
        self.__grow()
        #x, y = self.coords
        #self.move((x+1, y+1))

    def render(self):
        self.parent.blit(self.background, self.coords)
