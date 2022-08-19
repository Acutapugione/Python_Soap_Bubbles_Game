import pygame
import random

from game.bubble import Bubble
from game.bubble_handler import BubbleHandler
from settings import *

pygame.init()


class Game:
	def __init__(self,
				 width: int, height: int, title: str,
				 bg: pygame.Surface = (140, 80, 55),
				 fps: int = FPS) -> None:
		self.bubbles=[]
		self.width = width
		self.height = height
		self.win = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)

		self.clock = pygame.time.Clock()
		self.running = True
		self.FPS = fps
		self.background = bg

	def start(self):
		for i in range(1, 5):
			self.bubbles.append(
				Bubble(
					(0, 0),
					(B_WIDTH, B_HEIGHT),
					2,
					self.win,
					(random.randrange(0, WIDTH),random.randrange(0, HEIGHT))
				)
			)

	def logic(self):
		for bubble in self.bubbles:
			bubble.logic()
		self.__handle_collision()

	def __handle_collision(self):
		for bubble in self.bubbles:
			for n_bubble in self.bubbles:
				if bubble != n_bubble:
					BubbleHandler.handle_collision(bubble,n_bubble)

	def render(self, window):

		if self.background is tuple:
			self.win.fill(self.background)
		else:
			self.win.blit(self.background, (0,0))

		for bubble in self.bubbles:
			try:
				bubble.render()
			except Exception as e:
				pass


		pygame.display.update()
