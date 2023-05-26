from Ball import Ball
from players import Player

class GameModel():

    """
    The is intended to be the Model part of an MVC-pattern.
    """

    def __init__(self):

        self.players = []
        self.balls = []

    def add_ball(self, ball):

        assert isinstance(ball, Ball)
        self.balls.append(ball)

    def get_balls(self):

        return self.balls

    def add_player(self, player):

        assert isinstance(player, Player)
        self.players.append(player)

    def get_players(self):

        return self.players

    def update_model(self, timedelta: float):

        for b in self.get_balls():
            b.update_pos(timedelta)
