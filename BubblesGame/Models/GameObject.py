from pygame.rect import Rect

class GameObject:
    def __init__(self, params:dict) -> None:
        x = params.get('pos').get('x')                   
        y = params.get('pos').get('y')  

        w = params.get('size').get('w')
        h = params.get('size').get('h')

        self.bounds = Rect(x, y, w, h)
        self.speed = params.get('speed')

    @property
    def left(self):
        return self.bounds.left

    @property
    def right(self):
        return self.bounds.right

    @property
    def top(self):
        return self.bounds.top

    @property
    def bottom(self):
        return self.bounds.bottom

    @property
    def width(self):
        return self.bounds.width
    
    @property
    def height(self):
        return self.bounds.height

    @property
    def center(self):
        return self.bounds.center

    @property
    def centerx(self):
        return self.bounds.centerx

    @property
    def centery(self):
        return self.bounds.centery

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        self.bounds = self.bounds.move(dx, dy)

    def update(self):
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)