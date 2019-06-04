import pygame
import sys

from settings import Settings

game_settings = Settings()
def game_looper():
    game_exit = False

    pygame.init()
    pygame.display.set_caption('Heros!')
    game_screen = pygame.display.set_mode(
        game_settings.SCREEN_SIZE,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        game_screen.fill(game_settings.BG_COLOR)
        pygame.display.update()

if __name__ == '__main__':
    game_looper()