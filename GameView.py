import sys

import pygame

class GameView:

    WHITE = (255, 255, 255)
    #BLUE = (0, 0, 255)

    def __init__(self, surface):    

        self.surface = surface  # The surface where the game will be drawn      

    def draw(self, draw_these: list):

        self.surface.fill(GameView.WHITE)

        for draw_this in draw_these:
            draw_this.draw_on_surface(self.surface)

        # while True:  # the main game loop

        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()

        #     # Get actions from keys preseed (human players)
        #     keys_pressed = pygame.key.get_pressed()
        #     for b in [b for b in game.get_balls() if b.is_human()]:
        #         if first:
        #             print(b)
        #             print(keys_pressed)
        #         b.feed_keys_pressed(keys_pressed)

        #     # Get actions (AI players)
        #     # TBD

        #     # Update the balls based on deliberate actions taken
        #     for ball in game.get_balls():
        #         #ball.update_pos(1 / FPS)
        #         ball.full_update(1 / FPS)

        #     # Update the ball based on interactions and physics
        #     # TBD


