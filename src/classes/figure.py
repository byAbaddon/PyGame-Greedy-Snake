from src.settings import *


class Figure(pygame.sprite.Sprite):
    levels_dict = {
        1: (0, 0),
        2: (S_W // 2 - BLOCK_SIZE * 2 + 10, BLOCK_SIZE + 15),
        3: (S_W // 2 - BLOCK_SIZE * 4 - 20, S_H // 3 - 17 - BLOCK_SIZE * 2),
        4: (S_W // 2 - 2, 196),
        5: (S_W // 2, 194),
        6: (S_W // 2, 194),

    }

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.level = int(image.split('/')[5][-5:-4])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = self.levels_dict[self.level]


