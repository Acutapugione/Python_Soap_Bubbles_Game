import pygame
import random
from Settings import *


class Speed():
    def __init__(self, xA:float = 0, yA:float = 0) -> None:
        self.__xA = xA
        self.__yA = yA

    @property
    def xA(self)->float:
        return self.__xA
    @xA.setter
    def xA(self, xA:float = 0)->None:
        self.__xA = xA

    @property
    def yA(self)->float:
        return self.__yA
    @yA.setter
    def yA(self, yA:float)->None:
        self.__yA = yA

    def reverce(self):
        self.__yA , self.__xA =  -self.__yA, -self.__xA

def getRandomSpeed() -> Speed:
    return Speed( random.choice(ACCELERATION_VARIABLES), random.choice(ACCELERATION_VARIABLES) )

def getRandomWindowPoint(width:float, height:float) -> tuple((float, float)):
    return ( random.randint(width, WIDTH - width), random.randint(height, HEIGHT - height))

class Player(pygame.sprite.Sprite):
    def __init__(self, image:pygame.image) -> None:
        super().__init__()
        self.image = image
        self.image.set_colorkey(WHITE)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = getRandomWindowPoint(self.width, self.height)
        #self.rect.bottom = HEIGHT - 10
        self.__speed = getRandomSpeed()
        #width = image.get_rect().width
        #height = image.get_rect().height

    @property
    def width(self)->float:
        return self.rect.width
    @width.setter
    def width(self, width:float)->None:
        self.rect.width = width
        
    @property
    def height(self)->float:
        return self.rect.height
    @height.setter
    def height(self, height:float)->None:
        self.rect.height = height

    @property
    def speed(self)->Speed:
        return self.__speed

    @speed.setter
    def speed(self, speed:Speed)->None:
        self.speed.yA = speed.yA
        self.speed.xA = speed.xA

    @property 
    def left(self)->float:
        return self.rect.left
    
    @left.setter
    def left(self, x:float)->None:
        self.rect.left = x

    @property 
    def right(self)->float:
        return self.rect.right

    @right.setter
    def right(self, x:float)->None:
        self.rect.right = x

    @property 
    def top(self)->float:
        return self.rect.top

    @top.setter
    def top(self, y:float)->None:
        self.rect.top = y

    @property 
    def bottom(self)->float:
        return self.rect.bottom

    @bottom.setter
    def bottom(self, y:float)->None:
        self.rect.bottom = y

    def update(self)->None:
        self.rect.x += self.__speed.xA
        self.rect.y += self.__speed.yA

        if self.right > WIDTH:
            self.speed.xA = -self.speed.xA
        if self.left <= 0:
            self.speed.xA = -self.speed.xA
        if self.top <= 0:
            self.speed.yA = -self.speed.yA
        if self.bottom > HEIGHT:
            self.speed.yA = -self.speed.yA
