import pygame.image

from src.settings import *


class Table:
    def __init__(self, snake):
        self.snake_data = snake
        self.image = pygame.image.load('./src/assets/images/frames/full_frame_2.png')
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (2, S_H - FRAME_SIZE + 3)
        self.height_score = 30000

    def draw_display_frame(self):
        table_rect = pygame.Rect(0, 0, S_W, S_H)
        SCREEN.blit(self.image, table_rect)

    def draw_labels_and_table_data(self):
        # label height_score
        text_creator('Top Score', 'white', 40, S_H - 65, 20, None, './src/fonts/mario.ttf')
        if self.snake_data.points >= self.height_score:
            self.height_score = self.snake_data.points
        text_creator(f': {self.height_score}', 'white', 170, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label_score
        text_creator('You Score', 'white', 40, S_H - 35, 20, None, './src/fonts/mario.ttf')
        text_creator(f': {self.snake_data.points}', 'white', 168, S_H - 35, 20, None, './src/fonts/mario.ttf')


        # label snakes left
        text_creator('Snakes:', 'white', 280, S_H - 65, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.lives}', 'white', 374, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # # label snake_speed
        text_creator('Snake Speed:', 'white', 280, S_H - 35, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.current_snake_speed}', 'white', 430, S_H - 35, 20, None, './src/fonts/mario.ttf')

        # label fruits left
        text_creator('Fruits:', 'white', 520, S_H - 65, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.fruits_counter}', 'white', 610, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label time
        text_creator('Time :', 'white', 520, S_H - 35, 20, None, './src/fonts/mario.ttf')
        if self.snake_data.eat_timer > 20:
            text_creator(f'{self.snake_data.eat_timer}', 'white', 596, S_H - 35, 20, None, './src/fonts/mario.ttf')
        else:
            text_creator(f'{self.snake_data.eat_timer}', 'red', 596, S_H - 35, 20, None, './src/fonts/mario.ttf')

        # label level
        text_creator('Level:', 'white', 710, S_H - 65, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{self.snake_data.level}', 'chartreuse4', 786, S_H - 65, 20, None, './src/fonts/mario.ttf')

        # label FPS
        text_creator('FPS:', 'white', 710, S_H - 35, 20, None, './src/fonts/mario.ttf')
        text_creator(f'{ int(CLOCK.get_fps())}', 'white', 760, S_H - 35, 20, None, './src/fonts/mario.ttf')

    def update(self):
        self.draw_display_frame()
        self.draw_labels_and_table_data()





