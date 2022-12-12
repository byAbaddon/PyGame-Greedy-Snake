import pygame
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)


class Sound:
    @staticmethod
    def play_sound(sound_file, volume=0.5, loops=0):
        play = pygame.mixer.Sound(sound_file)
        play.set_volume(volume)
        play.play(loops)

    @staticmethod
    def stop_all_sounds():
        pygame.mixer.stop()

    def btn_click(self):
        self.play_sound('./src/assets/sounds/btn_one.wav')

    # Background
    def intro_music(self):
        self.play_sound('./src/assets/sounds/intro_music.mp3', 0.6, -1)

    def background_music(self):
        self.play_sound('./src/assets/sounds/Background_tango.mp3', 0.6, -1)

    def game_over_music(self):
        self.play_sound('./src/assets/sounds/game_over_music.mp3', 0.6, -1)

    def bonus_music(self):
        self.play_sound('./src/assets/sounds/bonus_music.mp3', 0.8, - 1)

    def add_penalty_fruits(self):
        self.play_sound('./src/assets/sounds/add_penalty_fruits.mp3')

    def time_over(self):
        self.play_sound('./src/assets/sounds/time-over.wav')

    def fruits_finish(self):
        self.play_sound('./src/assets/sounds/fruits_finish.wav')

    def level_complete(self):
        self.play_sound('./src/assets/sounds/level_complete.wav')

    def pistol_gun(self):
        self.play_sound('./src/assets/sounds/pistol_gun.wav', 0.9)

    # ===========================  SNAKE ===========================
    def snake_move(self):
        self.play_sound('./src/assets/sounds/snake_move_one.wav')

    def snake_eat(self):
        self.play_sound('./src/assets/sounds/snake_eat_one.wav')

    def snake_eat_rabbit(self):
        self.play_sound('./src/assets/sounds/snake_eat_bunny.wav')

    def snake_eat_frog(self):
        self.play_sound('./src/assets/sounds/snake_eat_frog.wav')

    def snake_crash(self):
        self.play_sound('./src/assets/sounds/crash.wav')


