from src.settings import *


class Figure(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (S_W // 2,  BLOCK_SIZE - 15)
