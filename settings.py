import os

""" settings of this game"""
class Settings(object):

    def __init__(self):
        # screen settings
        self.SCREEN_WIDTH = 960
        self.SCREEN_HEIGHT = 640
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.BG_COLOR = (100, 100, 100)



game_settings = Settings()