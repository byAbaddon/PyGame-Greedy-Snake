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
        self.play_sound('./src/assets/sounds/buttons/click.wav')

    # Background
    def intro_music(self):
        self.play_sound('./src/assets/sounds/game_musics/intro.mp3')

    def background_music(self):
        self.play_sound('./src/assets/sounds/Background_tango.mp3', 0.6, -1)

    # ===========================  SNAKE ===========================
    def snake_move(self):
        self.play_sound('./src/assets/sounds/snake_move_one.wav')

    def snake_eat(self):
        self.play_sound('./src/assets/sounds/snake_eat_one.wav')

