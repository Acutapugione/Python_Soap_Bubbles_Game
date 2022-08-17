import pygame as pg
from Settings import *
pg.init()

class Dashboard:
    """docstring for Dashboard."""

    def __init__(self,
                 surface:pg.Surface,
                 size:tuple = (WIDTH, HEIGHT)):
        self.__screen = surface
        self.__prepare()
        self.__draw(size)
        pg.display.update()

    def __prepare(self):
        bg_img = pg.image.load(IMAGES_FOLDER+BG_IMAGE)
        bg_img = pg.transform.scale(bg_img,(WIDTH, HEIGHT))

        self.__screen.blit(bg_img, (0,0))

    def __draw(self, size:tuple):
        view = pg.Surface(size).convert_alpha()

        rect = view.get_rect()
        #rect.x += (self.__screen.get_width()-rect.width) // 2
        #rect.y += (self.__screen.get_height()-rect.height) // 2

        self.__screen.blit(view, rect)
