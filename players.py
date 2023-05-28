from abc import ABC, abstractmethod
from Ball import Ball

class Player(ABC):

    def __init__(self, name: str, ball: Ball):

        self.name = name
        self.ball = ball
    
    def get_ball(self):
        return self.ball
    
    @abstractmethod
    def get_actions(self):
        raise NotImplementedError



class PlayerHuman(Player):

    def __init__(self, name: str, ball: Ball, up_key: int, down_key: int, right_key: int, left_key: int):

        super().__init__(name, ball)
        self.actions = None
        self.up_key = up_key
        self.down_key = down_key
        self.right_key = right_key
        self.left_key = left_key


    def convert_keys_pressed_to_actions(self, keys_pressed: tuple):

        self.actions = {"x_acc": 0,
                        "y_acc": 0}

        if keys_pressed[self.up_key]:
            self.actions["y_acc"] -= 1
        if keys_pressed[self.down_key]:
            self.actions["y_acc"] += 1
        if keys_pressed[self.right_key]:
            self.actions["x_acc"] += 1
        if keys_pressed[self.left_key]:
            self.actions["x_acc"] -= 1


    def get_actions(self):
        return self.actions
    

