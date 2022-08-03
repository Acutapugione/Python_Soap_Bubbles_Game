import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    while True:
        screen.fill((192, 192, 192))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()