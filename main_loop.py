import pygame, sys
from pygame.locals import *

from Game import Game
from Ball import Ball

print("Welcome to the amazinglicious game!")

game = Game()
game.add_Ball(Ball("human", "Red", 10, 100, 100, (255, 0, 0), "Not none"))
game.add_Ball(Ball("passive", "Blue", 10, 200, 100, (0, 0, 255)))
for b in game.get_Balls():
    b.set_speed(-10, 10)

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Bounce and burn")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

while True:  # the main game loop

    surface.fill(WHITE)

    #if direction == 'right':
    #    catx += 5


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Check if the game event (e.g. a key pressed) matches a relevant human key
        for b in [b for b in game.get_Balls() if b.is_human()]:
            b.feed_event(event)

    # Check for AI events
    # TBD at some later stage


    for b in game.get_Balls():
        b.update_pos(1/FPS)

    for b in game.get_Balls():
        pos = b.get_pos()
        pygame.draw.circle(surface, b.get_color(), (round(pos["x"]), round(pos["y"])), b.get_radius(), 0)

    pygame.display.update()
    fpsClock.tick(FPS)

print("That was fun.")