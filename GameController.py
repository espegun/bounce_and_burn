import sys

import pygame
from pygame.locals import *

from GameModel import GameModel
from GameView import GameView
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
        # pygame.display  # This is a module with various methods
        #self.display = pygame.display    # Define the main Window
        self.display = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        #self.display.set_caption("Bounce and burn")
        #pygame.display.set_caption("Bounce and burn")
        
        self.gv = GameView(self.display) 


    def __setup_game_model__(self):

        gm = GameModel()
        ball1 = Ball((255, 0, 0), 10, 100, 100, 5, -5, 1, 1)
        ball2 = Ball((0, 0, 255), 10, 200, 200, -5, 5, 1, 1)
        gm.add_ball(ball1)
        gm.add_ball(ball2)

        return gm

    def run_game(self):

        
        while True:

            # TBD: Get inputs from keys and AI

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # TBD: Update model - with no input so far
            self.gm.update_model(timedelta=1/self.FPS) 
            
            self.gv.draw(self.gm.get_balls())
            pygame.display.update()  # Show everything from the drawn off-screen buffer
            self.fps_clock.tick(self.FPS)




        # if 0:
        #     if keyboard_controls_set is not None:
        #         if keyboard_controls_set == 1:
        #             # Maybe: Use decorators to define (decorated functions) versions of set_acc
        #             # https://www.datacamp.com/community/tutorials/decorators-python

        #             # self.keyboard_controls = {pygame.K_UP: "up", pygame.K_DOWN: "down", pygame.K_RIGHT: "right", pygame.K_LEFT: "left"}
        #             self.keyboard_controls = {pygame.K_UP: "up",
        #                                     pygame.K_DOWN: "down",
        #                                     pygame.K_RIGHT: "right",
        #                                     pygame.K_LEFT: "left"}
        #         elif keyboard_controls_set == 2:
        #             self.keyboard_controls = {}  # TBD
        #         else:
        #             raise ValueError(f"{keyboard_controls_set} is not a value keyboard_controls_set entry.")
        #     else:
        #         self.keyboard_controls = None
