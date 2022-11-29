from src.settings import *
from src.classes.sound import Sound


class Snake(pygame.sprite.Sprite, Sound):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.head = scale_image('./src/assets/images/snake/head_up.png', BLOCK_SIZE - 5, BLOCK_SIZE - 5)
        self.body = scale_image('./src/assets/images/snake/body_rad.png', BLOCK_SIZE - 5, BLOCK_SIZE - 5)
        self.rect = self.head.get_bounding_rect(min_alpha=1)
        self.rect.center = (S_W // 2 + 3, S_H - 292)
        self.pos = vec(self.rect.x, self.rect.y)
        self.direction = vec(0, 0)
        self.speed = 3
        self.body_list = []


    def move(self):
        if key_pressed(pygame.K_UP) and self.direction.y != -1:
            if self.direction.y != 1:  # check is not same direction
                self.direction = Vector2(0, -1)
                self.transform('up')
        if key_pressed(pygame.K_DOWN) and self.direction.y != 1:
            if self.direction.y != -1:  # check is not same direction
                self.direction = Vector2(0, +1)
                self.transform('down')
        if key_pressed(pygame.K_LEFT) and self.direction.x != -1:
            if self.direction.x != 1:  # check is not same direction
                self.direction = Vector2(-1, 0)
                self.transform('left')
        if key_pressed(pygame.K_RIGHT) and self.direction.x != 1:
            if self.direction.x != -1:  # check is not same direction
                self.direction = Vector2(+1, 0)
                self.transform('right')

        if self.direction.y == -1:
            self.rect.y -= self.speed
        if self.direction.y == 1:
            self.rect.y += self.speed
        if self.direction.x == -1:
            self.rect.x -= self.speed
        if self.direction.x == 1:
            self.rect.x += self.speed

    def transform(self, direction):
        self.head = pygame.image.load(f'./src/assets/images/snake/head_{direction}.png')

    def update(self):
        self.move()

