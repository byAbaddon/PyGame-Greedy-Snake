import pygame.image

from src.settings import *


class Table:
    def __init__(self, snake):
        self.snake_data = snake
        self.image = pygame.image.load('./src/assets/images/frames/full_frame_2.png')
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (2, S_H - FRAME_SIZE + 3)
        self.height_score = 150000

    def draw_display_frame(self):
        table_rect = pygame.Rect(0, 0, S_W, S_H)
        SCREEN.blit(self.image, table_rect)

    def draw_labels_and_table_data(self):
        # label height_score
        text_creator('Top Score', 'crimson', 40, S_H - 65, 20, None, './src/fonts/mario.ttf')
        if self.snake_data.points >= self.height_score:
            self.height_score = self.snake_data.points
        text_creator(f': {self.height_score}', 'crimson', 170, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label_score
        text_creator('You Score', 'cornflowerblue', 40, S_H - 35, 20, None, './src/fonts/mario.ttf')
        text_creator(f': {self.snake_data.points}', 'cornflowerblue', 168, S_H - 35, 20, None, './src/fonts/mario.ttf')


        # label snakes left
        text_creator('Snakes:', 'springgreen4', 280, S_H - 65, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.lives}', 'springgreen4', 374, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # # label snake_speed
        text_creator('Speed:', 'orange', 280, S_H - 35, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.current_snake_speed}', 'orange', 360, S_H - 35, 20, None, './src/fonts/mario.ttf')

        # label fruits left
        text_creator('Fruits:', 'deepskyblue4', 420, S_H - 65, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.fruits_counter}', 'deepskyblue4', 510, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label time
        text_creator('Time :', 'purple', 420, S_H - 35, 20, None, './src/fonts/mario.ttf')
        if self.snake_data.eat_timer > 20:
            text_creator(f'{self.snake_data.eat_timer}', 'white', 496, S_H - 35, 20, None, './src/fonts/mario.ttf')
        else:
            text_creator(f'{self.snake_data.eat_timer}', 'red', 496, S_H - 35, 20, None, './src/fonts/mario.ttf')

        # label FPS
        text_creator('FPS :', 'grey49', 575, S_H - 65, 20, None, './src/fonts/mario.ttf', True)
        text_creator(f'{int(CLOCK.get_fps())}', 'grey49', 635, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label Grid
        text_creator('Grid:', 'coral3', 575, S_H - 35, 20, None, './src/fonts/mario.ttf', True)
        if self.snake_data.is_grid_sys_activated:
            text_creator('on', 'green', 635, S_H - 35, 16, None, './src/fonts/mario.ttf')
        else:
            text_creator('off', 'brown', 635, S_H - 35, 16, None, './src/fonts/mario.ttf')

        # label level
        text_creator('Level:', 'goldenrod4', 700, S_H - 65, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.level}', 'goldenrod4', 776, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label scroll
        text_creator('Scroll:', 'lightskyblue4', 700, S_H - 35, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.scrolling_game}', 'lightskyblue4', 792, S_H - 35, 20, None, './src/fonts/mario.ttf')

    # watch
    def draw_watch(self):
        if self.snake_data.body_list[-1][1] > 0: # check is snake exit from level
            image = pygame.image.load('./src/assets/images/watch/watch.png')
            SCREEN.blit(image,[S_W // 2 - 45, 0])
            if self.snake_data.eat_timer > 20:
                text_creator(f'{self.snake_data.eat_timer}', 'white', S_W // 2 - 28, 15, 22, None, './src/fonts/mario.ttf')
            else:
                text_creator(f'{self.snake_data.eat_timer}', 'red', S_W // 2 - 28, 15, 22, None, './src/fonts/mario.ttf')

    def update(self):
        self.draw_display_frame()
        self.draw_labels_and_table_data()
        self.draw_watch()





