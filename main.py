from src.settings import *
from src.classes.sound import Sound


# Game State
class GameState(Sound):
    COOLDOWN = 2000  # milliseconds
    start_timer = pygame.time.get_ticks()

    def __init__(self,):
        self.state = 'intro'
        self.current_music = ''
        self.is_music_play = False
        self.background = None
        self.is_bg_created = False

    def game(self):
        pass

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


# ============= Starting Game loop
while True:
    SCREEN.fill(pygame.Color('black'))
    game_state.state_manager()
    pygame.display.update()
    CLOCK.tick(FPS)
    exit_game()
