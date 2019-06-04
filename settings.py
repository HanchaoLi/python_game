import os

""" settings of this game"""
class Settings(object):

    def __init__(self):
        # screen settings
        self.SCREEN_WIDTH = 960
        self.SCREEN_HEIGHT = 640
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.BG_COLOR = (100, 100, 100)
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.MAP_DIR = os.path.join(self.BASE_DIR, "python_game/img/game.tmx")


game_settings = Settings()