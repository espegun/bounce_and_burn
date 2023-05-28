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

    def update_model(self, time_delta: float, keys_pressed: tuple):

        # Get player actions
        for p in self.players:
            p.convert_keys_pressed_to_actions(keys_pressed)

        # Implement actions (so far just in balls)   
        for p in self.players:
            actions = p.get_actions()
            b = p.get_ball()
            b.update_acc_from_actions(actions["x_acc"], actions["y_acc"])

        # Execute physics  
        for b in self.get_balls():    
            b.update_speed_and_pos(time_delta)
