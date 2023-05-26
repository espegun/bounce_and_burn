from abc import ABC, abstractmethod
from Ball import Ball

class Player(ABC):

    def __init__(self, name: str, ball: Ball):

        self.name = name
    
    @abstractmethod
    def get_action(self):
        raise NotImplementedError


class PlayerHuman(Player):

    def __init__(self, name: str, ball: Ball):

        super().__init__(name, ball)

    def get_action(self, keys_from_controller):
        return None
