from abc import ABC, abstractmethod
from Ball import Ball

class Player(ABC):

    def __init__(self, name: str, ball: Ball):

        self.name = name
    
    @abstractmethod
    def get_actions(self):
        raise NotImplementedError


class PlayerHuman(Player):

    def __init__(self, name: str, ball: Ball, up_key: int, down_key: int, right_key: int, left_key: int):

        super().__init__(name, ball)
        self.actions = None
        self.up_key = up_key
        self:down_key = down_key
        self.right_key = right_key
        self.left_key = left_key

    def reset_actions(self):

        self.actions = {"x_acc": 0,
                        "y_acc": 0}

    def convert_events_to_actions(self, events):
        
        
        
        
        decide_actions_from_events

    def get_actions(self):
        return self.actions
    

