import sys

import pygame
from pygame.locals import *

from GameModel import GameModel
from Ball import Ball

class GameController:

    """
    The is intended to be the Controller part of an MVC-pattern.
    """


    def __init__(self)

        self.gm = self.__setup_game_model__()

    def __setup_game_model__(self):

        gm = GameModel()
        ball1 = Ball(10, 100, 100, )



        return gm




    def init_default_game():

        game = Game()
        game.add_ball(Ball("human", "Red", 10, 100, 100, (255, 0, 0), 1))
        game.add_ball(Ball("passive", "Blue", 10, 200, 100, (0, 0, 255)))
        for ball in game.get_balls():
            ball.set_speed(-10, 10)

        return game


    game = init_default_game()



    def run_game(self):

        pass
        pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Bounce and burn")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


print(pygame.K_RIGHT)

first = True

while True:  # the main game loop

    surface.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Get actions from keys preseed (human players)
    keys_pressed = pygame.key.get_pressed()
    for b in [b for b in game.get_balls() if b.is_human()]:
        if first:
            print(b)
            print(keys_pressed)
        b.feed_keys_pressed(keys_pressed)

    # Get actions (AI players)
    # TBD

    # Update the balls based on deliberate actions taken
    for ball in game.get_balls():
        #ball.update_pos(1 / FPS)
        ball.full_update(1 / FPS)

    # Update the ball based on interactions and physics
    # TBD

    for b in game.get_balls():
        pos = b.get_pos()
        pygame.draw.circle(
            surface,
            b.get_color(),
            (round(pos["x"]), round(pos["y"])),
            b.get_radius(),
            0,
        )

    pygame.display.update()
    fpsClock.tick(FPS)

    first = False










    if 0:
        if keyboard_controls_set is not None:
            if keyboard_controls_set == 1:
                # Maybe: Use decorators to define (decorated functions) versions of set_acc
                # https://www.datacamp.com/community/tutorials/decorators-python

                # self.keyboard_controls = {pygame.K_UP: "up", pygame.K_DOWN: "down", pygame.K_RIGHT: "right", pygame.K_LEFT: "left"}
                self.keyboard_controls = {pygame.K_UP: "up",
                                          pygame.K_DOWN: "down",
                                          pygame.K_RIGHT: "right",
                                          pygame.K_LEFT: "left"}
            elif keyboard_controls_set == 2:
                self.keyboard_controls = {}  # TBD
            else:
                raise ValueError(f"{keyboard_controls_set} is not a value keyboard_controls_set entry.")
        else:
            self.keyboard_controls = None









