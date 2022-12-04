import pygame.sprite

from src.settings import *
from src.classes.sound import Sound
from src.classes.snake import Snake
from src.classes.fruit import Fruit
from src.classes.grid import Grid
from src.classes.figure import Figure

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
#
# # add to group
snake_group.add(snake)
fruit_group.add(fruit)

# ==================================================================


# Game State
class GameState(Sound):
    COOLDOWN = 2000  # milliseconds
    start_timer = pygame.time.get_ticks()

    def __init__(self,):
        self.state = 'game'
        self.current_music = ''
        self.is_music_play = False
        self.background = None
        self.is_bg_created = False

    def game(self):
        text_creator(f'FPS: {int(CLOCK.get_fps())}', 'brown3', 250, 20, 22)
        # ++++++++++++++++++++++++++++++ developer utils +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        text_creator(f'FPS {int(CLOCK.get_fps())}', 'white', 10, 5, 25)
        text_creator(f'Direction: x= {int(snake.direction.x)} y= {int(snake.direction.y)}', 'white', 90, 15, 22)
        text_creator(f'Pos: x= {int(snake.pos.x)} y= {int(snake.pos.y)}', 'white', 86, 33, 22)
        text_creator(f'MousePos: x= {pygame.mouse.get_pos()}', 'white', 490, 5)

        if not self.is_bg_created:
            pass
            # Sound.background_music(self)
            figure_group.add(Figure('./src/assets/images/figures/level_2.png'))
            self.is_bg_created = True

        if snake.is_eat_fruit:
            fruit_group.add(Fruit(all_spite_groups_dict, snake))
            snake.is_eat_fruit = False

        # # =================================================== UPDATE
        Grid.draw_grid(self)

        # #  --------------------------- draw sprite group
        snake_group.draw(SCREEN)
        figure_group.draw(SCREEN)
        fruit_group.draw(SCREEN)
        #
        # # # # --------------------------- update sprite group
        snake_group.update()
        fruit_group.update()

    def intro(self):
        pass

    def menu(self):
        pass

    def start_pause(self):
        pass

    # ========================================= state manager ...
    def state_manager(self):
        # print(self.state)
        if self.state == 'game':
            self.game()
        if self.state == 'intro':
            self.intro()
        if self.state == 'menu':
            self.menu()
        if self.state == 'pause':
            self.start_pause()


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
