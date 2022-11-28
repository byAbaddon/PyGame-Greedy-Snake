from src.settings import *


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ''
        self.direction = vec((0, 0))
        self.speed = 5
