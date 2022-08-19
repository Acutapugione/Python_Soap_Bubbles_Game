import pygame as pg
from settings import *


class Bubble:
    """docstring for Bubble."""

    def __init__(self,
                 init_size: tuple,
                 final_size: tuple,
                 growing_step: int,
                 parent: pg.Surface,
                 pos: tuple,
                 speed: tuple = (.5, .5),
                 img_num: int = 0) -> None:
        """Initialize an Bubble obj

        Args:
            init_size (tuple): starting size (width, height)
            final_size (tuple): finishing size (width, height)
            growing_step (int): step in growing process
            parent (pg.Surface): surface to render in
            pos (tuple): statring position (x, y)
            speed (tuple, optional): starting speed (dx, dy). Defaults to (.5, .5).
            img_num (int, optional): number of image in BUBBLES_IMG. Defaults to 0.
        """

        self.width, self.height = init_size
        self.g_width, self.g_height = final_size
        self.speed = speed
        self.grow_step = growing_step
        self.parent = parent
        self.coords = pos
        self.collision_happend = False

        self.__rotation = ROTATION_SPEED
        self.__img_num = img_num

        self.__init_img()
        self.__resize()

    def __init_img(self):
        self.__img_num = self.__img_num % len(BUBBLES_IMG)
        self.image = BUBBLES_IMG[int(self.__img_num)]

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, angle):
        self.__rotation = angle

    def __move(self, pos: tuple = (0, 0)) -> None:
        dx, dy = self.speed
        x, y = self.coords
        x += dx
        y += dy
        self.coords = (x, y)
        if (pos is not None and pos != (0, 0)):  # or pos == (0, 0):
            self.coords = pos

    def __rotate(self):
        if self.__img_num >= len(BUBBLES_IMG)-1:
            self.rotation *= -1
        self.__img_num += self.rotation
        self.__img_num = self.__img_num % len(BUBBLES_IMG)
        self.image = BUBBLES_IMG[int(self.__img_num)]

    def __resize(self):
        self.view = pg.transform.scale(
            self.image,
            (self.width, self.height)
        )

    def __grow(self):

        if self.width + self.grow_step < self.g_width:
            self.width += self.grow_step

        if self.height + self.grow_step < self.g_height:
            self.height += self.grow_step

        if (
            self.width + self.grow_step <= 0
            or self.width + self.grow_step >= self.g_width
            or self.height + self.grow_step <= 0
            or self.height + self.grow_step >= self.g_height
        ):
            self.grow_step *= -1
            #self.rotation *= -1

        self.__resize()

    def logic(self):
        """Doing some logic"""

        if self.collision_happend == False:
            self.__move()
        else:
            self.rotation *= -1
            #self.grow_step = 0
            #self.collision_handled = True
        # self.__move()

    def render(self):
        """Doing some render actions
        """
        self.__grow()
        self.__rotate()
        self.parent.blit(self.view, self.coords)
