import pygame.sprite

from src.settings import *
from src.classes.sound import Sound


class Snake(pygame.sprite.Sprite, Sound):
    is_dead = False
    start_x_pos = CELL_NUMBER // 2
    start_y_pos = CELL_NUMBER // 2 + 4

    def __init__(self, all_spite_groups_dict):
        pygame.sprite.Sprite.__init__(self)
        self.asg = all_spite_groups_dict
        self.image = pygame.image.load('./src/assets/images/snake/head_up.png')
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (self.start_x_pos * BLOCK_SIZE - 16, self.start_y_pos * BLOCK_SIZE - 16)
        self.pos = vec(self.rect.center)
        self.direction = vec(0, 0)  # Start UP
        self.direction_name = 'up'
        self.speed = 5
        self.body = scale_image('./src/assets/images/snake/body_cross.png', BLOCK_SIZE, BLOCK_SIZE)
        self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.body_list = [vec(self.start_x_pos * 2, self.start_y_pos * 2) for _ in range(7)]

    def check_direction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.direction.y != 1:  # check is not same direction
                        self.direction = vec(0, -1)
                        self.direction_name = 'up'
                if event.key == pygame.K_DOWN:
                    if self.direction.y != -1:  # check is not same direction
                        self.direction = vec(0, 1)
                        self.direction_name = 'down'
                if event.key == pygame.K_LEFT:
                    if self.direction.x != 1:  # check is not same direction
                        self.direction = vec(-1, 0)
                        self.direction_name = 'left'
                if event.key == pygame.K_RIGHT:
                    if self.direction.x != -1:  # check is not same direction
                        self.direction = vec(1, 0)
                        self.direction_name = 'right'

    def transform(self):
        self.image = pygame.image.load(f'./src/assets/images/snake/head_{self.direction_name}_2.png')

    def draw(self):
        for i, block in enumerate(self.body_list):
            x_pos = int(block.x * BLOCK_SIZE // 2)
            y_pos = int(block.y * BLOCK_SIZE // 2)
            block_rect = pygame.Rect(x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE)
            if i == 0:  # draw head
                self.rect.x = x_pos
                self.rect.y = y_pos
                SCREEN.blit(self.image, [x_pos, y_pos, 30, 30])
            elif i != len(self.body_list) - 1:  # draw body
                SCREEN.blit(self.body, block_rect)
            else:  # draw queue
                queue_direction = 'up'
                block_before_queue = self.body_list[-2]
                block_queue = self.body_list[-1]
                queue_rel = block_before_queue - block_queue
                if queue_rel == vec(0, 1):
                    queue_direction = 'down'
                elif queue_rel == vec(0, -1):
                    queue_direction = 'up'
                elif queue_rel == vec(-1, 0):
                    queue_direction = 'left'
                elif queue_rel == vec(1, 0):
                    queue_direction = 'right'
                self.queue = pygame.image.load(f'./src/assets/images/snake/queue_{queue_direction}.png')
                SCREEN.blit(self.queue, block_rect)

    def move(self):  # move snake
        copy_body_list = self.body_list[:-1]
        copy_body_list.insert(0, self.body_list[0] + self.direction)
        self.body_list = copy_body_list

        # self.rect.center = (self.body_list[:1][0],self.body_list[:1][1])

    def increase_body_snake(self):  # add element to body snake
        get_last_element_pos = self.body_list[-1]
        # add three new element to queue snake
        number_add_elements = 3
        for _ in range(number_add_elements):
            self.body_list.append(vec(get_last_element_pos))

    def increase_speed_snake(self):  # increase snake speed
        self.speed += 1

    def check_snake_and_fruit_collide(self):
        hits = pygame.sprite.spritecollide(self, self.asg['fruit'], True, pygame.sprite.collide_mask)
        if hits:
            Sound.snake_eat(self)
            # self.asg['fruit'].add(fruit)

    def update(self):
        self.transform()
        self.check_direction()
        self.move()
        self.draw()
        self.check_snake_and_fruit_collide()
        # self.increase_body_snake()
        # self.increase_speed_snake()

#
# class Snake(pygame.sprite.Sprite, Sound):
#     COOLDOWN = 2000  # milliseconds
#     start_timer = pygame.time.get_ticks()
#     is_dead = False
#     start_x_pos = CELL_NUMBER // 2
#     start_y_pos = 14
#
#     def __init__(self, all_spite_groups_dict):
#         pygame.sprite.Sprite.__init__(self)
#         self.asg = all_spite_groups_dict
#         self.image = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE, BLOCK_SIZE)
#         self.rect = self.image.get_bounding_rect(min_alpha=1)
#         self.rect.center = (self.start_x_pos, self.start_y_pos)
#         self.pos = vec(self.rect.center)
#         self.direction = vec(0, -1)  # Start UP
#         self.speed = 2
#         self.body = scale_image('./src/assets/images/snake/body_cross.png', BLOCK_SIZE, BLOCK_SIZE)
#         self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE, BLOCK_SIZE)
#         self.body_list = [vec(self.start_x_pos, self.start_y_pos) for _ in range(5)]
#         self.head = vec(self.start_x_pos, self.start_y_pos)
#         self.head_start_pos = self.body_list[0]
#
#     def check_direction(self):
#         if key_pressed(pygame.K_UP) and self.direction.y != -1:
#             if self.direction.y != 1:  # check is not same direction
#                 self.direction = vec(0, -1)
#                 self.transform('up')
#         if key_pressed(pygame.K_DOWN) and self.direction.y != 1:
#             if self.direction.y != -1:  # check is not same direction
#                 self.direction = vec(0, 1)
#                 self.transform('down')
#         if key_pressed(pygame.K_LEFT) and self.direction.x != -1:
#             if self.direction.x != 1:  # check is not same direction
#                 self.direction = vec(-1, 0)
#                 self.transform('left')
#         if key_pressed(pygame.K_RIGHT) and self.direction.x != 1:
#             if self.direction.x != -1:  # check is not same direction
#                 self.direction = vec(1, 0)
#                 self.transform('right')
#
#     def transform(self, direction):
#         self.image = pygame.image.load(f'./src/assets/images/snake/head_{direction}.png')
#
#     def draw(self):
#         for index in range(len(self.body_list)):
#             x_pos = int(self.body_list[index].x * BLOCK_SIZE)
#             y_pos = int(self.body_list[index].y * BLOCK_SIZE)
#             block_rect = pygame.Rect(x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE)
#             if index == 0:  # draw head
#                 head = self.image
#                 SCREEN.blit(head, block_rect)
#             elif index != len(self.body_list) - 1:  # draw body
#                 SCREEN.blit(self.body, block_rect)
#             else:  # draw queue
#                 queue_direction = 'up'
#                 block_before_queue = self.body_list[-2]
#                 block_queue = self.body_list[-1]
#                 queue_rel = block_before_queue - block_queue
#                 if queue_rel == vec(0, 1):
#                     queue_direction = 'down'
#                 elif queue_rel == vec(0, -1):
#                     queue_direction = 'up'
#                 elif queue_rel == vec(-1, 0):
#                     queue_direction = 'left'
#                 elif queue_rel == vec(1, 0):
#                     queue_direction = 'right'
#                 self.queue = pygame.image.load(f'./src/assets/images/snake/queue_{queue_direction}.png')
#                 SCREEN.blit(self.queue, block_rect)
#
#     def move(self):  # move snake
#         head_snake = self.body_list[0:1]
#         head_x_pos = int(self.direction.x + head_snake[0][0])
#         head_y_pos = int(self.direction.y + head_snake[0][1])
#         self.pos  = vec(head_x_pos, head_y_pos)  # actualize current head position to use in sprite option
#         self.body_list.insert(0, vec(head_x_pos, head_y_pos))
#         self.body_list.pop()
#         self.head = self.body_list[0]  # update position head snake
#
#
#     def increase_body_snake(self):  # add element to body snake
#         get_last_element_pos = self.body_list[-1]
#         # add three new element to queue snake
#         number_add_elements = 3
#         for _ in range(number_add_elements):
#             self.body_list.append(vec(get_last_element_pos))
#
#     def increase_speed_snake(self):  # increase snake speed
#         self.speed += 1
#
#     def check_snake_and_fruit_collide(self):
#         print(self.rect.center)
#         hits = pygame.sprite.groupcollide(self.asg['snake'], self.asg['fruit'], False, True, pygame.sprite.collide_mask)
#         if hits:
#             print(hits)
#
#
#         # fruit_group = [self.asg[gr] for gr in self.asg if gr == 'fruit']
#         # snake_group = [self.asg[gr] for gr in self.asg if gr == 'snake']
#         # print(self, fruit_group)
#         # sprite = pygame.sprite.groupcollide(snake_group, fruit_group, False, pygame.sprite.collide_mask)
#         # for sp in sprite:
#         #     print(sp)
#
#
#
#     def update(self):
#         self.check_direction()
#         self.draw()
#         self.move()
#         self.check_snake_and_fruit_collide()
#         # self.increase_body_snake()
#         # self.increase_speed_snake()
