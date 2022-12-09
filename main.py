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

    def __init__(self,):
        self.state = 'intro'
        self.current_music = ''
        self.is_music_play = False
        self.background = None
        self.is_bg_created = False
        self.reset_all_data_for_new_game = False

    def game(self):

        if self.reset_all_data_for_new_game:
            self.current_music = ''
            self.is_music_play = False
            self.background = None
            self.is_bg_created = False
            self.reset_all_data_for_new_game = False
            self.start_game_counter = 3  # restore start counter
            snake.reset_all_data()
            [all_spite_groups_dict[group].empty() for group in all_spite_groups_dict]
            all_spite_groups_dict['snake'].add(snake)
            if snake.level > 15:
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
            self.state = 'game_over'

        # # =================================================== UPDATE
        Grid.draw_grid(self)
        table.update()

        # #  --------------------------- draw sprite group
        snake_group.draw(SCREEN)
        figure_group.draw(SCREEN)
        fruit_group.draw(SCREEN)
        #
        # # # # --------------------------- update sprite group
        snake_group.update()
        fruit_group.update()

    def intro(self):
        background_image('./src/assets/images/backgrounds/bg.png')
        text_creator('GREEDY SNAKE', 'green4', 40, 60, 80, None, './src/fonts/candy.ttf')
        text_creator('Start game - SPACE', 'beige', S_W // 4, S_H - 20, 30,None, './src/fonts/mario.ttf' )
        text_creator('Credits - C', 'fuchsia', S_W // 3, S_H - 100, 30, None, './src/fonts/mario.ttf')
        text_creator('Menu - M', 'red', S_W // 3, S_H - 60, 30, None, './src/fonts/mario.ttf')
        text_creator('By Abaddon', 'orange', 10, S_H - 10, 15, None, './src/fonts/mario.ttf')
        text_creator('Copyright ©2023', 'brown', S_W - 150, S_H - 10, 15, None, './src/fonts/mario.ttf')

        if key_pressed(pygame.K_SPACE):
            Sound.btn_click(self)
            self.start_game_counter = 3
            self.state = 'get_ready'
        if key_pressed(pygame.K_c):
            Sound.btn_click(self)
            self.state = 'credits'
        if key_pressed(pygame.K_m):
            Sound.btn_click(self)
            self.state = 'menu'
        exit_game()

    def menu(self):
        background_image('./src/assets/images/backgrounds/bg_menu.png')
        text_creator('Press RETURN to back...', 'cornsilk', S_W - 200, S_H - 10, 24)
        if key_pressed(pygame.K_RETURN):
            self.state = 'intro'
        exit_game()

    def credits(self):
        # background_image('./src/assets/images/backgrounds/bg_EMPTY.png')
        text_creator('CREDITS', 'slateblue3', S_W // 2 - 60, 40, 40, None, None, True)
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

        if key_pressed(pygame.K_RETURN):
            Sound.btn_click(self)
            self.state = 'intro'
        exit_game()

    def get_ready(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.start_timer > self.COOLDOWN:
            self.start_game_counter -= 1
            self.start_timer = time_now
        background_image('./src/assets/images/backgrounds/bg_snake.png')
        text_creator(f'START AFTER: {self.start_game_counter}', 'black', 260, S_H // 2, 50)
        # text_creator('Press RETURN to continue...', 'bisque', S_W - 280, S_H - FRAME_SIZE - 10)
        if self.start_game_counter == 0:
            if snake.lives == 0:
                self.reset_all_data_for_new_game = True
            self.state = 'game'
        exit_game()

    def start_pause(self):
        background_image('./src/assets/images/backgrounds/bg_pause.png')
        text_creator('PAUSE', 'chartreuse4', S_W - 360, S_H - FRAME_SIZE - 250, 50)
        text_creator('Press RETURN to continue...', 'bisque', S_W - 280, S_H - FRAME_SIZE - 10)

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
        if key_pressed(pygame.K_RETURN):
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

# ================================================================ create top Table for: score , energy and more

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
# ============= Starting Game loop
while True:
    SCREEN.fill(pygame.Color('black'))
    game_state.state_manager()
    pygame.display.update()
    CLOCK.tick(snake.speed)
