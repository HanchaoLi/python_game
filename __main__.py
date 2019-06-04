import pygame
import sys

def game_looper():
    pygame.init()
    game_screen = pygame.display.set_mode((960, 640))
    background_color = (30, 100, 30)
    game_screen.fill(background_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    game_looper()