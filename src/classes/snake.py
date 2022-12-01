from src.settings import *
from src.classes.sound import Sound


class Snake(pygame.sprite.Sprite, Sound):
    COOLDOWN = 2000  # milliseconds
    start_timer = pygame.time.get_ticks()
    is_dead = False
    start_x_pos = CELL_NUMBER // 2
    start_y_pos = 14

    def __init__(self, all_spite_groups_dict):
        pygame.sprite.Sprite.__init__(self, )
        self.asg = all_spite_groups_dict
        self.image = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (self.start_x_pos, self.start_y_pos)
        self.pos = vec(self.rect.center)
        self.direction = vec(0, -1)  # Start UP
        self.speed = 5
        self.body = scale_image('./src/assets/images/snake/body_cross.png', BLOCK_SIZE, BLOCK_SIZE)
        self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.body_list = [vec(self.start_x_pos, self.start_y_pos) for _ in range(5)]
        self.head = vec(self.start_x_pos, self.start_y_pos)
        self.head_start_pos = self.body_list[0]

    def check_direction(self):
        if key_pressed(pygame.K_UP) and self.direction.y != -1:
            if self.direction.y != 1:  # check is not same direction
                self.direction = vec(0, -1)
                self.transform('up')
        if key_pressed(pygame.K_DOWN) and self.direction.y != 1:
            if self.direction.y != -1:  # check is not same direction
                self.direction = vec(0, 1)
                self.transform('down')
        if key_pressed(pygame.K_LEFT) and self.direction.x != -1:
            if self.direction.x != 1:  # check is not same direction
                self.direction = vec(-1, 0)
                self.transform('left')
        if key_pressed(pygame.K_RIGHT) and self.direction.x != 1:
            if self.direction.x != -1:  # check is not same direction
                self.direction = vec(1, 0)
                self.transform('right')

    def transform(self, direction):
        self.image = pygame.image.load(f'./src/assets/images/snake/head_{direction}.png')

    def draw(self):
        for index in range(len(self.body_list)):
            x_pos = int(self.body_list[index].x * BLOCK_SIZE)
            y_pos = int(self.body_list[index].y * BLOCK_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE)
            if index == 0:  # draw head
                head = self.image
                SCREEN.blit(head, block_rect)
            elif index != len(self.body_list) - 1:  # draw body
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
        head_snake = self.body_list[0:1]
        head_y_pos = int(self.direction.y + head_snake[0][1])
        head_x_pos = int(self.direction.x + head_snake[0][0])
        self.body_list.insert(0, vec(head_x_pos, head_y_pos))
        self.body_list.pop()
        self.head = self.body_list[0]  # update position head snake
        self.pos = self.head  # actualize current head position to use in sprite option

    def increase_body_snake(self):  # add element to body snake
        get_last_element_pos = self.body_list[-1]
        # add three new element to queue snake
        number_add_elements = 3
        for _ in range(number_add_elements):
            self.body_list.append(vec(get_last_element_pos))

    def increase_speed_snake(self):  # increase snake speed
        self.speed += 1

    def check_snake_and_fruit_collide(self):
        pass


    def update(self):
        self.check_direction()
        self.draw()
        self.move()
        # self.increase_body_snake()
        # self.increase_speed_snake()





