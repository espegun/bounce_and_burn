import sys

import pygame

class GameView:

    WHITE = (255, 255, 255)

    def __init__(self, surface):    

        self.surface = surface  # The surface where the game will be drawn      

    def draw(self, draw_these: list):

        self.surface.fill(GameView.WHITE)

        for draw_this in draw_these:
            draw_this.draw_on_surface(self.surface)
