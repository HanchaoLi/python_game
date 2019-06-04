import pygame
from pytmx.util_pygame import load_pygame
from game_funcs import draw_background_with_tiled_map
from settings import game_settings


def game_loop():
    game_exit = False
    pygame.init()
    pygame.display.set_caption('Python Game')
    game_screen = pygame.display.set_mode(
        game_settings.SCREEN_SIZE,
    )
    game_map = load_pygame(game_settings.MAP_DIR)
    draw_background_with_tiled_map(game_screen, game_map)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        pygame.display.update()

game_loop()