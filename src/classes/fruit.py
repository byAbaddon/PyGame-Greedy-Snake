import pygame.draw

from src.settings import *


class Fruit(pygame.sprite.Sprite):
    fruits_list = list(sorted(Path('./src/assets/images/fruits/').glob('*.png')))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, )
        self.random_weight_fruit = choices(self.fruits_list, weights=[10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])[0]
        self.item_name = str(self.random_weight_fruit).split('/')[-1][:-4]
        self.image = scale_image(self.random_weight_fruit, BLOCK_SIZE - 1, BLOCK_SIZE - 1).convert_alpha()
        self.rect = self.image.convert_alpha().get_bounding_rect(min_alpha=1)
        self.rect = self.image.get_rect()
        self.x_pos = randint(0, CELL_NUMBER - 1)
        self.y_pos = randint(0, CELL_NUMBER - 10)
        self.fruit_sell_position = [self.x_pos, self.y_pos]
        self.rect.center = (self.x_pos * BLOCK_SIZE + self.image.get_width() // 2,
                            self.y_pos * BLOCK_SIZE + self.image.get_height() // 2)

    # def update(self):
    #     print(self.fruit_sell_position)
    #     fruit_rect = pygame.Rect(self.x_pos * BLOCK_SIZE, self.y_pos * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    #     # pygame.draw.rect(SCREEN, 'red', fruit_rect)
    #     SCREEN.blit(self.image, fruit_rect)
