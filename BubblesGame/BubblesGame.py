import os
import pygame
from Models.GameObject import GameObject
def main():
    pygame.init()
    #print(help(pygame.image.load(os.path.join('src', 'logo.png'))))
    logo = pygame.image.load(
        os.path.join('src', 'logo.png'))
    
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    screen = pygame.display.set_mode((500,480))
    screen.fill(("#FFD26F"))
    
    buble_image = pygame.image.load(
        os.path.join('src', 'soap_buble.png'))
    screen.blit(buble_image, (0,0))
    pygame.display.flip()
    
    running = True
    params = dict(
        {
            'pos':dict(
                {
                    'x':1,
                    'y':2,
                    }),
            'size':dict(
                {
                    'w':30,
                    'h':30,
                    }),
            'speed':120
            }
        )
    go = GameObject(params)
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__ == "__main__":
    main()
