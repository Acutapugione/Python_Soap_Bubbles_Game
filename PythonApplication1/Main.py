
# Pygame scaffold
from importlib.machinery import all_suffixes
import sys
from xml.sax.handler import all_properties
import pygame
import random


from Settings import *
from Resources import *
from Player import Player, Speed


def is_collision(pos:tuple or Player, player:Player)->bool:
    if isinstance(pos, Player):#np.linalg.norm( np.array([b1.x,b1.y]) - np.array([b2.x,b2.y]) ) < (b1.size + b2.size)
        return(
           pos.rect.x <= player.right 
           and pos.rect.x >= player.left
           and pos.rect.y >= player.top
           and pos.rect.y <= player.bottom
           and pos != player
           )
    else:
        x, y = pos
        return(
           x <= player.right 
           and x >= player.left
           and y >= player.top
           and y <= player.bottom
           )
    
def getImg(
    path:str = IMAGES_FOLDER,
    src:str = 'bubble.png',
    size:dict = dict({'width': B_WIDTH,'height': B_HEIGHT})
    ):
    
    image = pygame.image.load(os.path.join(path, src))

    width = size.get('width')
    height = size.get('height')
    if (
        width is not None 
        and height is not None
        ):
        if (
            width>0 
            and height>0
            ):
            image = pygame.transform.smoothscale(
                image, 
                (int(width), int(height))
                ) 
    return image

def generateBubbles(sprites):
    for i in range(INIT_BUBBLES_CNT):
        resize = random.randint(int(B_WIDTH/1.5), int(B_WIDTH*1.5))
        sprites.add(Player(getImg(IMAGES_FOLDER, 'bubble.png',  dict({'width': resize,'height': resize}))))

def main():
    # Create game & window
    pygame.init()
    pygame.mixer.init()
    #screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)  ##Uncomment to fullscreen
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    bg = getImg(IMAGES_FOLDER, 'bg_water.jpg',  dict({'width': WIDTH,'height': HEIGHT}))
    screen.blit(bg, (0, 0))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    # Groupping all sprites
    all_sprites = pygame.sprite.Group() 
    generateBubbles(all_sprites)
    # Main loop
    running = True
    while running:
        screen.blit(bg, (0, 0))
        # Frames per second
        clock.tick(FPS)
        
        # Events loop
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                for item in all_sprites:
                    if is_collision(pygame.mouse.get_pos(), item) and isinstance(item, Player):
                        all_sprites.remove(item)
            
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
            #for item in all_sprites:
            #    if isinstance(item, Player):
            #        if keystate[pygame.K_LEFT]:
            #            item.speed.xA += -1
            #        if keystate[pygame.K_RIGHT]:
            #            item.speed.xA +=  1
            #        if keystate[pygame.K_UP]:
            #            item.speed.yA +=  -1 
            #        if keystate[pygame.K_DOWN]:
            #            item.speed.yA +=  1
            if event.type == pygame.KEYDOWN:
                for item in all_sprites:
                    if isinstance(item, Player):
                        if event.key == pygame.K_LEFT:
                            item.speed.xA += -1
                        if event.key == pygame.K_RIGHT:
                            item.speed.xA +=  1
                        if event.key == pygame.K_UP:
                            item.speed.yA +=  -1 
                        if event.key == pygame.K_DOWN:
                            item.speed.yA +=  1
        for item1 in all_sprites:
            for item in all_sprites:
                if is_collision(item1, item) and isinstance(item, Player):
                    all_sprites.remove(item)
                    all_sprites.remove(item1)
                
        if len(all_sprites) == 0:
            del all_sprites
            all_sprites = pygame.sprite.Group() 
            generateBubbles(all_sprites)
            
        # Updating
        all_sprites.update()
        # Rendering
        #screen.fill(bg)
        
        all_sprites.draw(screen)

        # Process after rendering, flipping the window
        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(int(main() or 0))