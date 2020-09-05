from Ball import Ball

class Game(object):

    def __init__(self):

        self.Balls = []


    def add_Ball(self, ball):

        assert isinstance(ball, Ball)

        self.Balls.append(ball)


    def get_Balls(self):

        return self.Balls

