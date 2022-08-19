import pygame as pg
from settings import *

#bg_img = pg.image.load(IMAGES_FOLDER+BUBBLE_IMAGE)
class Bubble:
    """docstring for Bubble."""

    def __init__(self,
                 init_size: tuple,
                 final_size: tuple,
                 growing_step: int,
                 parent: pg.Surface,
                 pos: tuple,
                 img_num:int = 0)->None:
        self.width, self.height = init_size
        self.g_width, self.g_height = final_size
        self.grow_step = growing_step
        self.parent = parent
        self.image = pg.image.load(BUBBLES_FOLDER+BUBBLES_IMG[img_num])

        self.background = pg.transform.scale(
            self.image,
            (self.width, self.height)
            )

        self.coords = pos
        self.collision_handled = False
        self.__img_num = img_num
        self.__rotation = ROTATION_SPEED

    @property
    def rotation(self):
        return self.__rotation
    @rotation.setter
    def rotation(self, angle):
        self.__rotation = angle

    def move(self, pos: tuple = (0, 0))->None:
        self.coords = pos

    def __rotate(self):
        self.__img_num += self.rotation
        self.__img_num =  self.__img_num % len(BUBBLES_IMG)
        #print( int(self.__img_num) )
        self.image = pg.image.load(BUBBLES_FOLDER+BUBBLES_IMG[ int(self.__img_num) ])

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
            #self.grow_step *= -1
            pass

        self.__resize()

    def logic(self):
        pass
        #self.rotation+=1
        #self.__rotate()

        #x, y = self.coords
        #self.move((x+1, y+1))

    def render(self):

        self.__grow()
        self.__rotate()
        self.parent.blit(self.background, self.coords)
