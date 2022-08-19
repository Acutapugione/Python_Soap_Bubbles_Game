import pygame as pg
from settings import *
from game.main import Game


def main():
	bg_img = pg.image.load(IMAGES_FOLDER+BG_IMAGE)
	bg_img = pg.transform.scale(bg_img,(WIDTH, HEIGHT))

	game = Game(WIDTH, HEIGHT, "Bubbles the game", bg_img)
	game.start()

	while game.running:
		game.clock.tick(game.FPS)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				game.running = False

		game.logic()
		game.render(game.win)


if __name__ == "__main__":
	main()
	pg.quit()
	quit()