#
# class Snake(pygame.sprite.Sprite, Sound):
#     is_dead = False
#     COOLDOWN = 2000  # milliseconds
#     start_timer = pygame.time.get_ticks()
#
#     def __init__(self, all_spite_groups_dict):
#         pygame.sprite.Sprite.__init__(self)
#         # self.asg = all_spite_groups_dict
#         self.image = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE - 5, BLOCK_SIZE- 5)
#         self.rect = self.image.get_bounding_rect(min_alpha=1)
#         self.rect.center = (S_W // 2, S_H - 200)
#         self.pos = vec(self.rect.x, self.rect.y)
#         self.direction = vec(0, 0)
#         self.speed = 3
#         self.body = scale_image('./src/assets/images/snake/body_rad.png', BLOCK_SIZE - 5, BLOCK_SIZE -5)
#         self.body_rect = self.image.get_bounding_rect(min_alpha=1)
#         self.body_rect.center = (S_W // 2, S_H - 200 + BLOCK_SIZE)
#         self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE - 5, BLOCK_SIZE - 5)
#         self.queue_rect = self.image.get_bounding_rect(min_alpha=1)
#
#         self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
#
#         self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
#         self.body_list = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE) for _ in range(4)]
#
#         self.bb_list = [(self.body_rect.x, self.body_rect.y + BLOCK_SIZE * i) for i in range(3)]
#
#     def move(self):
#         if key_pressed(pygame.K_UP) and self.direction.y != -1:
#             if self.direction.y != 1:  # check is not same direction
#                 self.direction = Vector2(0, -1)
#                 self.transform('up')
#         if key_pressed(pygame.K_DOWN) and self.direction.y != 1:
#             if self.direction.y != -1:  # check is not same direction
#                 self.direction = Vector2(0, 1)
#                 self.transform('down')
#         if key_pressed(pygame.K_LEFT) and self.direction.x != -1:
#             if self.direction.x != 1:  # check is not same direction
#                 self.direction = Vector2(-1, 0)
#                 self.transform('left')
#         if key_pressed(pygame.K_RIGHT) and self.direction.x != 1:
#             if self.direction.x != -1:  # check is not same direction
#                 self.direction = Vector2(1, 0)
#                 self.transform('right')
#
#         if self.direction.y == -1:
#             self.rect.y -= self.speed
#             self.body_rect.y -= self.speed
#         if self.direction.y == 1:
#             self.rect.y += self.speed
#             self.body_rect.y += self.speed
#         if self.direction.x == -1:
#             self.rect.x -= self.speed
#             self.body_rect.x -= self.speed
#         if self.direction.x == 1:
#             self.rect.x += self.speed
#             self.body_rect.x += self.speed
#
#         self.bb_list = [(self.body_rect.x, self.body_rect.y + BLOCK_SIZE * i) for i in range(3)]
#
#
#     def transform(self, direction):
#         self.image = pygame.image.load(f'./src/assets/images/snake/head_{direction}.png')
#         self.queue = pygame.image.load(f'./src/assets/images/snake/queue_{direction}.png')
#
#     def draw(self):
#         # draw static parts of body in start position
#         for i in range(len(self.bb_list)):
#             SCREEN.blit(self.body, self.bb_list[i])
#
#         self.bb_list.append(self.rect)
#         for i in range(len(self.bb_list) - 1):  #_ _ _ .
#             print(self.bb_list[i])
#             self.bb_list[i] = self.bb_list[i + 1]
#         self.bb_list.pop()
#         print('-------------------------------')
#
#
#
#         # draw part of body
#         for i in range(len(self.body_list)):
#             SCREEN.blit(self.body, self.body_list[i])
#             # pygame.draw.rect(SCREEN, 'green', self.body_list[i])
#
#         # pygame.draw.rect(SCREEN, 'red', self.head)
#
#         # SCREEN.blit(self.image, (self.head.x, self.head.y))
#         # self.body_list.append(self.head)
#         # for i in range(len(self.body_list) - 1):
#         #     if i == 0:
#         #         SCREEN.blit(self.queue, self.body_list[i])
#         #     self.body_list[i].x = self.body_list[i + 1].x
#         #     self.body_list[i].y = self.body_list[i + 1].y
#         # self.head.x += self.direction.x * BLOCK_SIZE
#         # self.head.y += self.direction.y * BLOCK_SIZE
#         # self.body_list.remove(self.head)
#
#
#     def update(self):
#         self.move()
#         self.draw()
#
#
#
#
#
#
#
#
#
#
#
#
