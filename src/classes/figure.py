from src.settings import *


class Figure(pygame.sprite.Sprite):
    levels_dict = {
        1: (0, 0),
        2: (S_W // 2 - BLOCK_SIZE * 2 + 10, BLOCK_SIZE + 15),
        3: (29, BLOCK_SIZE * 6 - 15),
        4: (S_W // 2 - BLOCK_SIZE * 4 - 20, S_H // 3 - 17 - BLOCK_SIZE * 2),
        5: (S_W // 2, 194),
        6: (S_W // 2 - 2, 196),
        7: (S_W // 2, 194),
        8: (S_W // 2, BLOCK_SIZE * 2 - 1),
        9: (BLOCK_SIZE * 5 - 1, BLOCK_SIZE * 6 - 15),
        10: (S_W // 2 - 15, S_H // 2 - 67),
        11: (S_W // 2, S_H // 2 - 35),
        12: (S_W // 2, S_H // 2 - 67),
        13: (S_W // 2, S_H // 2 - 35),
        14: (S_W // 2 - BLOCK_SIZE, S_H // 2 - 48),
        15: (S_W // 2 - BLOCK_SIZE - 1, BLOCK_SIZE * 6 - 16),

    }

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.level = int(image.split('/')[5].split('_')[1][:-4])
        self.image = pygame.image.load(image)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = self.levels_dict[self.level]


