import pygame.sprite

from src.settings import *
from src.classes.sound import Sound
from src.classes.snake import Snake
from src.classes.fruit import Fruit
from src.classes.grid import Grid
from src.classes.figure import Figure
from src.classes.table import Table

# ======================================================================== create Sprite groups
snake_group = pygame.sprite.Group()
fruit_group = pygame.sprite.Group()
figure_group = pygame.sprite.Group()
#
# # add to all_sprite_groups
all_spite_groups_dict = {'snake': snake_group, 'fruit': fruit_group, 'figure': figure_group}
#
# # ======================================================================= initialize  Classes
#
snake = Snake(all_spite_groups_dict)
fruit = Fruit(all_spite_groups_dict, snake)
#
# # add to group
snake_group.add(snake)


# ==================================================================
table = Table(snake)


# Game State
class GameState(Sound):
    COOLDOWN = 1000  # milliseconds
    start_timer = pygame.time.get_ticks()
    start_game_counter = 3
    radius = 2
    cord_x = S_W // 2 - 110
    cord_y = S_W // 3 - 6
    cord_x_aye = S_W // 2 - 110
    aye_counter = 0

    def __init__(self,):
        self.state = 'intro'
        self.is_music_play = False
        self.background = None
        self.is_bg_created = False
        self.reset_all_data_for_new_game = False
        self.is_grid_system = False

    def game(self):
        if self.reset_all_data_for_new_game:
            self.is_music_play = False
            self.background = None
            self.is_bg_created = False
            self.reset_all_data_for_new_game = False
            self.start_game_counter = 3  # restore start counter
            snake.reset_all_data()
            [all_spite_groups_dict[group].empty() for group in all_spite_groups_dict]
            all_spite_groups_dict['snake'].add(snake)
            if snake.level > 15:
                snake.scrolling_game += 1
                snake.level = 1
            all_spite_groups_dict['figure'].add(Figure(f'./src/assets/images/figures/level_{snake.level}.png'))

        if snake.is_back_to_game_state:
            Sound.stop_all_sounds()
            pygame.time.delay(1500)
            fruit_group.empty()  # ================
            snake.reset_current_data()  # reset current snake data
            self.start_game_counter = 3  # restore start counter
            self.is_bg_created = False
            self.state = 'get_ready'
            return

        if not self.is_bg_created:
            Sound.background_music(self)
            figure_group.empty()
            figure_group.add(Figure(f'./src/assets/images/figures/level_{snake.level}.png'))
            new_fruit = Fruit(all_spite_groups_dict, snake)
            fruit_group.add(new_fruit)
            self.is_bg_created = True

        if snake.is_eat_fruit and not len(fruit_group):
            fruit_group.add(Fruit(all_spite_groups_dict, snake))
            snake.is_eat_fruit = False

        if snake.is_pause:
            snake.is_pause = False
            self.state = 'pause'

        if snake.is_game_over:
            Sound.stop_all_sounds()
            pygame.time.delay(1500)
            Sound.pistol_gun(self)
            Sound.game_over_music(self)
            self.state = 'game_over'

        # --------------------------  switch on/of to Grid system
        if check_key_pressed(pygame.K_g):
            if not self.is_grid_system:
                self.is_grid_system = True
            else:
                self.is_grid_system = False

        # # =================================================== UPDATE
        if self.is_grid_system:
            Grid.draw_grid(self)
        table.update()

        # #  --------------------------- draw sprite group
        fruit_group.draw(SCREEN)
        snake_group.draw(SCREEN)
        figure_group.draw(SCREEN)

        # # --------------------------- update sprite group
        fruit_group.update()
        snake_group.update()

    def intro(self):
        if not self.is_music_play:
            Sound.intro_music(self)
            self.is_music_play = True
        background_image('./src/assets/images/backgrounds/bg_1.png')
        text_creator('GREEDY SNAKE', 'green4', 40, 60, 80, None, './src/fonts/candy.ttf')
        # text_creator('Menu - M', 'red', 50, S_H - 64, 27, None, './src/fonts/mario.ttf')
        text_creator('Menu - M', 'orangered3', S_W - 230, S_H - 160, 27, None, './src/fonts/mario.ttf')
        text_creator('Credits - C', 'fuchsia', S_W - 230, S_H - 110, 29, None, './src/fonts/mario.ttf')
        text_creator('Start game - SPACE', 'beige', S_W // 4 - 6, S_H - 24, 32, None, './src/fonts/mario.ttf')
        text_creator('By Abaddon', 'orange', 10, S_H - 10, 15, None, './src/fonts/mario.ttf')
        text_creator('Copyright ©2023', 'teal', S_W - 150, S_H - 10, 15, None, './src/fonts/mario.ttf')

        if check_key_pressed(pygame.K_SPACE):
            Sound.btn_click(self)
            self.start_game_counter = 3
            Sound.stop_all_sounds()
            self.state = 'get_ready'
        if check_key_pressed(pygame.K_c):
            Sound.btn_click(self)
            self.state = 'credits'
        if check_key_pressed(pygame.K_m):
            Sound.btn_click(self)
            self.state = 'menu'
        exit_game()

    def menu(self):
        background_image('./src/assets/images/backgrounds/bg_menu.png')
        text_creator('Press RETURN to back...', 'cornsilk', S_W - 200, S_H - 10, 24)
        if check_key_pressed(pygame.K_RETURN):
            self.state = 'intro'
        exit_game()

    def credits(self):
        # background_image('./src/assets/images/backgrounds/bg_EMPTY.png')
        text_creator('CREDITS', 'slateblue3', S_W // 2 - 100, 40, 36, None, './src/fonts/born.ttf', True)
        text_creator('version: 1.0.0-beta', 'cornsilk', S_W - 130, 20, 20)

        text_creator('Free images:', 'brown', 110, 100, 35)
        text_creator('https://www.pngwing.com', 'cadetblue4', 130, 125, 30)

        text_creator('Free sounds:', 'brown', 110, 200, 35)
        text_creator('https://freesound.org/', 'cadetblue4', 130, 225, 30)

        text_creator('Platform 2D game:', 'brown', 110, S_H // 2, 34)
        text_creator('https://www.pygame.org', 'cadetblue4', 130, S_H // 2 + 24, 30)

        SCREEN.blit(pygame.image.load('./src/assets/images/title/pygame_logo.png'), (S_W // 4 - 50, S_H - 266))

        text_creator('Developer:', 'brown', 30, S_H - 60, 30)
        text_creator('by Abaddon', 'cadetblue4', 50, S_H - 40, 30)

        text_creator('Bug rapports:', 'brown', S_W // 2 - 90, S_H - 60, 30)
        text_creator('subtotal@abv.bg', 'cadetblue4', S_W // 2 - 70, S_H - 40, 30)

        text_creator('Copyright:', 'brown', S_W - 140, S_H - 60, 30)
        text_creator('© 2023', 'cadetblue4', S_W - 120, S_H - 40, 30)

        text_creator('Press RETURN to back...', 'cornsilk', S_W - 200, S_H - 10, 24)

        if check_key_pressed(pygame.K_RETURN):
            Sound.btn_click(self)
            self.state = 'intro'
        exit_game()

    def get_ready(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.start_timer > self.COOLDOWN:
            self.start_game_counter -= 1
            self.start_timer = time_now
        background_image('./src/assets/images/backgrounds/bg.png', 20, -100)
        text_creator('By Abaddon', 'orange', 10, S_H - 10, 15, None, './src/fonts/mario.ttf')
        text_creator('Copyright ©2023', 'brown', S_W - 150, S_H - 10, 15, None, './src/fonts/mario.ttf')
        text_creator(f'START AFTER: {self.start_game_counter}', 'purple', 260, S_H - 50, 40,
                     None, './src/fonts/mario.ttf')
        if self.start_game_counter == 0:
            if snake.lives == 0:
                self.reset_all_data_for_new_game = True
            self.state = 'game'
        exit_game()

    def start_pause(self):
        background_image('./src/assets/images/backgrounds/bg_pause_2.png')
        text_creator('PAUSE', 'red3', S_W // 2, S_H  // 2 - 30, 80, None, './src/fonts/born.ttf')
        text_creator('Press RETURN to continue...', 'bisque', S_W - 280, S_H - 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                Sound.btn_click(self)
                if event.key == pygame.K_RETURN:
                    self.state = 'game'

    def game_over(self):
        background_image('./src/assets/images/backgrounds/bg_game_over.png')
        text_creator('Press RETURN to back...', 'cornsilk', S_W - 200, S_H - 10, 24)

        text_creator('You reached :', 'goldenrod4', 10, 24, 28, None, './src/fonts/born.ttf', True)
        text_creator(f'Points: {snake.points}', 'brown', 30, 90, 25, None, './src/fonts/mario.ttf')
        text_creator(f'Level: {snake.level}','springgreen4', 30, 140, 25, None, './src/fonts/mario.ttf')
        text_creator(f'Scrolling : {snake.scrolling_game}', 'wheat', 30, 190, 25, None, './src/fonts/mario.ttf')
        # --------------- statistics
        text_creator('Statistics :', 'goldenrod4', S_W - 280, 21, 28, None, './src/fonts/born.ttf', True)
        sort_by_values = sorted(snake.statistics_dict.items(), key=lambda v: -v[1])

        for i in range(len(sort_by_values)):
            fruit, count = sort_by_values[i]
            image = scale_image(f'src/assets/images/fruits/fruits_pic/{fruit}.png', 28, 28)
            if i < 4:
                SCREEN.blit(image, [S_W - 280 , 50 + i * 45])
                text_creator(f'- {count}', 'white', S_W - 245, 70 + i * 43)
            elif i < 8:
                i -= 4
                SCREEN.blit(image, [S_W - 190, 50 + i * 45])
                text_creator(f'- {count}', 'white', S_W - 155, 70 + i * 43)
            else:
                i -= 8
                SCREEN.blit(image, [S_W - 100, 50 + i * 45])
                text_creator(f'- {count}', 'white', S_W - 65, 70 + i * 43)



        time_now = pygame.time.get_ticks()
        if time_now - self.start_timer > self.COOLDOWN - 500:
            self.start_timer = time_now
            if self.radius < 4:
                self.radius += 1
            else:
                self.cord_y += 10
                if self.cord_y > S_H // 2:
                    self.cord_y = S_W // 3 - 6
            # move aye
            self.aye_counter += 1
            if self.aye_counter < 4:
                self.cord_x_aye -= 1
            else:
                if self.aye_counter < 7:
                    self.cord_x_aye += 1
                else:
                    self.aye_counter = 0

        # draw circle
        pygame.draw.circle(SCREEN, 'red', (S_W // 2 - 107, S_W // 3 - 6), self.radius)
        # draw rect
        pygame.draw.rect(SCREEN, 'red', (self.cord_x, self.cord_y, 2, 4))

        # draw circle ayes
        pygame.draw.circle(SCREEN, 'white', (self.cord_x_aye + 168, S_W // 3 + 8), 4)
        pygame.draw.circle(SCREEN, 'white', (self.cord_x_aye + 194, S_W // 3 + 8), 4)
        pygame.draw.circle(SCREEN, 'blue', (self.cord_x_aye + 168, S_W // 3 + 8), 3)
        pygame.draw.circle(SCREEN, 'blue', (self.cord_x_aye + 194, S_W // 3 + 8), 3)

        if key_pressed(pygame.K_RETURN):
            Sound.stop_all_sounds()
            Sound.intro_music(self)
            self.reset_all_data_for_new_game = True
            self.state = 'intro'
        exit_game()

    # ========================================= state manager ...
    def state_manager(self):
        # print(self.state)
        if self.state == 'intro':
            self.intro()
        if self.state == 'game':
            self.game()
        if self.state == 'get_ready':
            self.get_ready()
        if self.state == 'menu':
            self.menu()
        if self.state == 'credits':
            self.credits()
        if self.state == 'pause':
            self.start_pause()
        if self.state == 'game_over':
            self.game_over()


#  ================================ create new GameState
game_state = GameState()

# SCREEN_UPDATE = pygame.USEREVENT
# pygame.time.set_timer(SCREEN_UPDATE, 150)

# ============= Starting Game loop
while True:
    SCREEN.fill(pygame.Color('black'))
    game_state.state_manager()
    pygame.display.update()
    CLOCK.tick(snake.speed)
