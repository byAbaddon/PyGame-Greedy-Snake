import pygame.image

from src.settings import *


class Table:
    def __init__(self, snake, fruit):
        self.snake_data = snake
        self.fruit_data = fruit
        self.image = pygame.image.load('./src/assets/images/frames/frame.png')
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (2, S_H - FRAME_SIZE + 3)
        self.height_score = 30000

    def draw_display_frame(self):
        table_rect = pygame.Rect(0, 0, S_W, S_H)
        SCREEN.blit(pygame.image.load('./src/assets/images/frames/full_frame_2.png'), table_rect)

    def draw_labels_and_table_data(self):
        # label height_score
        text_creator('Height Score:', 'chartreuse4', 40, S_H - 65)
        if self.snake_data.points >= self.height_score:
            self.height_score = self.snake_data.points
        text_creator(f'{self.height_score}', 'chartreuse4', 164, S_H - 65)

        # label_score
        text_creator('Current Score:', 'chartreuse4', 40, S_H - 35)
        text_creator(f'{self.snake_data.points}', 'chartreuse4', 166, S_H - 35)

        # label snakes left
        text_creator('Snakes:', 'chartreuse4', 280, S_H - 65)
        text_creator(f'{self.snake_data.lives}', 'chartreuse4', 350, S_H - 65)

        # # label snake_speed
        text_creator('Snake Speed:', 'chartreuse4', 280, S_H - 35)
        text_creator(f'{self.snake_data.current_snake_speed}', 'chartreuse4', 400, S_H - 35)

        # label fruits left
        text_creator('Fruits:', 'chartreuse4', 520, S_H - 65)
        text_creator(f'{self.snake_data.fruits_counter}', 'chartreuse4', 580, S_H - 65)

        # label time
        text_creator('Time:', 'chartreuse4', 520, S_H - 35)
        text_creator(f'{self.snake_data.eat_timer}', 'chartreuse4', 580, S_H - 35)

        # label level
        text_creator('Level:', 'chartreuse4', 720, S_H - 65)
        text_creator(f'{self.snake_data.level}', 'chartreuse4', 780, S_H - 65)

        # label FPS
        text_creator('FPS:', 'chartreuse4', 720, S_H - 35)
        text_creator(f'{ int(CLOCK.get_fps())}', 'chartreuse4', 780, S_H - 35)

    def update(self):
        self.draw_display_frame()
        self.draw_labels_and_table_data()





