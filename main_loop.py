import sys

import pygame
from pygame.locals import *

from Game import Game
from Ball import Ball


def init_default_game():
    game = Game()
    game.add_Ball(Ball("human", "Red", 10, 100, 100, (255, 0, 0), 1))
    game.add_Ball(Ball("passive", "Blue", 10, 200, 100, (0, 0, 255)))
    for b in game.get_Balls():
        b.set_speed(-10, 10)

    return game


print("Welcome to the amazinglicious game!")
game = init_default_game()

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Bounce and burn")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


print(pygame.K_RIGHT)

while True:  # the main game loop

    surface.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()
    for b in [b for b in game.get_Balls() if b.is_human()]:
        b.feed_keys_pressed(keys_pressed)

    # Check for AI events
    # TBD at some later stage

    for b in game.get_Balls():
        b.update_pos(1 / FPS)

    for b in game.get_Balls():
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

print("That was fun.")
