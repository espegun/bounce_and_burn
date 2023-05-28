import sys

import pygame
from pygame.locals import *

from GameModel import GameModel
from GameView import GameView
from players import PlayerHuman
from Ball import Ball

class GameController:

    """
    The is intended to be the Controller part of an MVC-pattern.
    """

    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400

    def __init__(self):

        self.gm = self.__setup_game_model__()

        self.FPS = 30  # frames per second setting
        self.fps_clock = pygame.time.Clock()
        
        pygame.init()
        self.display = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        #pygame.display.set_caption("Bounce and burn")
        
        self.gv = GameView(self.display) 


    def __setup_game_model__(self):

        gm = GameModel()
        ball1 = Ball((255, 0, 0), 10, 100, 100, 5, -5, 100, 100)
        ball2 = Ball((0, 0, 255), 10, 200, 200, -5, 5, 100, 100)
        Ball((100, 231, 21), 10, 25, 25 , 1, 1, 100, 100)
        gm.add_ball(ball1)
        gm.add_ball(ball2)
        player1 = PlayerHuman("Player 1", ball1, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)
        gm.add_player(player1)

        return gm

    def run_game(self):
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys_pressed = pygame.key.get_pressed()

            self.gm.update_model(time_delta=1/self.FPS, keys_pressed=keys_pressed) 
            
            self.gv.draw(self.gm.get_balls())
            pygame.display.update()  # Show everything from the drawn off-screen buffer
            self.fps_clock.tick(self.FPS)
