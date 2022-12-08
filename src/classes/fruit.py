import pygame.draw

from src.settings import *


class Fruit(pygame.sprite.Sprite):
    fruits_list = list(sorted(Path('./src/assets/images/fruits/').glob('*.png')))

    def __init__(self, all_spite_groups_dict, snake):
        pygame.sprite.Sprite.__init__(self,)
        self.asg = all_spite_groups_dict
        self.snake_data = snake
        self.random_weight_fruit = self.check_is_penalty()
        self.item_name = str(self.random_weight_fruit).split('/')[-1][:-4]
        self.image = scale_image(self.random_weight_fruit, BLOCK_SIZE - 2, BLOCK_SIZE - 2).convert_alpha()
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.x_pos = randint(1, CELL_NUMBER - 2)  # 0, 1
        self.y_pos = randint(1, CELL_NUMBER - 12)  # 0, 11
        self.fruit_sell_position = [self.x_pos, self.y_pos]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos * BLOCK_SIZE + self.image.get_width() // 2,
                            self.y_pos * BLOCK_SIZE + self.image.get_height() // 2)

    def check_is_penalty(self):
        if self.snake_data.is_penalty:
            self.random_weight_fruit = './src/assets/images/penalty/zeroPoints_frog_0.png'
        else:
            self.random_weight_fruit = choices(self.fruits_list, weights=[10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])[0]
        return self.random_weight_fruit

    def check_fruit_and_snake_body_collide(self):
        for part in self.snake_data.body_list[1:]:
            if part == self.fruit_sell_position:
                fruit_group = self.asg['fruit']
                fruit_group.empty()
                fruit_group.add(Fruit(self.asg, self.snake_data))
                break

    def check_fruit_and_figure_collide(self):
        fruit_group = self.asg['fruit']
        figure_group = self.asg['figure']
        sprite = pygame.sprite.groupcollide(fruit_group, figure_group, True, False, pygame.sprite.collide_mask)
        if sprite:
            fruit_group.empty()
            fruit_group.add(Fruit(self.asg, self.snake_data))

    def update(self):
        self.check_fruit_and_snake_body_collide()
        self.check_fruit_and_figure_collide()


