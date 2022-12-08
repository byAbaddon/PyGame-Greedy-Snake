import pygame

from src.settings import *
from src.classes.sound import Sound
from src.classes.fall_effect import FallEffect

effect = FallEffect()


class Snake(pygame.sprite.Sprite, Sound):
    exit_pos = [S_W // 2 - BLOCK_SIZE, 0]
    start_time = pygame.time.get_ticks()
    COOLDOWN = 10
    points = 0
    lives = 3
    level = 14
    # - for reset in current game
    eat_timer = 60
    speed = 6  # FPS
    current_snake_speed = 50
    fruits_counter = 1
    is_eat_fruit = False
    is_penalty = False
    is_level_complete = False
    is_exit = False
    is_pause = False
    is_game_over = False
    is_back_to_game_state = False
    start_x_pos = CELL_NUMBER // 2 - 1
    start_y_pos = CELL_NUMBER // 2 + 3

    def __init__(self, all_spite_groups_dict):
        pygame.sprite.Sprite.__init__(self)
        self.asg = all_spite_groups_dict
        self.image = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (self.start_x_pos * BLOCK_SIZE + 15, self.start_y_pos * BLOCK_SIZE + 15)
        self.pos = vec(self.rect.center)
        self.direction = vec(0, -1)  # Start UP
        self.direction_name = 'up'
        self.body = scale_image('./src/assets/images/snake/body_cross.png', BLOCK_SIZE, BLOCK_SIZE)
        self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.body_list = [vec(self.start_x_pos, self.start_y_pos) for _ in range(5)]

    def check_direction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if not self.is_exit:  # -----------------------prevent keys if level complete
                    Sound.snake_move(self)
                    if event.key == pygame.K_UP and self.direction.y != 1:  # check is not same direction
                        self.direction = vec(0, -1)
                        self.direction_name = 'up'
                    if event.key == pygame.K_DOWN and self.direction.y != -1:
                        self.direction = vec(0, 1)
                        self.direction_name = 'down'
                    if event.key == pygame.K_LEFT and self.direction.x != 1:
                        self.direction = vec(-1, 0)
                        self.direction_name = 'left'
                    if event.key == pygame.K_RIGHT and self.direction.x != -1:
                        self.direction = vec(1, 0)
                        self.direction_name = 'right'
                    if event.key == pygame.K_p:
                        Sound.btn_click(self)
                        self.is_pause = True

    def transform(self):
        self.image = pygame.image.load(f'./src/assets/images/snake/head_{self.direction_name}_s.png')

    def draw(self):
        for i, block in enumerate(self.body_list):
            block_rec = pygame.Rect(block.x * BLOCK_SIZE, block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            # pygame.draw.rect(SCREEN, 'yellow', test_rec)
            if i == 0:  # -------------- draw head
                self.rect.center = [block.x * BLOCK_SIZE + 15, block.y * BLOCK_SIZE + 15]  # new head sprite coordinate
                SCREEN.blit(self.image, block_rec)
            elif i > 0 and i != len(self.body_list) - 1:  # ---------- draw body
                SCREEN.blit(self.body, block_rec)
                pass
            else:  # -------------------- draw queue
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
                SCREEN.blit(self.queue, block_rec)

    def move(self):  # move snake
        copy_body_list = self.body_list[:-1]
        copy_body_list.insert(0, self.body_list[0] + self.direction)
        self.body_list = copy_body_list

        # self.rect.center = (self.body_list[:1][0],self.body_list[:1][1])

    def increase_body_snake(self):  # add element to body snake
        get_last_element_pos = self.body_list[-1]
        # add three new element to queue snake
        number_add_elements = 6
        for _ in range(number_add_elements):
            self.body_list.append(vec(get_last_element_pos))

    def increase_speed_snake(self):  # increase snake speed
        self.speed += 0.4
        self.current_snake_speed += 10

    def check_over_time_eat_fruit(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.start_time > self.COOLDOWN:
            self.start_time = time_now
            self.eat_timer -= 1
        if self.eat_timer <= 0:
            self.eat_timer = 60
            Sound.time_over(self)
            Sound.add_penalty_fruits(self)
            self.fruits_counter += 3
            self.is_penalty = True

    def check_snake_and_fruit_collide(self):
        for sprite in pygame.sprite.spritecollide(self, self.asg['fruit'], True, pygame.sprite.collide_mask):
            if sprite:
                # print(sprite.item_name)
                _, fruit_name, fruit_points = sprite.item_name.split('_')
                if fruit_name == 'rabbit':
                    Sound.snake_eat_rabbit(self)
                elif fruit_name == 'frog':
                    Sound.snake_eat_frog(self)
                else:
                    Sound.snake_eat(self)
                self.points += int(fruit_points)
                self.increase_body_snake()
                self.increase_speed_snake()
                self.fruits_counter -= 1
                self.eat_timer = 60
                self.is_eat_fruit = True

    def check_snake_and_figure_collide(self):
        for sprite in pygame.sprite.spritecollide(self, self.asg['figure'], False, pygame.sprite.collide_mask):
            if sprite:
                print('Crash in figure')
                self.check_is_alive()

    def check_crash_in_body(self):
        for body in self.body_list[1:]:
            body_part = (int(body.x * BLOCK_SIZE + 15), int(body.y * BLOCK_SIZE + 15))
            if self.rect.center == body_part:
                print('Crash in body')
                self.check_is_alive()

    def check_crash_in_wall(self):
        BS = BLOCK_SIZE
        if BS > self.rect.x or self.rect.x > S_W - BS * 2 or self.rect.y > S_H - FRAME_SIZE - BS or self.rect.y < BS:
            if self.fruits_counter == 0 and self.rect.x == self.exit_pos[0] and self.rect.y <= 0:
                self.is_exit = True
                self.level_complete()
            else:
                print('Crash in wall')
                self.check_is_alive()

    def check_is_alive(self):
        Sound.snake_crash(self)
        self.lives -= 1
        table_rect = pygame.Rect(0, 0, S_W, S_H)
        img = pygame.image.load(f'./src/assets/images/frames/full_frame_crash_1.png')
        SCREEN.blit(img, table_rect)

        if self.lives == 0:  # ---------------------- go to Game Over state
            self.is_game_over = True
        else:  # -------------------------------------start_level_again
            self.is_back_to_game_state = True

    def check_level_complete(self):
        if self.fruits_counter == 0:
            self.eat_timer = 60
            self.is_eat_fruit = False
            queue_block_pos = self.body_list[-1]
            if self.rect.y > queue_block_pos.y:
                exit_rect = pygame.Rect(self.exit_pos[0], self.exit_pos[1], BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, 'black', exit_rect)

    def draw_bonus_label(self):
        bonus_img = pygame.image.load('./src/assets/images/frames/bonus_frame.png')
        SCREEN.blit(bonus_img, [S_W // 3, S_H // 3 - 20])
        text_creator('CONGRATULATIONS', 'red', S_W // 3 + 32, S_H // 3 + 26, 32)
        text_creator(f'Level {self.level} - complete', 'yellow', S_W // 3 + 74, S_H // 3 + 55)
        text_creator(f'BONUS - {self.level * 1000}', 'green', S_W // 3 + 90, S_H // 3 + 85)

    def level_complete(self):
        if not self.is_level_complete:
            Sound.stop_all_sounds()
            Sound.level_complete(self)
            Sound.bonus_music(self)
            self.points += self.level * 1000
            self.is_exit = True
            self.is_level_complete = True
        self.draw_bonus_label()
        effect.update()
        text_creator('Press SPACE to continue...', 'white', S_W - 260, S_H - FRAME_SIZE - 15)
        if key_pressed(pygame.K_SPACE):
            self.level += 1
            self.lives += 1
            self.is_back_to_game_state = True

    def reset_current_data(self):
        self.image = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (self.start_x_pos * BLOCK_SIZE + 15, self.start_y_pos * BLOCK_SIZE + 15)
        self.pos = vec(self.rect.center)
        self.direction = vec(0, -1)  # Start UP
        self.direction_name = 'up'
        self.body = scale_image('./src/assets/images/snake/body_cross.png', BLOCK_SIZE, BLOCK_SIZE)
        self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.body_list = [vec(self.start_x_pos, self.start_y_pos) for _ in range(5)]
        self.eat_timer = 60
        self.speed = 6  # FPS
        self.current_snake_speed = 50
        self.fruits_counter = 10
        self.is_eat_fruit = False
        self.is_penalty = False
        self.is_level_complete = False
        self.is_exit = False
        self.is_pause = False
        self.is_back_to_game_state = False

    def reset_all_data(self):  # for new game
        self.image = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (self.start_x_pos * BLOCK_SIZE + 15, self.start_y_pos * BLOCK_SIZE + 15)
        self.pos = vec(self.rect.center)
        self.direction = vec(0, -1)  # Start UP
        self.direction_name = 'up'
        self.body = scale_image('./src/assets/images/snake/body_cross.png', BLOCK_SIZE, BLOCK_SIZE)
        self.queue = scale_image('./src/assets/images/snake/queue_up.png', BLOCK_SIZE, BLOCK_SIZE)
        self.body_list = [vec(self.start_x_pos, self.start_y_pos) for _ in range(5)]
        self.points = 0
        self.lives = 3
        self.level = 1
        self.eat_timer = 60
        self.speed = 6  # FPS
        self.current_snake_speed = 50
        self.fruits_counter = 10
        self.is_eat_fruit = False
        self.is_penalty = False
        self.is_level_complete = False
        self.is_exit = False
        self.is_pause = False
        self.is_back_to_game_state = False
        self.is_game_over = False

    def update(self):
        self.check_direction()
        self.move()
        self.transform()
        self.draw()
        self.check_snake_and_fruit_collide()
        self.check_over_time_eat_fruit()
        self.check_level_complete()
        self.check_snake_and_figure_collide()
        self.check_crash_in_wall()
        self.check_crash_in_body()
        text_creator(f'MousePos: x= {pygame.mouse.get_pos()}', 'white', 300, 15)





